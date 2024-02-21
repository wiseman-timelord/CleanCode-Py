REM Script: CleanCode-Py.Bat

@echo off

:: Initialization
cd /d "%~dp0"
echo.
echo =========================( CleanCode-Py )=========================
echo.
mode con cols=66 lines=32
color 80
title CleanCode-Py
timeout /t 1 /nobreak >nul
echo Launcher Initialized...
echo.
timeout /t 2 /nobreak >nul

:: Main Menu
:menu
cls
echo            ^_^_^_^_ ^_                   ^_^_^_^_          ^_      
echo           ^/ ^_^_^_^| ^| ^_^_^_  ^_^_^_^_ ^_^_^_^_  ^/ ^_^_^_^|^_^_^_   ^_^_^| ^| ^_^_^_ 
echo          ^| ^|   ^| ^|^/ ^_ ^\^/ ^_  ^|  ^_ ^\^| ^|   ^/ ^_ ^\ ^/ ^_  ^|^/ ^_ ^\
echo          ^| ^|^_^_^_^| ^|  ^_^_^/ ^<^_^| ^| ^| ^| ^| ^|^_^_^| ^<^_^> ^| ^<^_^| ^|  ^_^_^/
echo           ^\^_^_^_ ^|^_^|^\^_^_^_^|^\^_^_^_^_^|^_^| ^|^_^|^\^_^_^_^_^\^_^_^_^/ ^\^_^_^_^_^|^\^_^_^_^|
echo.
echo =========================( CleanCode-Py )=========================
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo                        1. Run CleanCode-Py,
echo.
echo                        2. Check Integrity,
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo ------------------------------------------------------------------

:: Variables
set /p choice=Select; Options=1-2, Exit=X: 
if "%choice%"=="1" goto executeMain
if "%choice%"=="2" goto checkScript
if "%choice%"=="x" goto end
echo Invalid choice. Try again.
timeout /t 2 /nobreak >nul
goto menu

:: Execute main.py
:executeMain
cls
echo.
echo =========================( CleanCode-Py )=========================
echo.
timeout /t 1 /nobreak >nul
echo Maintenance Started..
if exist ".\Errors-Crash.Log" (
    echo Deleted: Errors-Crash.Log
    del ".\Errors-Crash.Log"
)
echo ..Maintenance Done.
echo.
timeout /t 1 /nobreak >nul

:: Attempt to use python command directly as python3 might not be recognized on Windows
echo Attempting to run script using Python...
python main.py 2> Errors-Crash.Log
if %ERRORLEVEL% equ 0 (
    echo Script ran successfully with Python.
) else (
    echo Failed to run script. Checking for Python installation...
    where python >nul 2>&1
    if %ERRORLEVEL% equ 0 (
        echo Python installation found. Please check the script for errors.
    ) else (
        echo Python not found. Ensure Python is installed and in your PATH.
        exit /b 1
    )
)
echo.
color 80
echo Returning to menu..
timeout /t 2 /nobreak >nul
goto menu

:: Check File Structure
:checkScript
cls
echo.
echo =========================( CleanCode-Py )=========================
echo.
echo Checking Script Files..
set missing=0
timeout /t 1 /nobreak >nul
if not exist ".\scripts\utility.py" set missing=1
if not exist ".\scripts\display.py" set missing=1
if not exist ".\main.py" set missing=1
if %missing%==1 (
    echo ..Failure, Re-Install Program!
) else (
    echo ..Program Files Correct.
)
echo.
timeout /t 1 /nobreak >nul
echo Returning to menu..
echo.
timeout /t 2 /nobreak >nul
goto menu

:: End Function
:end
echo ...Exit Process Initiated.
timeout /t 2 /nobreak >nul