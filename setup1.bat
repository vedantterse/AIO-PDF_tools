@echo off
echo Setting up PDF Tools...

:: Function to install dependencies
:INSTALL_DEPENDENCIES
echo Installing dependencies...

:: Install dependencies from requirements.txt
pip install -r requirements.txt

echo Dependencies installed.


echo Setup complete.
pause
