from flask import Flask, request, jsonify, make_response, session, send_file
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
import hashlib
import time
import sys
import logging

sys.path.append(r'D:\study\cs\se\se_porject\new_proj\neural-style-tf-master1\neural-style-tf-master')

from torch_test_v2 import style_transfer

app = Flask(__name__)
CORS(app, supports_credentials=True)

#database connect
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/se_proj'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'abcde'
db = SQLAlchemy(app)

BASE_UPLOAD_FOLDER = os.path.abspath('image')
CONTENT_UPLOAD_FOLDER = os.path.join(BASE_UPLOAD_FOLDER, 'content_img')
STYLE_UPLOAD_FOLDER = os.path.join(BASE_UPLOAD_FOLDER, 'style_img')

#new image folder
IMAGE_FOLDER = os.path.join(os.getcwd(), 'image', 'new_img')

#database tables
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)

class NewImage(db.Model):
    __tablename__ = 'new_img'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(255), nullable=False)

class TransferOperation(db.Model):
    __tablename__ = 'transfer_operation'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    new_img_id = db.Column(db.Integer, nullable=False)
    style_id = db.Column(db.String(255), nullable=False)
    content_id = db.Column(db.String(255), nullable=False)
    time = db.Column(db.DateTime, default=db.func.current_timestamp())

class Admin(db.Model):
    __tablename__ = 'admins'
    admin_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class ContentImage(db.Model):
    __tablename__ = 'content_img'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(255), nullable=False)

class StyleImage(db.Model):
    __tablename__ = 'style_img'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(255), nullable=False)

def create_tables():
    with app.app_context():
        db.create_all()

create_tables()

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data.get('name')
    password = data.get('password')
    email = data.get('email')

    new_user = User(name=name, password=password, email=email)
    db.session.add(new_user)
    try:
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Database error', 'error': str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(name=username, password=password).first()

    if user:
        #store usr info by session
        session['user_id'] = user.id
        session['name'] = user.name
        session['email'] = user.email

        #check admin info
        admin = Admin.query.filter_by(user_id=user.id).first()
        session['isadmin'] = admin is not None

        r = make_response(jsonify({'message': 'Login successful'}))
        r.set_cookie('user_id', str(user.id))
        return r
    else:
        return jsonify({'message': 'wrong'}), 401

#home main fuctions
@app.route('/transfer', methods=['POST'])
def transfer():
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'message': 'User not log in'}), 401

        content_file = request.files['content']
        style_file = request.files['style']
        content_filename_hash = hashlib.md5(f"content_{user_id}_{content_file.filename}".encode()).hexdigest()
        style_filename_hash = hashlib.md5(f"style_{user_id}_{style_file.filename}".encode()).hexdigest()

        content_path = os.path.join(CONTENT_UPLOAD_FOLDER, f"content_{user_id}_{content_filename_hash}.png")
        style_path = os.path.join(STYLE_UPLOAD_FOLDER, f"style_{user_id}_{style_filename_hash}.png")
        content_file.save(content_path)
        style_file.save(style_path)

        content_image = ContentImage(user_id=user_id, url=content_path)
        style_image = StyleImage(user_id=user_id, url=style_path)
        db.session.add(content_image)
        db.session.add(style_image)
        db.session.commit()

        output_image_path = os.path.join(IMAGE_FOLDER, f"styled_{user_id}_{int(time.time())}.jpg")

        #transfer function
        style_transfer(content_path, style_path, output_image_path)

        #save to the folder
        new_image = NewImage(user_id=user_id, url=output_image_path)
        db.session.add(new_image)
        db.session.commit()

        #mark in the database
        transfer_operation = TransferOperation(
            user_id=user_id,
            new_img_id=new_image.id,
            style_id=style_image.id,
            content_id=content_image.id
        )
        db.session.add(transfer_operation)
        db.session.commit()

        return jsonify({'url': f'/download/{os.path.basename(output_image_path)}'}), 201

    except Exception as e:
        logging.error("Error during style transfer", exc_info=True)
        return jsonify({'message': 'Internal server error', 'error': str(e)}), 500

