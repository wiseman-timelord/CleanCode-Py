@echo off

:: Get the current directory
set "CurrentDir=%~dp0"

:: Check for admin rights
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Running with Admin...
) else (
    echo Enabling Admin mode...
    PowerShell -Command "Start-Process -FilePath '%0' -WorkingDirectory '%CurrentDir%' -Verb RunAs"
    exit /b
)

:: Change to the directory of the batch file
cd /d "%CurrentDir%"
echo.

:: Run the scriptclean.py script
echo Launching Python script...
@echo on
wsl python3 main.py
@echo off

:: Exiting
echo.
echo Program exited, press any key to continue...
pause >nul
