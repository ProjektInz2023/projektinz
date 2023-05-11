# Running the project
In order to download and run the project on your local machine follow these steps:

```
git clone https://github.com/ProjektInz2023/projektinz.git
```
Creates a copy of the repository.
```
cd projektinz/
```

Moves inside directory. 

```
py -m venv venv (windows)
python3 -m venv venv (linux)
```
Creates a virtual environment, that allows you to manage separate package installations for this project.

```
venv\Scripts\activate (windows)
source venv/bin/activate (linux)
```
Activate a virtual environment which puts the virtual environment-specific python and pip executables into your shell’s PATH.

```
pip install -r requirements.txt
```
Install the packages with for a specified version.

Note that it might be necessary to execute `python` instead of `python3`, depending on unix-like distributions.
