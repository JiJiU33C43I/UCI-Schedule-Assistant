set current_path=%cd% 
echo The Current Directory is %cd%
call %cd%\venv\Scripts\activate.bat
cd %cd%\src\gui_src\
main_gui.py