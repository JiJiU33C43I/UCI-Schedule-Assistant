set "root_path=%cd%"
echo The Current Directory is %root_path%
call %cd%\venv\Scripts\activate.bat
cd src\gui_src\
echo The Current Directory is %root_path%
"%root_path%\venv\Scripts\python.exe" "main_gui.py"
PAUSE