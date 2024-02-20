:: Script: BatPy-Launch.Bat
@echo off
setlocal

:: Global Variables
set "Sys_Ver="
set "Pyth_Ver="
set "Work_Dir=%~dp0"
set "Work_Dir=%Work_Dir:~0,-1%"
set "AdminMethod=1"  :: Default to method 1 (VBScript)

:: System Info
echo Getting System Info:
for /f "delims=" %%i in ('ver') do set "Sys_Ver=%%i"
echo System Version: %Sys_Ver%
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set "Pyth_Ver=%%i"
echo Python Version: %Pyth_Ver%
timeout /t 5 /nobreak >nul

:: Determine Windows version and set admin method accordingly
echo %Sys_Ver% | findstr /C:"Version 6.1" >nul || echo %Sys_Ver% | findstr /C:"Version 6.3" >nul && set "AdminMethod=1"  :: Windows 7/8.1
echo %Sys_Ver% | findstr /C:"Version 10." >nul || echo %Sys_Ver% | findstr /C:"Version 11." >nul && set "AdminMethod=2"  :: Windows 10/11

:: Get Admin
if "%~1"=="admin" goto :AdminConfirmed
echo.
echo Getting Admin Rights:
echo Working Dir is %Work_Dir%
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Moved To System.
    echo Success Gaining Admin.
    goto :AdminConfirmed
)

:: Apply admin method based on Windows version
echo Enabling Admin mode...
if "%AdminMethod%"=="1" (
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    echo UAC.ShellExecute "%~s0", "admin", "", "runas", 1 >> "%temp%\getadmin.vbs"
    cscript "%temp%\getadmin.vbs" /nologo
    del "%temp%\getadmin.vbs" /q
) else (
    PowerShell -Command "Start-Process -FilePath '%0' -ArgumentList 'admin' -WorkingDirectory '%Work_Dir%' -Verb RunAs"
)
exit /b

:: Preparation
:AdminConfirmed
echo.
echo Script Preparations:
cd /d "%Work_Dir%"
echo Moved to Script Location.
echo Checking Window Status:
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Admin Rights Success.
) else (
    echo Admin Rights Failure.
)
echo Current Directory:
cd
timeout /t 5 /nobreak >nul

:: Command Run Script
:RunScript
echo Launching Python script...
@echo on
if "%Pyth_Ver:~0,1%"=="3" (
    python.exe main.py
    echo Script Execution Successful.
) else (
    echo Unsupported Python version. Please use Python 3.
    echo Script Execution Failed.
    exit /b
)
@echo off

:: Exiting
echo.
echo Program exited.
echo Press any key to continue...
pause >nul
endlocal
