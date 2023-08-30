@echo off
mode 76, 30


:: Get the current directory
set "CurrentDir=%~dp0"

:: Check for admin rights
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Running with admin rights
) else (
    echo Running without admin rights, relaunching with admin rights...
    PowerShell -Command "Start-Process -FilePath '%0' -WorkingDirectory '%CurrentDir%' -Verb RunAs"
    exit /b
)
Echo.
Echo.


:: Change to the directory of the batch file
cd /d "%CurrentDir%"
Echo.
echo.


:: Run the scriptclean.py script
echo Launching ScriptClean...
echo.
@echo 
wsl python3 scriptclean.py
@echo off
echo.

:: Exiting
echo Llama2Robot shutting down...
echo.
pause
exit /b
