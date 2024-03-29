# How to set up your own Docker environment

The goal of this tutorial is to set up your own Docker environment on your machine, so that you are able to create a container for your code. Such a container is very useful in that, it protects the environment when system update happens in the future.

## Set up docker on Ubuntu Linux

* Environment: 
  * Ubuntu 20.04 LTS
  * Docker
* Set up Docker's Apt repository

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

* Install the Docker packages

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

* Verify that the Docker Engine installation is successful by running the `hello-world` image

```bash
sudo docker run hello-world
```

This command downloads a test image and runs it in a container. When the container runs, it prints a confirmation message and exits.

* To run Docker without root, you need to add your account to the `docker` group with the following command and reboot your machine to make it work:

```bash
sudo usermod -aG docker $USER
```

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

If you want to access the GPUs from the container:

```bash
docker run --gpus all --name <container_name> -d -i -t ljiang98/fedthe_iclr2023:latest /bin/sh
```

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

[How to Use GPU from a Docker Container](https://saturncloud.io/blog/how-to-use-gpu-from-a-docker-container-a-guide-for-data-scientists-and-software-engineers/)

[Installing the NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