@app.route('/api/getUserInfo', methods=['GET'])
def get_user_info():
    user_id = session.get('user_id')
    name = session.get('name')
    email = session.get('email')
    isadmin = session.get('isadmin', False)
    if user_id:
        return jsonify({'name': name, 'email': email, 'user_id': user_id, 'isadmin': isadmin}), 200
    else:
        return jsonify({'message': 'User not log in'}), 401

#sign out api
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'Log out successfully'}), 200

@app.route('/update/username', methods=['POST'])
def update_username():
    data = request.json
    new_name = data.get('name')
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'message': 'User not log in'}), 401

    user = User.query.get(user_id)
    if user:
        user.name = new_name
        db.session.commit()
        return jsonify({'message': 'Username updated successfully'}), 200
    return jsonify({'message': 'wrong'}), 404

#delete account API
@app.route('/delete/account', methods=['DELETE'])
def delete_account():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'message': 'User not log in'}), 401

    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        session.clear()
        return jsonify({'message': 'Account deleted successfully'}), 200
    return jsonify({'message': 'wrong'}), 404

@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'message': str(e)}), 500

@app.route('/api/deleteUser/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    return jsonify({'message': 'User not found'}), 404

@app.route('/api/promoteToAdmin', methods=['POST'])
def promote_to_admin():
    data = request.json
    user_id = data.get('userId')
    user = User.query.get(user_id)
    if user:
        new_admin = Admin(user_id=user.id)
        db.session.add(new_admin)
        db.session.commit()
        return jsonify({'message': 'User promoted to admin successfully'}), 200
    return jsonify({'message': 'User not found'}), 404

@app.route('/api/getUsers', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = []
    for user in users:
        is_admin = Admin.query.filter_by(user_id=user.id).first() is not None
        user_list.append({
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'is_admin': is_admin
        })
    return jsonify(user_list), 200

@app.route('/download/<filename>')
def download_image(filename):
    try:
        file_path = os.path.join(IMAGE_FOLDER, filename)
        if not os.path.exists(file_path):
            return jsonify({'message': 'File not found'}), 404

        return send_file(file_path, as_attachment=True)
    except Exception as e:
        logging.error("Error sending file", exc_info=True)
        return jsonify({'message': 'File not found'}), 404

@app.route('/api/deleteOperation/<int:operation_id>', methods=['DELETE'])
def delete_operation(operation_id):
    operation = TransferOperation.query.get(operation_id)
    if operation:
        db.session.delete(operation)
        db.session.commit()
        return jsonify({'message': 'Operation deleted successfully'}), 200
    return jsonify({'message': 'Operation not found'}), 404

@app.route('/api/getUserHistory', methods=['GET'])
def get_user_history():
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'message': 'User not log in'}), 401

        operations = TransferOperation.query.filter_by(user_id=user_id).all()
        history = []
        for op in operations:
            new_image = NewImage.query.get(op.new_img_id)
            if new_image:
                history.append({
                    'id': op.id,
                    'new_img_id': op.new_img_id,
                    'content_id': op.content_id,
                    'style_id': op.style_id,
                    'time': op.time,
                    'url': new_image.url
                })
        return jsonify(history), 200

    except Exception as e:
        logging.error("Error fetching user history", exc_info=True)
        return jsonify({'message': 'Internal server error', 'error': str(e)}), 500

@app.route('/update/password', methods=['POST'])
def update_password():
    try:
        data = request.json
        new_password = data.get('password')
        
        if not new_password:
            return jsonify({'message': 'Password is required'}), 400

        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'message': 'User not logged in'}), 401

        #directly change
        user = User.query.get(user_id)
        if user:
            user.password = new_password
            db.session.commit()
            return jsonify({'message': 'Password updated successfully'}), 200
        else:
            return jsonify({'message': 'User not found'}), 404

    except Exception as e:
        logging.error("Error updating password", exc_info=True)
        return jsonify({'message': 'Internal server error', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)