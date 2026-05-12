@echo off
echo [!] Todos los ejecutables y binarios (exe, obj y map) seran eliminados.

choice /C SN /M "¿Estas seguro de que deseas eliminarlos? (S/N)"

if errorlevel 2 goto cancelar
if errorlevel 1 goto limpiar

:limpiar
echo [!] Limpiando archivos anteriores...
del *.exe >nul 2>&1
del *.obj >nul 2>&1
del *.map >nul 2>&1
echo [!] Archivos anteriores eliminados.
goto fin

:cancelar
echo [X] Operacion cancelada por el usuario.
goto fin

:fin