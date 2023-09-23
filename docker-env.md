# How to set up your own Docker environment

The goal of this tutorial is to set up your own Docker environment on your machine, so that you are able to create a container for your code. Such a container is very useful in that, it protects the environment when system update happens in the future.

## Set up docker on Ubuntu Linux

* Environment: 
  * Ubuntu 20.04 LTS
  * Docker

## Set up docker on Manjaro Linux

* Environment: 
  * Manjaro 20.2.1 Nibia
  * Docker 20.10.1 for both client and server

* To install and enable Docker, run the following commands:

```bash
sudo pacman -S docker # or 'yay -S docker' if you have yay
sudo systemctl enable docker.service # (optional) enable docker when the system is rebooted
sudo systemctl start docker.service # start docker service
```

You can use the following commands to check the version and basic information of your Docker:

```bash
sudo docker version
sudo docker info
```

* To run Docker without root, you need to add your account to the `docker` group with the following command and reboot your machine to make it work:

```bash
sudo usermod -aG docker $USER
```

## Quick Start from Pulled Image

* Pull the built image from online

```bash
docker pull ljiang98/fedthe_iclr2023:latest
```

* Run the container from image and keep the container running

```bash
docker run --name <container_name> -d -i -t ljiang98/fedthe_iclr2023:latest /bin/sh
```

The `-d` option (shorthand for `--detach`) sets the container to run in the background, in detached mode, with a pseudo-TTY attached (`-t`). The `-i` option is set to keep `STDIN` attached (`-i`), which prevents the `sh` process from exiting immediately. There are two alternative ways to keep the container running: [here](docker run -d -t ljiang98/fedthe_iclr2023:latest).

Check the list of running container:

```bash
docker ps    # show the running containers
docker ps -a # show all containers including the stop containers
```

* Start an interactive `sh` shell on the container:

```bash
docker exec -it <container_name> sh
```

Or, execute additional commands in the container:

```bash
docker exec -it <container_name> sh -c "echo a && echo b"
```

* Stop and remove the container

```bash
docker stop <container_name>
docker rm <container_name>
```

### Resources

[Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

[Manjaro Linux Docker installation](https://linuxconfig.org/manjaro-linux-docker-installation)
