@echo off
setlocal
cd /d "%~dp0"

if exist ".venv\Scripts\python.exe" (
    set "PYTHON=.venv\Scripts\python.exe"
) else (
    set "PYTHON=python"
)

echo ========================================================
echo 正在更新数据分析...
echo ========================================================

echo 1. 正在执行数据对比分析 (Excel)...
"%PYTHON%" analyze_data_full.py
if errorlevel 1 goto :error

echo 2. 正在导出大屏数据 (JSON)...
"%PYTHON%" export_data_to_json.py
if errorlevel 1 goto :error

echo.
echo ========================================================
echo 数据更新完成！请刷新大屏页面查看最新结果。
echo ========================================================
pause
exit /b 0

:error
echo.
echo ========================================================
echo 数据更新失败，请检查上方的错误信息。
echo ========================================================
pause
exit /b 1
