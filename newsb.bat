@echo off 

taskkill /F /IM "winget_validator.exe"
timeout /t 1

del "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\winget_validator.exe" 
 

