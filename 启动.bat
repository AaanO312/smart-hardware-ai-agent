@echo off
cd /d "%~dp0"
docker compose up -d
echo.
echo 启动完成！
echo Streamlit: http://localhost:8501
echo API文档:   http://localhost:8000/docs
pause
