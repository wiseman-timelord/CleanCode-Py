REM Script: CleanCode-Ps.Bat

@echo off

:: Initialization
cd /d "%~dp0"
echo.
echo =========================( CleanCode-Ps )=========================
echo.
mode con cols=66 lines=32
color 80
title CleanCode-Ps
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
echo =========================( CleanCode-Ps )=========================
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo                        1. Run CleanCode-Ps,
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
echo =========================( CleanCode-Ps )=========================
echo.
timeout /t 1 /nobreak >nul
echo Maintenenace Started..
if exist ".\Errors-Crash.Log" (
    echo Deleted: Errors-Crash.Log
    del ".\Errors-Crash.Log"
)
echo ..Maintenance Done.
echo.
timeout /t 1 /nobreak >nul
echo Launching Script...
echo.
timeout /t 1 /nobreak >nul
where pwsh >nul 2>&1
if %ERRORLEVEL% equ 0 (
    pwsh.exe -NoProfile -ExecutionPolicy Bypass -File ".\main.ps1" 2>>".\Errors-Crash.Log"
	echo ...Psc Process Exited.
) else (
    powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\main.ps1" 2>>".\Errors-Crash.Log"
	echo ...Ps Process Exited.
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
echo =========================( CleanCode-Ps )=========================
echo.
echo Checking Script Files..
set missing=0
timeout /t 1 /nobreak >nul
if not exist ".\scripts\utility.ps1" set missing=1
if not exist ".\scripts\display.ps1" set missing=1
if not exist ".\main.ps1" set missing=1
if not exist ".\settings.psd1" set missing=1
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