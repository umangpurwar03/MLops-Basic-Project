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
