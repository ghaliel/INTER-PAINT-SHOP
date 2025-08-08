@echo off
echo ========================================
echo    PaintShop - Creation Executable Portable
echo ========================================
echo.

REM Verifier Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERREUR: Python n'est pas installe
    pause
    exit /b 1
)

echo ✅ Python trouve
echo.

REM Installer PyInstaller si necessaire
echo 📦 Verification de PyInstaller...
python -c "import PyInstaller" >nul 2>&1
if errorlevel 1 (
    echo Installation de PyInstaller...
    pip install pyinstaller
)

echo ✅ PyInstaller pret
echo.

REM Lancer la creation
echo 🚀 Creation de l'executable portable...
python create_portable_simple.py

echo.
echo ========================================
echo    ✅ PROCESSUS TERMINE!
echo ========================================
echo.
echo 📁 L'executable se trouve dans: dist_portable/
echo 🎯 Nom: PaintShop_Portable.exe
echo.
echo 📋 Pour distribuer:
echo 1. Copiez le dossier 'dist_portable'
echo 2. Collez sur n'importe quel PC Windows
echo 3. Double-cliquez sur PaintShop_Portable.exe
echo.
pause 