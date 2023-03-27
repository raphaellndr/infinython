# Chocolatine

## Installation instructions

### Prerequisites

In order to generate a python project from this repository, you need to 
have [cookiecutter](https://github.com/cookiecutter/cookiecutter) installed 
on your machine. You can find the instructions [here.](https://cookiecutter.readthedocs.io/en/stable/installation.html#install-cookiecutter)
Obviously, you also need to have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
installed.

## Usage

Once cookiecutter installed, you are set to generate an empty python project
using this repository. You can achieve this by either cloning the repo 
locally or working directly with git.

### Cloning the repository

On your machine, simply run the following command to clone the repository
locally:

````shell
git clone git@void.visiblepatient.com:rlandure/chocolatine.git
````

Then, to generate the project:

````shell
cookiecutter chocolatine
````

### Working with git

Where you want to generate your project, run the following command:

````shell
cookiecutter git@void.visiblepatient.com:rlandure/chocolatine.git
````

---

In both cases, you will be prompted to enter a few config values (defined
in *coockiecutter.json*). Once done, Cookiecutter will generate a project 
from the template, using the entered values.
