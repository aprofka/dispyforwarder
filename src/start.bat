@echo off
title Dispy Forwarder Runner

:loop
python bot.py
echo.
echo Bot script has exited.
set /p choice=Press Enter to restart the script or close the window...
if "%choice%"=="" goto loop