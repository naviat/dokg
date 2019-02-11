## My test package

### STEP to upload your package

1.  Install the required packages:

- `Setuptools`: Setuptools is a package development process library designed for creating and distributing Python packages.
- `Wheel`: The Wheel package provides a bdist_wheel command for setuptools. It creates .whl file which is directly installable through the pip install command. We'll then upload the same file to pypi.org.
- `Twine`: The Twine package provides a secure, authenticated, and verified connection between your system and PyPi over HTTPS.
- `Tqdm`: This is a smart progress meter used internally by Twine.

```
sudo python -m pip install --upgrade pip setuptools wheel
sudo python -m pip install tqdm
sudo python -m pip install --user --upgrade twine
```

1. Setup project

- Create folder structure follow this repo
- Package file sample `dokg`

```
#!/usr/bin/env python
echo "hey there, this is my first pip package"
```

- Make script excecutable:
    `chmod +x dokr`

- Create a setup file setup.py in your package. This file will contain all your package metadata information. 

```
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name = 'dokg',
    version = '0.3',
    scripts = ['dokg'],
    author = 'Hai V.Dam',
    author_email = 'haidv@tomochain.com',
    description  = 'My test package',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/naviat/dokg',
    packages = setuptools.find_packages(),
    classifiers = [
         "Programming Language :: Python :: 3",
         "Programming Language :: Python :: 2",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
)
```

1. Compiling Your Package

Go into your package folder and execute this command: `python setup.py bdist_wheel`. This will create a  structure like this:

```
.
├── LICENSE
├── README.md
├── build
│   ├── bdist.macosx-10.7-x86_64
│   └── scripts-3.7
│       └── dokg
├── dist
│   └── dokg-0.3-py3-none-any.whl
├── dokg
├── dokg.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   └── top_level.txt
└── setup.py
```

- `build`: build package information.

- `dist`: Contains your .whl file. A WHL file is a package saved in the Wheel format, which is the standard built-package format used for Python distributions. You can directly install a .whl file using pip install some_package.whl on your system

- `project.egg.info`: An egg package contains compiled bytecode, package information, dependency links, and captures the info used by the setup.py test command when running tests.

1. Upload on pip

- Create pypirc: The Pypirc file stores the PyPi repository information. Create a file in the home directory

for Windows :  `C:\Users\UserName\.pypirc`

for *nix :   `~/.pypirc`

And add the following content to it. Replace javatechy with your username.

```
[distutils] 
index-servers=pypi
[pypi] 
repository = https://upload.pypi.org/legacy/ 
username = naviat
```