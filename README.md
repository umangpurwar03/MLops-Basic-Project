# Project Introduction

 I want to introduce you to my MLOps project, where we explore the fascinating world of Machine Learning Operations. I've also created an app for training linear regression, which is a way to understand and predict data patterns. It might not be perfect, but it's pretty neat!
 
## Project Overview

The main goal of this project is to demonstrate the seamless integration of machine learning and version control using GitHub. Through the following steps, I'll guide you on how I've brought this project to life:

**GitHub Repository**: I started by creating a GitHub repository as the central hub for this project. It's here that we'll manage our code and project files. This repository is public, which means anyone can explore it, making collaboration and sharing easy.

## The Machine Learning Journey

Besides setting up the project, there's also a machine learning part. I made a Python script that acts like our learning helper.You can check the file [**`View App Code`**](streamlit.py) This script deals with some [**`Data`**](data) I picked to teach a machine learning model.

So, whether you're curious about how machine learning works, want to grasp version control, or are just here to explore, you're in the right spot. This project aims to show that, with the right tools and some know-how, we can get data to do cool stuff for us.

If you have questions, want to team up, or just want to know more about this project, feel free to reach out. Let's go on this journey together!

# Docker Containerization

Greetings, fellow learners! In this exciting stage of our project, we're diving into the world of Docker to containerize our machine learning model and its dependencies. It's like putting everything we need into a neatly wrapped box.

**Here's how I did it:**

### 1. writing the Dockerfile

Our journey started with crafting a [**`Dockerfile`**](Dockerfile). Think of it as a formal recipe that guides Docker on how to create a container for our machine learning model. In this file, we meticulously listed all the necessary tools and libraries required by our model. It's like writing a specific shopping list for a grand cooking adventure.

### 2. Building the Docker Image

Once Dockerfile was ready, I invoked the **`docker build`** command (**docker build -t assignment .**)to piece together a **Docker image**. This image is akin to taking a photograph of our project at a specific moment, capturing all the vital components needed for running our model. It's like preserving a snapshot of project in a sturdy frame.

### 3. Storing the Docker Image

To share container with the world, decided to upload it to a trusted container registry. Our choice was **Docker Hub**, a reliable storage facility for Docker containers. This step is taken to storing container in a secure warehouse, accessible to anyone interested in using our project.

### 4. For using our Docker 

The command I used to run docker locally and connecting our port locally the method I used is **docker run -d -p 8000:8501 assignment**.

# Cloud Deployment on AWS

we all ready prepared our docker image

### Setting Up AWS

Next, we go to AWS, which is like a big place on the internet for projects. Here's what I did:

1. I logged into AWS using the AWS Management Console. It's like logging into your computer.
2. Then, I went to the EC2 Dashboard, which is like choosing what you want to do on your computer.
3. I started a new EC2 instance, which is like getting a special computer for our project. I chose one that fits our project's needs.
4. I set up the security group for the EC2 instance. It's like telling the computer who can visit our project. We want people to visit, so we tell the computer to let them in through a (port).

### Moving Our Docker Image to AWS

Now, we need to send our Docker image to AWS. It's like sending a letter to a friend. We use a command called `scp`:

```bash
scp -i ec2-key.pem assignment.tar ec2-user@ec2-public-ip:/path of ec2 instance where you want that tar file to be saved
```

### Opening Our Docker Image

When our Docker image arrives in AWS, we need to open it. It's like opening a box that you received in the mail. We do this with a command:

```bash
docker load -i /path to tar file in your aws
```

### Let the Project Begin

Now, our project is ready to be seen by everyone. It's like opening a shop for the first time. To do this, we start our Docker container with this command:

```bash
docker run -d -p 80:8501 assignment
```

This command is like turning on the lights and opening the doors for our project. It will be available on the internet on port 80.


### Sharing Our Project

Now, people can see our project. It's like telling your friends about your new shop. They can visit it by typing the AWS public IP address into their web browser:
[**`http://13.213.202.48`**](http://13.213.202.48)

# Automated Testing and CI/CD using Travis CI 

## Running Tests with Travis CI

Travis CI is like a watchful guardian for our code. Whenever we make changes and upload them here, Travis CI steps in to run these tests to make sure our code is in good shape.

### Understanding Our Tests

Let's break down our tests and what they do:

1. **Testing Model Training**:
   - This test, `test_train_model`, checks if we can train our machine learning model. We read movie data, select features, and ratings to use in training. After splitting the data into training and non-training parts, we train our model using the training data. This test ensures that our model is successfully trained and is not empty. The line `self.assertIsNotNone(model)` checks that the model is not None.

2. **Testing Model Predictions**:
   - The `test_make_predictions` test is all about checking if we can make predictions using our trained model. Just like before, we prepare our data and split it into training and non-training sections. We train the model again and then predict ratings on the training data. This test ensures that predictions are generated successfully, and they are not empty.

3. **Assessing Model Performance**:
   - In the `test_model_performance` test, we evaluate our model's performance. We perform similar data preparation and model training as in the previous tests. After training, we make predictions both on the training and test data. Then, we calculate the mean squared error (MSE) for both sets of predictions. Finally, we determine if the model's performance is good, bad, or somewhere in between. The `self.assertTrue(test_mse >= train_mse)` line asserts that the test MSE is less than or equal to the train MSE.

4. **Streamlit App Testing**:
   - We've also added a new test, **`testing.py`**, for your Streamlit app. This test checks if your Streamlit app runs smoothly and loads without errors. This test can be run locally using the `testing.py` file. It ensures that your app is working as expected.

### The Travis CI 

Travis CI is like our trusty assistant. To make all this happen, we have a special file called **`.travis.yml`. This file gives Travis CI instructions on which version of Python to use, how to set things up, and where to find the data for the tests. This way, we ensure our machine learning code stays in tip-top shape.

### Checking Our Progress

See that badge up there? It tells us whether the tests passed or not. Click on it to view the test results, kind of like looking at a report card for our code.

### Test Results

Travis CI keeps a record of all the tests it runs. You can check the details on the Travis CI website or by clicking the badge. This record helps us make sure our machine learning code is working as expected.

If you have any questions or need assistance, please don't hesitate to reach out. You can start a chat or send us a message directly.

## How to Get Started

Interested in trying out our project on your computer? It's not as hard as it seems! Here's what you need to do:

1. First, you need to grab a copy of our project and bring it to your computer. You can do that with this command:

```bash
git clone https://github.com/umangpurwar03/MLops-Basic-Project.git
```

This project is managed by **`Umang Purwar`**. You can contact me at [**`umangpurwar03@gmail.com`**](umangpurwar03@gmail.com).
