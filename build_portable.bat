@echo off
echo ========================================
echo    PaintShop - Creation Executable Portable
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

REM Lancer le script de creation de l'executable portable
echo 🚀 Creation de l'executable portable...
python build_portable_exe.py
if errorlevel 1 (
    echo ERREUR: Impossible de creer l'executable portable
    pause
    exit /b 1
)

echo.
echo ========================================
echo    ✅ EXECUTABLE PORTABLE CREE!
echo ========================================
echo.
echo 📁 L'executable portable se trouve dans: dist_portable/
echo 🎯 Nom du fichier: PaintShop_Portable.exe
echo.
echo 📋 Instructions de distribution:
echo 1. Copiez tout le contenu du dossier 'dist_portable'
echo 2. Collez-le sur n'importe quel PC Windows
echo 3. Double-cliquez sur PaintShop_Portable.exe
echo 4. L'application fonctionnera immediatement!
echo.
echo 🎉 Votre application est maintenant portable!
echo.
pause 