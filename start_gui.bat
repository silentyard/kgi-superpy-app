@echo off
echo 正在啟動 KGI Securities Trading Application GUI...
echo.

REM 切換到應用程式目錄
cd /d "%~dp0"

REM 啟動 GUI 版本
"C:/Users/ching/AppData/Local/Programs/Python/Python312/python.exe" gui_main.py

echo.
echo 應用程式已結束
pause
