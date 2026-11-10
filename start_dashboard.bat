@echo off
setlocal
cd /d "%~dp0"

if exist ".venv\Scripts\python.exe" (
    set "PYTHON=.venv\Scripts\python.exe"
) else (
    set "PYTHON=python"
)

echo ========================================================
echo 正在启动数据可视化大屏服务器...
echo ========================================================
echo.
echo 请在浏览器中访问以下地址：
echo http://localhost:8000/
echo.
echo (按 Ctrl+C 可停止服务器)
echo.

"%PYTHON%" -m http.server 8000 --directory dashboard
pause
