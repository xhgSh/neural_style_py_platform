# Neural Style Transfer Platform

[English](#english) | [中文](#chinese)

---

## English

### Project Overview
A comprehensive neural style transfer platform combining TensorFlow and PyTorch implementations with a modern web interface. The platform provides both single image and video style transfer capabilities with user management and history tracking.

### Project Structure
```
neural-style-py-platform/
├── neural-style-tf-master1/          # TensorFlow implementation
│   └── neural-style-tf-master/
│       ├── neural_style.py           # Core style transfer algorithm
│       ├── torch_test_v2.py          # PyTorch implementation
│       ├── stylize_image.sh          # Single image processing script
│       ├── stylize_video.sh          # Video processing script
│       ├── image_input/              # Content images directory
│       ├── styles/                   # Style images directory
│       ├── image_output/             # Output images directory
│       └── video_input/              # Video processing utilities
├── flask/                            # Backend API server
│   ├── app.py                       # Flask application with REST APIs
│   ├── image/                       # Image storage directories
│   │   ├── content_img/             # Uploaded content images
│   │   ├── style_img/               # Uploaded style images
│   │   └── new_img/                 # Generated stylized images
└── vue/                             # Frontend web application
    └── nerual_style_tf_platform_front/
        ├── src/
        │   ├── views/               # Vue components
        │   │   ├── home.vue         # Main dashboard
        │   │   ├── login.vue        # Login page
        │   │   ├── management.vue   # Admin management
        │   │   └── history.vue      # User history
        │   └── api/                # API service layer
        └── package.json             # Node.js dependencies
```

### Environment Setup

#### Prerequisites
- Python 3.7+
- Node.js 16+
- MySQL 5.7+
- CUDA (optional, for GPU acceleration)

#### Backend Setup (Flask)
1. **Install Python dependencies:**
   ```bash
   pip install flask flask-cors flask-sqlalchemy pymysql torch torchvision tensorflow opencv-python-headless
   ```

2. **Configure MySQL:**
   - Create database: `CREATE DATABASE se_proj;`
   - Update connection string in `flask/app.py`:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost:3306/se_proj'
   ```

3. **Start Flask server:**
   ```bash
   cd flask
   python app.py
   ```
   Server runs on: `http://localhost:5000`

#### Frontend Setup (Vue)
1. **Install dependencies:**
   ```bash
   cd vue/nerual_style_tf_platform_front
   npm install
   ```

2. **Start development server:**
   ```bash
   npm run dev
   ```
   Application runs on: `http://localhost:5173`

#### TensorFlow Setup (Optional)
1. **Navigate to TensorFlow directory:**
   ```bash
   cd neural-style-tf-master1/neural-style-tf-master
   ```

2. **Download VGG-19 weights:**
   - Download `imagenet-vgg-verydeep-19.mat` from [VLFeat](http://www.vlfeat.org/matconvnet/pretrained/)
   - Place in project root directory

3. **Install dependencies:**
   ```bash
   pip install tensorflow==1.15.0 scipy opencv-python
   ```

### Running the Application

#### Method 1: Full Web Interface (Recommended)
1. **Start Flask backend:**
   ```bash
   cd flask
   python app.py
   ```

2. **Start Vue frontend:**
   ```bash
   cd vue/nerual_style_tf_platform_front
   npm run dev
   ```

3. **Access application:**
   - Open browser to `http://localhost:5173`
   - Register new account or login
   - Upload content and style images
   - Generate stylized images

#### Method 2: Command Line (TensorFlow)

**Single Image:**
```bash
cd neural-style-tf-master1/neural-style-tf-master
python neural_style.py \
  --content_img content.jpg \
  --style_imgs style.jpg \
  --max_size 512 \
  --max_iterations 1000
```

**Video:**
```bash
bash stylize_video.sh video.mp4 style.jpg
```

#### Method 3: Direct API Usage

**Upload and process:**
```bash
curl -X POST http://localhost:5000/transfer \
  -F "content=@content.jpg" \
  -F "style=@style.jpg" \
  -H "Cookie: user_id=your_user_id"
```

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/register` | POST | User registration |
| `/login` | POST | User authentication |
| `/transfer` | POST | Image style transfer |
| `/api/deleteUser/<id>` | DELETE | Delete user (admin) |
| `/api/promoteToAdmin` | POST | Promote user to admin |

---

## 中文

### 项目概述
一个结合TensorFlow和PyTorch实现的神经风格迁移平台，提供现代化的Web界面。支持单张图片和视频的风格迁移，包含用户管理和历史记录功能。

### 项目结构
```
neural-style-py-platform/
├── neural-style-tf-master1/          # TensorFlow实现
│   └── neural-style-tf-master/
│       ├── neural_style.py           # 核心风格迁移算法
│       ├── torch_test_v2.py          # PyTorch实现
│       ├── stylize_image.sh          # 单图片处理脚本
│       ├── stylize_video.sh          # 视频处理脚本
│       ├── image_input/              # 内容图片目录
│       ├── styles/                   # 风格图片目录
│       ├── image_output/             # 输出图片目录
│       └── video_input/              # 视频处理工具
├── flask/                            # 后端API服务器
│   ├── app.py                       # Flask应用与REST API
│   ├── image/                       # 图片存储目录
│   │   ├── content_img/             # 上传的内容图片
│   │   ├── style_img/               # 上传的风格图片
│   │   └── new_img/                 # 生成的风格化图片
└── vue/                             # 前端Web应用
    └── nerual_style_tf_platform_front/
        ├── src/
        │   ├── views/               # Vue组件
        │   │   ├── home.vue         # 主仪表板
        │   │   ├── login.vue        # 登录页面
        │   │   ├── management.vue   # 管理员管理
        │   │   └── history.vue      # 用户历史
        │   └── api/                # API服务层
        └── package.json             # Node.js依赖
```

### 环境配置

#### 系统要求
- Python 3.7+
- Node.js 16+
- MySQL 5.7+
- CUDA（可选，用于GPU加速）

#### 后端配置（Flask）
1. **安装Python依赖：**
   ```bash
   pip install flask flask-cors flask-sqlalchemy pymysql torch torchvision tensorflow opencv-python-headless
   ```

2. **配置MySQL：**
   - 创建数据库：`CREATE DATABASE se_proj;`
   - 修改`flask/app.py`中的连接字符串：
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://用户名:密码@localhost:3306/se_proj'
   ```

3. **启动Flask服务器：**
   ```bash
   cd flask
   python app.py
   ```
   服务器运行在：`http://localhost:5000`

#### 前端配置（Vue）
1. **安装依赖：**
   ```bash
   cd vue/nerual_style_tf_platform_front
   npm install
   ```

2. **启动开发服务器：**
   ```bash
   npm run dev
   ```
   应用运行在：`http://localhost:5173`

#### TensorFlow配置（可选）
1. **进入TensorFlow目录：**
   ```bash
   cd neural-style-tf-master1/neural-style-tf-master
   ```

2. **下载VGG-19权重：**
   - 从[VLFeat](http://www.vlfeat.org/matconvnet/pretrained/)下载`imagenet-vgg-verydeep-19.mat`
   - 放置在项目根目录

3. **安装依赖：**
   ```bash
   pip install tensorflow==1.15.0 scipy opencv-python
   ```

### 运行应用

#### 方式1：完整Web界面（推荐）
1. **启动Flask后端：**
   ```bash
   cd flask
   python app.py
   ```

2. **启动Vue前端：**
   ```bash
   cd vue/nerual_style_tf_platform_front
   npm run dev
   ```

3. **访问应用：**
   - 浏览器打开`http://localhost:5173`
   - 注册新账户或登录
   - 上传内容图片和风格图片
   - 生成风格化图片

#### 方式2：命令行（TensorFlow）

**单张图片：**
```bash
cd neural-style-tf-master1/neural-style-tf-master
python neural_style.py \
  --content_img content.jpg \
  --style_imgs style.jpg \
  --max_size 512 \
  --max_iterations 1000
```

**视频：**
```bash
bash stylize_video.sh video.mp4 style.jpg
```

#### 方式3：直接API调用

**上传并处理：**
```bash
curl -X POST http://localhost:5000/transfer \
  -F "content=@content.jpg" \
  -F "style=@style.jpg" \
  -H "Cookie: user_id=your_user_id"
```

### API接口文档

| 接口地址 | 方法 | 描述 |
|----------|------|------|
| `/register` | POST | 用户注册 |
| `/login` | POST | 用户认证 |
| `/transfer` | POST | 图片风格迁移 |
| `/api/deleteUser/<id>` | DELETE | 删除用户（管理员） |
| `/api/promoteToAdmin` | POST | 提升用户为管理员 |

### 故障排除

#### 常见问题
1. **MySQL连接失败：** 检查数据库配置和网络连接
2. **CUDA内存不足：** 使用CPU模式或减少图片尺寸
3. **前端跨域错误：** 确保CORS配置正确
4. **图片上传失败：** 检查文件大小限制和存储权限

#### 性能优化
- 使用GPU加速：确保安装CUDA和cuDNN
- 调整图片尺寸：通过`--max_size`参数控制
- 优化迭代次数：调整`--max_iterations`参数
 

