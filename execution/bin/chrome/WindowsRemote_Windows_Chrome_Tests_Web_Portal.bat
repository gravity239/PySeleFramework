cd /D %~dp0
cd "../../.."
@echo off
cls

set mth=%date:~4,2%
set dth=%date:~7,2%
set yth=%date:~10,4%
set hh=%time:~0,2%
set mm=%time:~3,2%
set ss=%time:~6,2%

set REPORT_FOLDER=execution/results/Report/Allure_Results
set REPORT_FILE=Broadspot_Automation_Report_%mth%_%dth%_%yth%_%hh%_%mm%_%ss%.html

set STARTUP_TARGET=windows-chrome

set RUN_CONFIG=execution/config/sample_test_config.cfg

set TESTCASES_FOLDER=broadspot/testcases


py.test --alluredir="%REPORT_FOLDER%" --tb=short --startup-run-config="%STARTUP_TARGET%" --udids=%UDID% --hub-url="%HUB_URL%" --appium-url="%APPIUM_URL%" --optional-run-config="%SECOND_TARGET%" --config-file="%RUN_CONFIG%" --ignore="%IGNORE_FOLDER_1%" --ignore="%IGNORE_FOLDER_2%" %TESTCASES_FOLDER%
--alluredir="execution/results/Report/Allure_Results" --testrail --tr-config="execution/config/testrail_config.cfg" --tb=short --startup-run-config="windows-chrome" --config-file="execution/config/sample_test_config.cfg"
pause