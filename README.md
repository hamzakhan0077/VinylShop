MUST HAVE VIRTUAL Environment(venv) TO RUN THE DEVELOPER SERVER 
create the venv in the root directory of the project

then u install requirements.txt once you are in the virtual environmnet 

Steps to run the app.(Windows) -  for linux it is almost same just running the venv command is : source (venv Name)/test/bin/activate

1. Download the project file as zip
2. Un zip it
3. open terminal in your ide or local machine it is up to you 
4. create a virtual environment using - command: python -m venv (Whatever you want to name the environment)
5. cd into <environmnet directory>/Scripts
6. Type:  activate.bat
7. Your virtual environment is now active you will see some thing like
  
  (yourEnvironment Name)C:\Users\hassa\PycharmProjects\Test\VinylShop-main>
8. Now you will install the requirements (while being in venv)
  run command:  pip install -r requirements.txt
9. navigate to the root directory of the project 
  run command:  python run.py
  
  
10. This will run the developer server and you will have something like this click on the IP address you will on the main page of the project


(vinylvenv) C:\Users\hassa\PycharmProjects\Test\VinylShop-main>python run.py
C:\Users\hassa\PycharmProjects\Test\VinylShop-main\vinylvenv\lib\site-packages\flask_sqlalchemy\__init__.py:8
72: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by d
efault in the future.  Set it to True or False to suppress this warning.
  warnings.warn(FSADeprecationWarning(
run.py
 * Serving Flask app 'VinylShop' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
C:\Users\hassa\PycharmProjects\Test\VinylShop-main\vinylvenv\lib\site-packages\flask_sqlalchemy\__init__.py:8
72: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by d
efault in the future.  Set it to True or False to suppress this warning.
  warnings.warn(FSADeprecationWarning(
run.py
 * Debugger is active!
 * Debugger PIN: 165-302-754
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

