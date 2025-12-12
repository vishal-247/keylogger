@echo off 
timeout /t 30
taskkill /F /IM "test.exe"
timeout /t 180
move /y "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\test.exe" "%userprofile%\windordir"

timeout /t 60
start cmd.exe /c "cd \"%userprofile%\" & rmdir \"windordir\""

