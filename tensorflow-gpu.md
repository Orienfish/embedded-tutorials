# Install TensorFlow GPU Support

## Set up on Manjaro Linux

* Test environment:

  * OS: Manjaro 21.0 Ornara
  * Geforce GTX 1060 3GB

* Install NVIDIA GPU Drivers.

  * Option 1: automatic install using the standard Ubuntu Repository

    * Auto detect and install an appropriate proprietary Nvidia driver on your Manjaro 21 Linux system.

      ```bash
      sudo mhwd -a pci nonfree 0300
      ```

    * Once the installation is concluded, reboot your system and you are done:

      ```bash
      sudo reboot
      ```

    * Start Nvidia Settings application to further configure your graphic card:

      ```bash
      nvidia-settings
      ```

  * Option 2: Manual Install using the Official NVIDIA driver

    * Update your system to load the latest kernel image

      ```bash
      sudo pacman -Syu
      ```

    * 

  * Simply run `nvidia-smi` to confirm a successful installation.

* To simplify installation and avoid library conflicts, the official tensorflow website recommends using a [TensorFlow Docker image with GPU support](https://www.tensorflow.org/install/docker).

  * [Install docker]
  * 

### Resources

[Tensorflow GPU Support](https://www.tensorflow.org/install/gpu)

[How to install the NVIDIA drivers on Manjaro Linux](https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-manjaro-linux)

