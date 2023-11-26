# ChatBot

## How to setup development environment

1. Use PyEnv to make sure you're using Python 3.11.5 in the repo root 
2. Use Python 3's built-in virtual environment feature, called `venv`, to create an isolated virtual environment: 
```
python -m venv han 
source myenv/bin/activate
```
3. Pip install all the dependencies for this project:
pip install -r requirements.txt
```

## Adding dependencies

If you have to add a dependency to the project, use pip to isntall it:

```
pip install [the new dependency]
```

And record the dependency so that others will be able to easily install in on their local machines:

```
pip freeze >> requirements.txt
```

