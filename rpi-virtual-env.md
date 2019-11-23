# Setup Virtual Environment on Raspberry Pi

## Procedures

1. (Optional) Install Python 3.5 and change the link of Python3 to Python 3.5.

   ```shell
   sudo apt-get install python3.5
   sudo rm /usr/local/bin/python3
   sudo ln -s /usr/local/bin/python3.5 /usr/local/bin/python3
   ```

   In the following steps, `python3` can be used to replace `python3.5`. I just explicitly use `python3.5` for safety.

2. Install virtualenv and virtualenvwrapper.

   ```
   sudo python3.5 -m pip install virtualenv
   sudo python3.5 -m pip install virtualenvwrapper
   ```

3. Determine the version of Python to attach to. Find the path to executables by:

   ```shell
   which python3.5
   ```

   Add the following lines to the end of `~/.profile`, where `/usr/bin/python3` is what returned by the above command.

   ```shell
   VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.5
   export WORKON_HOME=$HOME/.virtualenvs
   source /usr/local/bin/virtualenvwrapper.sh
   ```

   In this way, VEs are stored in the hidden directory `.virtualenvs` located at your home path. 

   Run the profile with:

   ```shell
   source ~/.profile
   ```

4. The command **mkvirtualenv** can now be used to create python virtual environments as shown below.

   ```shell
   mkvirtualenv whatever -p /usr/bin/python3.5
   ```

   The directory “whatever” is a subdirectory of `~/.virtualenvs`. 

   To activate the VE “whatever” in any Terminal window enter:

   ```shell
   source ~/.profile
   workon whatever
   ```

   Your prompt now begins with (whatever). This means you are now working in the VE named “whatever”. All packages installed using pip3 (when the whatever VE is active) are placed in the site-packages directory located at `~/.virtualenvs/whatever/lib/python3.7/site-packages` (In this case, the version of Python is 3.7).

   To deactivate a virtual environment type:

   ```shell
   deactivate
   ```

## Resources

[Virtual Environments on the Raspberry Pi](https://medium.com/@ronm333/virtual-environments-on-the-raspberry-pi-ead158a72cd5)