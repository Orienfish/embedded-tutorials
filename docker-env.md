# How to set up your own Docker environment

The goal of this tutorial is to set up your own Docker environment on your machine, so that you are able to create a container for your code. Such a container is very useful in that, it protects the environment when system update happens in the future.

## Set up docker on Ubuntu Linux

Environment: Ubuntu 20.04 LTS

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

* 

### Resources

[Manjaro Linux Docker installation](https://linuxconfig.org/manjaro-linux-docker-installation)

