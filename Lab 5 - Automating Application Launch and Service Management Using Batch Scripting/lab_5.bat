@echo off
echo ============================
echo Starting Lab Automation...
echo ============================

:: --- 1. Launch Applications ---
echo Launching Google Chrome...
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe"

echo Launching Visual Studio Code...
start "" "C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe"

echo Launching SQL Server Management Studio...
start "" "C:\Program Files\Microsoft SQL Server Management Studio 21\Release\Common7\IDE\SSMS.exe"

:: --- 2. MSSQL Service Check ---
echo Checking SQL Server (MSSQLSERVER) status...
sc query MSSQLSERVER | findstr /I "RUNNING"
IF %ERRORLEVEL% EQU 0 (
    echo MSSQLSERVER is already running.
) ELSE (
    echo MSSQLSERVER is not running. Starting the service...
    net start MSSQLSERVER
    IF %ERRORLEVEL% EQU 0 (
        echo Service started successfully.
    ) ELSE (
        echo Failed to start the MSSQLSERVER service.
    )
)


:: --- 3. Open Python Lab Files ---
echo Opening Python Lab Files...

SET "LAB2_PATH=D:\Aarchi_022bim003\Lab_2.py"
SET "LAB3_PATH=D:\Aarchi_022bim003\Lab_3.py"

IF EXIST "%LAB2_PATH%" (
    start "" "%LAB2_PATH%"
) ELSE (
    echo Lab 2 file not found: %LAB2_PATH%
)

IF EXIST "%LAB3_PATH%" (
    start "" "%LAB3_PATH%"
) ELSE (
    echo Lab 3 file not found: %LAB3_PATH%
)

echo ============================
echo Automation Script Finished.
echo ============================
pause
