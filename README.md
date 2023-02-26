# Cookiecutter for MLOps projects

🍪 Cookiecutter is a CLI utility that allows us to create projects from cookiecutters (project templates), e.g. creating a data science project using the same files and folder structure you usually use.

**Example proejct:** https://github.com/cenciati/predict-taxi-fare

## How to use
### Install cookiecutter
Documentation: https://cookiecutter.readthedocs.io/en/stable/index.html
```bash
$ python3 -m pip install --user cookiecutter
```

### Use this template
Once you run the command below, cookiecutter will download this template and then ask some questions related to project settings, such as `author_name`, `project_name`, `repo_name`, and `license`. You just need to type your preferred configs in the terminal and it will do the rest for you.
```
$ python3 -m cookiecutter https://github.com/cenciati/cookiecutter-mlops
```