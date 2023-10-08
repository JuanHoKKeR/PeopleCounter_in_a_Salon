# PeopleCounter_in_a_Salon
This project is a people counter developed using Python, OpenCV, and DroidCam. It was specifically designed to operate on a Raspberry Pi 3.

Project Description:

This project is based on OpenCV tools for image transformation, employing elements such as image subtraction, morphology, and image dilation. The code implements these tools to create a single frame that detects whether people are entering or leaving a room, enabling us to count the current number of people inside.

To achieve real-time detection, we utilize the DroidCam app. This app proves useful when we either lack a camera or prefer to use a mobile device's camera. To establish the connection between the mobile camera, the app, and our program, we utilize the code found at [This Repository](https://github.com/cardboardcode/droidcam_simple_setup), which facilitates this connection.

<img src="https://github.com/JuanHoKKeR/PeopleCounter_in_a_Salon/blob/main/imagenApp.jpg?raw=true" alt="Image App" width="200">

For testing the code, we present an example using a video. In this example, you can observe how the frame is selected around the door, which is done to solely detect movement at the entrance.

<img src="https://github.com/JuanHoKKeR/PeopleCounter_in_a_Salon/blob/main/ContadorframeVideo.JPG?raw=true" alt="Image Counter" width="300">

The following image illustrates how the transformation works to detect a person entering through the use of subtraction to detect movement, morphology, and dilation to enhance the image, along with certain conditions related to the area of the contour to specifically detect the region near the heads of individuals.

<img src="https://github.com/JuanHoKKeR/PeopleCounter_in_a_Salon/blob/main/ContadorSustraccionVideo.JPG?raw=true" alt="Image CounterTransformation" width="300">

One limitation of this project is that it not only counts people but also detects any moving object within the frame. If the objective is to exclusively detect individuals, a convolutional model trained for head detection or a similar approach would be necessary.
