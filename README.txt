Dataset has been downloaded and extracted from the MNIST website for OCR character Recognition

Load the binary files: The binary files in the MNIST dataset contain the images and labels as byte streams. You can use a library like NumPy to read in these files and convert them into arrays that can be used for training.

Preprocess the data: Before training your model, you'll need to preprocess the data to prepare it for training. This may include normalizing the pixel values, resizing the images to a fixed size, and splitting the data into training and validation sets.

Build the model: You can use a deep learning framework like TensorFlow or PyTorch to build a neural network model for OCR. A simple architecture that can be used for this task which gives highest accuracy for the above dataset. You'll need to define the architecture of the network, including the number of layers, the size of the filters, and the activation functions to be used.

model architecture for the MNIST dataset using TensorFlow:

This architecture is a feedforward neural network with three layers: two dense layers with ReLU activation functions and a softmax output layer. A Flatten layer is added at the beginning to flatten the input images to a 1D vector. Two Dropout layers are added to prevent overfitting during training.

Train the model: This involves using the labeled data to adjust the model's parameters so that it can accurately recognize text in new images. This step typically involves splitting the dataset into training and validation sets, and then using an optimization algorithm (such as stochastic gradient descent) to iteratively improve the model's performance.


Evaluate the model: This involves testing the model on a separate test dataset to assess its performance on new, unseen data. You may need to fine-tune the model based on the results of this evaluation.


The Deployment of this project is done using the python django


URL: http://127.0.0.1:8000/ocr

To execute:
1) set path to the project_directory
2) run this command: python manage.py runserver
3) open the link in browser 

Input: Takes an image file as input
Output: The Printed Digit and Accuracy  
