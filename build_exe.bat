@echo off
echo ========================================
echo    PaintShop - Creation de l'executable
echo ========================================
echo.

REM Verifier si Python est installe
python --version >nul 2>&1
if errorlevel 1 (
    echo ERREUR: Python n'est pas installe ou n'est pas dans le PATH
    pause
    exit /b 1
)

echo ✅ Python trouve
echo.

REM Installer les dependances
echo 📦 Installation des dependances...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERREUR: Impossible d'installer les dependances
    pause
    exit /b 1
)

echo ✅ Dependances installees
echo.

REM Lancer le script de creation de l'executable
echo 🚀 Creation de l'executable...
python build_exe.py
if errorlevel 1 (
    echo ERREUR: Impossible de creer l'executable
    pause
    exit /b 1
)

echo.
echo ========================================
echo    ✅ EXECUTABLE CREE AVEC SUCCES!
echo ========================================
echo.
echo 📁 L'executable se trouve dans le dossier: dist/
echo 🎯 Nom du fichier: PaintShop.exe
echo.
echo 📋 Instructions d'utilisation:
echo 1. Allez dans le dossier 'dist'
echo 2. Double-cliquez sur PaintShop.exe
echo 3. Ou ouvrez un terminal et tapez: PaintShop.exe runserver
echo 4. Ouvrez votre navigateur sur: http://127.0.0.1:8000
echo.
pause 