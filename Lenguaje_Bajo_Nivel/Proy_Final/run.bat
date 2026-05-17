@echo off

if exist tasm.exe goto compilar
echo [!] TASM no encontrado. Configurando el entorno...
PATH=%PATH%;C:/TASM/BIN/


:compilar
tasm %1.asm 
if errorlevel 1 goto error_tasm

tlink %1.obj
if errorlevel 1 goto error_tlink

if exist %1.exe goto ejecutar
echo [X] Error: El archivo ejecutable no se ha generado.
goto fin

:ejecutar
echo ----------------------------------
echo %1.exe Listo para ejecutar
echo ----------------------------------
goto fin

:error_tasm
echo [X] Error al compilar con TASM.
goto fin

:error_tlink
echo [X] Error al enlazar con TLINK.
goto fin

:fin