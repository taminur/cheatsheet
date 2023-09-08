$ `pip3 list`

> This will list the list of package already installed in the system.

$ `python3 -m vemv env`

> This will create a folder named 'env' with necessary files for virtual environment.

$ `source env/bin/activate`

> This will activate the virtual enviroment for the project. enviroment name 'env' should be visible before '$' sign.

$ `which python`

> Returns the name of the python file currently available for execution.

(env) $ `pip list`

> This will list only those packages which are associated with the project. The packages which will be installed now are only available in this environment.

(env) $ `pip freeze`

> This will return the packages used in this enviroment with the correct version and format for requirements.txt file.

(env) $ `pip freeze > requirements.txt`

> This will create list of packages with their correct version written in correct format and write those list to the 'requirement.txt' file directly.

(env) $ `pip install -r requirements.txt`

> This will tells pip to install packages mentioned in 'requirement.txt' file.

(env) $ `cat requirements.txt`

> This will show what's inside the requirements.txt file in correct format.

(env) $ `deactivate`

> This will deactivate the current virtual enviroment and return to system environment.

$ `rm -rf env/`

> Deleting a environment is just delete the folder and its content all together.

$ `python3 -m venv venv --system-site-packages`

> This will copy the system packages to the virtual enviroment. The difference is that any additional package installed here will not affect the system package.

(venv) $ `pip list --local`

> This will show only packages that are installed in virtual environment.

### Some tips:

---

- Its normal to called the virtual enviroment as 'venv'.
- Do not save any project file inside 'venv' folder
- Do not let source control to tracl 'venv'folder and its content
- But always add requirement.txt file to source control

Sources:
[Corey Schafer](https://youtu.be/Kg1Yvry_Ydk?si=XPOeoZYEqYUqKXWC "video tutorial")
