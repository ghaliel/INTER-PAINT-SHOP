@echo off
echo ========================================
echo    PaintShop - Verification des prerequis
echo ========================================
echo.

REM Verifier si Python est disponible pour le script de verification
python --version >nul 2>&1
if errorlevel 1 (
    echo ⚠️  Python non trouve - Verification manuelle...
    goto verification_manuelle
)

REM Installer psutil si necessaire
echo 📦 Verification des dependances...
python -c "import psutil" >nul 2>&1
if errorlevel 1 (
    echo Installation de psutil...
    pip install psutil
)

REM Lancer la verification automatique
echo 🔍 Lancement de la verification automatique...
python verifier_prerequis.py
goto fin

:verification_manuelle
echo.
echo 🔍 VERIFICATION MANUELLE DES PREREQUIS
echo ========================================
echo.

REM Verifier Windows
echo 🖥️  Systeme d'exploitation:
ver | findstr "Version"
echo.

REM Verifier la RAM
echo 💾 Memoire RAM:
wmic computersystem get TotalPhysicalMemory | findstr /v "^$"
echo.

REM Verifier l'espace disque
echo 💿 Espace disque:
wmic logicaldisk get size,freespace,caption
echo.

REM Verifier les fichiers
echo 📁 Fichiers requis:
if exist "PaintShop_Portable.exe" (
    echo ✅ PaintShop_Portable.exe
) else (
    echo ❌ PaintShop_Portable.exe - MANQUANT
)

if exist "Lancer_PaintShop.bat" (
    echo ✅ Lancer_PaintShop.bat
) else (
    echo ❌ Lancer_PaintShop.bat - MANQUANT
)

if exist "README.txt" (
    echo ✅ README.txt
) else (
    echo ❌ README.txt - MANQUANT
)

if exist "db.sqlite3" (
    echo ✅ db.sqlite3
) else (
    echo ❌ db.sqlite3 - MANQUANT
)

echo.
echo 📁 Dossiers optionnels:
if exist "static" (
    echo ✅ static/
) else (
    echo ⚠️  static/ - Optionnel
)

if exist "media" (
    echo ✅ media/
) else (
    echo ⚠️  media/ - Optionnel
)

echo.
echo 🌐 Verification du port 8000:
netstat -an | findstr ":8000"
if errorlevel 1 (
    echo ✅ Port 8000 disponible
) else (
    echo ⚠️  Port 8000 deja utilise
    echo 💡 Utilisez un autre port (ex: 8080)
)

echo.
echo ========================================
echo 📊 RESUME
echo ========================================
echo.
echo ✅ Si tous les fichiers sont presents:
echo 💡 Double-cliquez sur PaintShop_Portable.exe
echo 🌐 Ouvrez http://127.0.0.1:8000 dans votre navigateur
echo.
echo ❌ Si des fichiers sont manquants:
echo 🔧 Recopiez le dossier dist_portable complet
echo.

:fin
echo.
echo ========================================
echo    ✅ VERIFICATION TERMINEE
echo ========================================
echo.
pause 