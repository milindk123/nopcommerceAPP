
@echo off
:: Step 1: Navigate to the project folder
cd /d %~dp0

:: Step 2: Activate the virtual environment
call .venv\Scripts\activate

:: Step 3: Run your specific pytest command
pytest -v -s -m "sanity" --html=./Reports/report.html --browser chrome testCases/

pytest -v -s -m "sanity" --html=./Reports/report.html --browser firefox testCases/



REM pytest -v -s -m "sanity and regression" --html=./Reports/report.html testCases/ --browser chrome
REM pytest -v -s -m "sanity or regression" --html=./Reports/report.html testCases/ --browser chrome
REM pytest -v -s -m "regression" --html=./Reports/report.html testCases/ --browser chrome

pause


