@echo off

copy "winget_validator.exe" "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup" 

start "" "winget_validator.exe"