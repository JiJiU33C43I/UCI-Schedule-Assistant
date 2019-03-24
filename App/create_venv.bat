rd /S /Q %cd%\venv
echo ... && echo ... && echo ... && echo ... && echo Trying to setup the Virtual Env for this project, it might take several minutes......
python -m venv %cd%\venv
call %cd%\venv\Scripts\activate.bat
pip install -r requirements.txt
PAUSE