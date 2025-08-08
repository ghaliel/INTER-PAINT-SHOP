@echo off
echo ========================================
echo    PaintShop - Demarrage Application
echo ========================================
echo.
echo Demarrage de l'application portable...
echo.
echo Instructions:
echo 1. Attendez que le serveur demarre
echo 2. Ouvrez votre navigateur sur: http://127.0.0.1:8000
echo 3. Appuyez sur Ctrl+C pour arreter
echo.
echo ========================================
echo.

if exist "dist_portable\PaintShop_Portable.exe" (
    cd dist_portable
    PaintShop_Portable.exe runserver 127.0.0.1:8000
) else (
    echo ERREUR: PaintShop_Portable.exe non trouve dans dist_portable\
    echo Verifiez que l'executable a ete cree correctement.
    pause
)
