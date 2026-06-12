@echo off
cd /d "%~dp0"
docker compose down
echo.
echo 已停止
pause
