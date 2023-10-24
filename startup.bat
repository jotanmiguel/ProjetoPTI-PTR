@echo off
py -m venv VirtualEnv
call VirtualEnv\Scripts\activate.bat
cd .\Django\
py manage.py runserver
