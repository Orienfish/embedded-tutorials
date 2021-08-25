### Setup virtual environment for Python

All commands in this tutorial are for macOS and Linux platforms.

### Installation

* Install `virtualenv` and virtual `wrapper`

```bash
python3 -m pip install --user virtualenv virtualenvwrapper
```

### Create a virtual environment under a Python project

* Create a virtual environment

```bash
python3 -m venv <name-of-your-env>
```

* Activate a virtual environment

```bash
source <name-of-your-env>/bin/activate
```

* Exit the environment

```bash
deactivate
```

### Use `virtualenvwrapper` to manage all virtual environments

* Taking my macOS as an example, add the following lines to the end of your shell startup file (`.bashrc`, `.zshrc`, `.profile`, etc.) to set the location where the virtual environments should live, and the location of the script installed with this package:

```bash
VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3.9
export WORKON_HOME=$HOME/.virtualenvs
source /Library/Frameworks/Python.framework/Versions/3.9/bin/virtualenvwrapper.sh
```

Make sure the Python version is the same as the one you install `virtualenvwrapper` for.

If you are not able to find `virtualenvwrapper.sh`, you can use the following command:

```bash
which virtualenvwrapper.sh
```

After editing it, reload the startup file, e.g., `source ~/.zshrc`.

* Create virual environment named "whatever" under `~/.virtualenvs` and activate it

```
mkvirtualenv whatever
workon whatever
```

To list the existing environments:

```bash
workon
```

Your prompt now begins with (whatever). This means you are now working in the VE named “whatever”. All packages installed using pip3 (when the whatever VE is active) are placed in the site-packages directory located at `~/.virtualenvs/whatever/lib/python3.9/site-packages` (In this case, the version of Python is 3.9).

To deactivate a virtual environment type:

```bash
deactivate
```

### Useful tips

* Export a list of all installed packages and their versions

```bash
python3 -m pip freeze > requirements.txt
```

* `lsvirtualenv`: List all of the environments.

  `cdvirtualenv`: Navigate into the directory of the currently activated virtual environment, so you can browse its `site-packages`, for example.

  `cdsitepackages`: Like the above, but directly into `site-packages` directory.

  `lssitepackages`: Shows contents of `site-packages` directory.

* Follow this [guide](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html) to configure virtual environment in PyCharm.

### Resources

[Virtual Environments, Guide to Python](https://python-guide-ru.readthedocs.io/en/latest/dev/virtualenvs.html)

