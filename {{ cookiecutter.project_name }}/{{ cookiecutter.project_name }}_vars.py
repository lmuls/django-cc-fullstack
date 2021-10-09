import os

from {{cookiecutter.project_name}}.settings import BASE_DIR

proj_vars = {
    "USE_DB": "{{ cookiecutter.USE_DB }}",
    'DATABASE_URL': "{{ cookiecutter.DATABASE_URL }}",
    'SECRET_KEY': "{{ cookiecutter.SECRET_KEY }}",
    'STATE': '{{ cookiecutter.STATE }}',
    "USE_S3": '{{ cookiecutter.USE_S3 }}',
}

proj_paths = [BASE_DIR]

def set_local():
    counter = 0
    with open(os.path.join(BASE_DIR, "{{cookiecutter.project_name}}env\Lib\site-packages\_set_envs.pth"), "w") as f:
        f.write("import os; ")
        for k,v in proj_vars.items():
            if "/" or "\ " in v:
                f.write("os.environ['" + k + "']=" + "r'" + v + "';" )
            else:
                f.write("os.environ['" + k + "']=" + "'" + v + "';" )
            
    with open(os.path.join(BASE_DIR, "{{cookiecutter.project_name}}env\Lib\site-packages\_set_path.pth"), "w") as f:
        f.write("import sys;") 
        for path in proj_paths:
            f.write("sys.path.insert(" + str(counter) + "," + "r'" + path + "');" )


def set_heroku():
    pass

set_local()