# Install NVIDIA GPU Driver on Linux

## Set up on Manjaro Linux

* Test environment:

  * OS: Manjaro 21.1.2 Pahvo
  * Linux Kernel 5.4
  * Geforce GTX 1060 3GB

* Before starting installation, you need to check if your Linux kernel version is compatible with NVIDIA drivers. Avoid Linux Kernel 5.9 for this reason.

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

    * Update your system to load the latest kernel image:

      ```bash
      sudo pacman -Syu
      ```

    * Identify your NVIDIA VGA card.The below commands will allow you to identify your Nvidia card model:

      ```
      lspci -vnn | grep VGA
      ```

    * Download official NVIDIA driver from [website](https://www.nvidia.com/Download/index.aspx).

    * Install prerequisites. First we detect the currently kernel version:

      ```bash
      $ uname -r
      5.4.116-1-MANJARO
      ```

      Then we can go on to install the kernel headers and development tools:

      ```bash
      sudo pacman -S linux54-headers
      sudo pacman -S base-devel dkms
      ```

    * Next we will disable the default `nouveau` drivers, as required in manual installation of NVIDIA driver. We edit the `/etc/default/grub` configuration file, locate the line starting with `GRUB_CMDLINE_LINUX` and include the following code: `nouveau.modeset=0`. After the modification, the line should be like:

      ```
      GRUB_CMDLINE_LINUX="nouveau.modeset=0"
      ```

      Then we update the grub via `sudo update-grub` and reboot the system.

    * Next we begin the actual installation of NVIDIA driver:

      ```bash
      sudo bash NVIDIA-Linux-x86_64-xx.run
      ```

      Reboot after completion

  * Simply run `nvidia-smi` to confirm a successful installation.

## Resources

[Tensorflow GPU Support](https://www.tensorflow.org/install/gpu)

[How to install the NVIDIA drivers on Manjaro Linux](https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-manjaro-linux)

[NVIDIA graphics driver installation documentation on Manjaro](https://github.com/imbarismustafa/manjaro-nvidia)

