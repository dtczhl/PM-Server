# PM-Server

**Internal Use**  
**All are welcome to edit**

Advisor: *Prof.* [Prasant Mohapatra](https://faculty.engineering.ucdavis.edu/mohapatra/)  
Maintainer: [Huanle Zhang](https://www.huanlezhang.com)

## Access Docker Environment
* IP address: http://169.237.7.61:8000
* Username: FirstnameLastname (Change your password ASAP)

    <img src="./images/docker_login.png" width=500/>

* One docker Volume is created for each one. Do not delete it or create new one. You're only allowed to access the folder/path of the assigned Volume.
* To access your Volume data, use SFTP with username: FirstnameLastname (Come to me to change your SFTP password)

### Important!

* Please remove unused docker images and containers to save space.
* Please do **NOT** use the server to store your data. We have ordered a data station and you can save your data there.

## Tutorial

This tutorial will show you how to use the server.

1. Download the `tutorial` folder
1. `app.py` is the program as shown below. It prints out some messages, and write a string to a file named `/data/tutorial.txt`.

    <img src="./images/app.png" width=400 />
1. `requirements.txt` specifies external packages your program is dependent on. Since we only use builtin `time` and `os` packages in this tutorial, this file is empty.
1. `Dockerfile` specifies how to run your program.

    <img src="./images/dockerfile.png" width=500 />
1. Build docker image. Under this tutorial folder, run
    ```
    docker build --tag=my_tutorial .
    ```
    `--tag` is your docker image name
1. After executing the previous command, the docker image has been installed in you host machine already. To show your docker images, run
    ```
    docker image ls
    ```
    You can see `my_tutorial` docker image as shown below

    <img src="./images/docker_img_ls.png" width=600 />
1. To save `my_tutorial` docker as an archive file so that you can upload to the server. Run
    ```
    docker save -o my_tutorial.tar my_tutorial
    ```
    `-o` specifies the output path/filename. `my_tutorial` is the docker name
1. Upload to server. Login into the server, under `images` tag, click `Import` button

    <img src="./images/images_docker.png" width=600 />
1. Upload `my_tutorial.tar`
1. Go to `Containers` tag, click `Add container`, fill in Name, Image, scroll down to the Volumes tag, click map additional volume, type in `/data` (because we save a file to `/data/tutorial.txt`), select your volume named FirstnameLastname (everyone is pre-allocated with one)

    <img src="./images/container_docker.png" width=600 />
1. Click `Deploy the container`. Your docker image is running automatically. It stops after it finish running the program.
1. Click the `Logs` under `Quick actions`, you can see the output from `print()`

    <img src="./images/log_docker.png" width=600 />
1. To access `/data/tutorial.txt`, login in using any SFTP client you like (I'm using FileZilla in Ubuntu). Type in the IP address (same as the server, but without the port number), username (FirstnameLastname), your password, and port 22. You can find the `tutorial.txt` file under your `Volume` directory
