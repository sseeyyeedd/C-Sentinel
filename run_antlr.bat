@echo off
set ANTLR_JAR="C:\Program Files\Antlr\antlr-4.13.1-complete.jar"

if "%1"=="" (
    echo Please provide a .g4 file name.
    echo Example: run_antlr.bat Arithmetic.g4
    pause
    exit /b
)

if not exist "%1" (
    echo File %1 not found.
    pause
    exit /b
)

java -Xmx500M -cp %ANTLR_JAR% org.antlr.v4.Tool -Dlanguage=Python3 -visitor -listener -o gen %1

echo ---------------------------------------
echo Files generated successfully.
echo Output folder: gen\