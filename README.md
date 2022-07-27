# rentomatic
Clean architecture in python, following https://www.thedigitalcatbooks.com/index.html

## Development
### Run flask server
1. Activate venv
2. run server
   1. ```$Env:FLASK_ENV = "development" flask run```

### MyPy
- install pycharm plugin
- pip install mypy
- Add to mypy-plugin-configuration arguments:
   - ```--explicit-package-bases```
   - ```--namespace-packages```

# history
[24/07/2022] Continue chapter 5, "Integrating external systems"