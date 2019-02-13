import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name = 'dokg',
    version = '0.4',
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
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
)