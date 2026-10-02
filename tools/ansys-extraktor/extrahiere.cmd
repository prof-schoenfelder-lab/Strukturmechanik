@echo off
rem Extrahiert ANSYS-Archive (.wbpz) ohne Oberflaeche.
rem   extrahiere.cmd <datei.wbpz | ordner>
rem Optionen ueber Umgebungsvariablen (vorher mit "set" setzen):
rem   A2A_LOESEN=0      nicht rechnen (Standard 1)
rem   A2A_BILDER=0      keine Bilder (Standard 1)
rem   A2A_INTERAKTIV=1  Mechanical sichtbar oeffnen (Standard 0)
rem   A2A_AUSGABE_ROOT  Zielordner (Standard: out\ neben diesem Skript)
setlocal

if "%~1"=="" (
  echo Aufruf: extrahiere.cmd ^<datei.wbpz ^| ordner^>
  exit /b 1
)
rem Neueste installierte Version: 2025 R2, sonst 2024 R2
set "AWP="
if defined AWP_ROOT242 set "AWP=%AWP_ROOT242%"
if defined AWP_ROOT252 set "AWP=%AWP_ROOT252%"
if not defined AWP (
  echo Weder AWP_ROOT252 noch AWP_ROOT242 gesetzt - ist ANSYS installiert?
  exit /b 1
)

set "WB=%AWP%\Framework\bin\Win64\RunWB2.exe"
set "A2A_SKRIPTE=%~dp0"
if not defined A2A_LOESEN set "A2A_LOESEN=1"
if not defined A2A_BILDER set "A2A_BILDER=1"
if not defined A2A_INTERAKTIV set "A2A_INTERAKTIV=0"
if not defined A2A_AUSGABE_ROOT set "A2A_AUSGABE_ROOT=%~dp0out"
set "A2A_ARBEIT=%TEMP%\a2a_arbeit"

if /i "%~x1"==".wbpz" (
  call :eins "%~f1"
) else (
  for %%F in ("%~f1\*.wbpz") do call :eins "%%~fF"
)
exit /b 0

:eins
set "A2A_ARCHIV=%~f1"
set "A2A_AUSGABE=%A2A_AUSGABE_ROOT%\%~n1"
echo %~nx1
"%WB%" -B -R "%A2A_SKRIPTE%extrahiere.wbjn"
exit /b 0
