# neural_style_tf_MIS
Chapter 3	Proposed project description
3.1	Problem diagnosis
3.1.1	detailed explanation
The neural style transfer is a technology that combines the content of one image with the style of another image through convolutional neural network to generate a more personalized and artistic image. The open source project "neural-style-tf" provides a TensorFlow implementation of this technology. This technology has attracted a lot of attention in the context of the highly developed era of artificial intelligence, and many people want to use this project to have fun. However, this open source project still has some shortcomings.
3.1.2	problem domain
In terms of function, the "neural-style-tf" project has strict requirements for image input. Images do not fit the required size cannot be used as input, and images with different pixels cannot be combined. This is unfriendly to users, because they do not need to deliberately adjust the image attributes, which is cumbersome and will bring unnecessary trouble to users. A good software system should simplify this operation and let the back end process the image attributes automatically, saving the user time.
At the same time, the amount of images input as content can only be 1, which cannot achieve picture stitching. Sometimes users will want to use multiple images as input at the same time, splicing pictures in content, and applying different combinations in style. Unfortunately, this open source project only allows multi-value input for style images, which is unreasonable and flawed. We will solve this problem and make the software more versatile.
  
In terms of user experience, as a research project, the technology does not have a user-friendly visual interface. If the technology is to be widely distributed among the public, it should be embedded in a software system that handles user interaction and effectively manages image data. For example, users do not have to configure environments such as TensorFlow, pytouch, etc., nor do they have to use the command line to run the program, which is too complex for the user. In addition, in order to make the technology available to the public, we also need to support multiple users online at the same time, and we need to address the need for users to view history.

3.2	Proposed treatment
3.2.1	Problem diagnosis
In the field of art and design, endowing the same image with different styles to meet the needs of users is a complex and challenging task. We focus on solving one of the core problems that users face in the process of image creation and design: how to quickly generate high-quality artistic style images. Traditional image processing methods often require professional skills and a lot of time, which not only affects creative efficiency but also limits the creativity of many users. Therefore, in order to enhance the user experience, we plan to design a diverse user interface so that users can not only enjoy a smooth experience during operation, but also access rich functions. 
Figure：Software Function Example
3.2.2	Specific intervention measures
We will set a series of success indicators, including user satisfaction, production speed, and image quality. Through user surveys, we will collect feedback to evaluate user satisfaction, with the goal of reducing image generation time to just a few seconds. Meanwhile, we will use image quality assessment metrics such as PSNR and SSIM to ensure that the quality of the output images meets industry standards. Customers can confirm our commitment through case studies and quantitative results. We regularly collect user feedback to continuously optimize our products. 
 
If we encounter characteristics such as long and slow code running time, we will use matrix optimization to improve the code. Through matrix optimization, we can achieve storage space savings and improve computational efficiency. And with this optimization, we can continuously improve the numerical stability of the algorithm. And our product will inevitably face a large user base, and matrix optimization algorithms can process larger datasets and extract effective information.
3.2.3	Customer feedback and Expected benefits
Our solution aims to promote the application of artificial intelligence in the art industry, reduce labor costs, and bring significant time and economic benefits to art practitioners. Users can generate high-quality images in a short period of time, which not only lowers the skill threshold for creation, but also enhances their creative expression ability. In addition, the rich features and good user experience will increase user stickiness, further enhance the reputation of the development team, and make our product stand out in the market.
3.2.4	Example scenario description
For example, suppose marketers need to create a visually appealing advertising image for an upcoming product release. Under traditional methods, designers may need several days to complete this task. Through our system, users only need to upload product images and selected art styles, and the system will quickly generate images, allowing users to adjust style intensity and details in real time. This process is completed within a few seconds, and users can download the final image, greatly meeting the time constraint requirements.
3.2.5	Advantages of the solution
Compared to traditional design methods, our solution not only saves time but also greatly reduces reliance on professional designers, increasing flexibility and creative freedom. Users can adjust and optimize the design according to their own needs at any time, creating more personalized works. These measures not only effectively solve the current problems, but also bring huge commercial value to users and customers, promoting a new era of artistic creation.
In order to provide a user-friendly interface, we will use a front-end separation of work, build a database, create a complete software system. There will be embedded deep learning models that will serve our software.
To solve the problem of image attribute limitation, our front end will allow the user to enter a variety of different sizes and pixels of the image, and the back end will adjust these images to fit the required format before entering the model.
 
