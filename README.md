# Rock, Paper, Scissors, shoot!
Fall 2023 ECE 4554/5554 Computer Vision: Course Project

## Names of Team Members Here
Henry Forsyth, Sagar Ranga, Shefali Ranjan

---


## Problem Statement
The goal of our project is to develop a real-time hand gesture recognition system that leverages a pre-trained model to accurately detect and classify hand gestures for playing rock-paper-scissors against a user.

## Approach
Our approach for this project involves two main stages: hand detection and hand gesture classification. For hand detection, we plan to use a pre-trained deep learning model, such as a pre-trained Faster R-CNN or YOLO, to localize the hand within the image. For hand gesture classification, we will use transfer learning to fine-tune a pre-trained convolutional neural network (CNN), such as VGG or ResNet, on a dataset of hand gesture images to classify the detected hand region into one of the four classes: rock, paper, scissors, or none/undecided. "None" or "Undecided" will be decided by a threshold of confidence, so if the gesture doesn't match then it will be thrown out. We plan on using a two different thresholds to determine action that our model will take. If the confidence level is above 70%, then the model will output the symbol that will win against the player. If the confidence level is below 70% and above 30%, then the model will output the symbol that will lose against the player. If the confidence level is below 30%, then the model will output that the symbol was not recognized. Data augmentation techniques, such as rotation and scaling, will be used to increase the diversity of the training data. We will implement these models using deep learning frameworks such as TensorFlow or PyTorch.

An example of the dataset we are planning on training off of is found here:

[Dataset 1](https://public.roboflow.com/classification/rock-paper-scissors/1)

## Experiments and Results
Our experimental setup will involve collecting a dataset of hand gesture images with various backgrounds, lighting conditions, and hand orientations. We plan to split the dataset into training and testing sets, with 80% of the data used for training and 20% for testing. The evaluation metric used will be classification accuracy. We will fine-tune the hyperparameters of the model (e.g., learning rate, batch size) and observe their impact on performance. We will also compare the performance of the fine-tuned model against the pre-trained model.

For our experiments, we plan to perform the following:

Fine-tune the pre-trained CNN model on the training dataset and evaluate its performance on the test dataset.
Fine-tune the hyperparameters of the model and observe their impact on performance.
Test the model in a real-time scenario where it plays rock-paper-scissors against a user.
We expect the experiments to reveal the effectiveness of the proposed approach in detecting and classifying hand gestures for playing rock-paper-scissors. The fine-tuned model is expected to outperform the pre-trained model due to the domain-specific training. However, the performance may vary depending on the quality of the dataset, the choice of hyperparameters, and the real-time conditions during testing.
