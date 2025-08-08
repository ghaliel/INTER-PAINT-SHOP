@echo off
echo ========================================
echo    PaintShop - Lancement Simple
echo ========================================
echo.
echo Demarrage de l'application Django...
echo.
echo Instructions:
echo 1. Attendez que le serveur demarre
echo 2. Ouvrez votre navigateur sur: http://127.0.0.1:8000
echo 3. Appuyez sur Ctrl+C pour arreter
echo.
echo ========================================
echo.

REM Activer l'environnement virtuel si il existe
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
    echo Environnement virtuel active
) else (
    echo Environnement virtuel non trouve, utilisation de Python system
)

REM Lancer l'application Django
python manage.py runserver 127.0.0.1:8000

pause
