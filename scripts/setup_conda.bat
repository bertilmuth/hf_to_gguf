@echo off

if "%~1"=="" (
    echo Usage: %0 environment_name
    exit /b 1
)

set "ENV_NAME=%~1"

:: Check if the environment exists
conda env list | findstr /c:"%ENV_NAME%" >nul
if %ERRORLEVEL%==0 (
    echo INFO: Environment %ENV_NAME% already exists.
) else (
    echo INFO: Creating new environment: %ENV_NAME%
    :: Create the new environment with Python 3.10 (or any version you need)
    conda create -n %ENV_NAME% python=3.10 -y
)
