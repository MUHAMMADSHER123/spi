#!/usr/bin/env python3
"""
Audio Downloader Startup Script
Bu script backend va frontend ni oson ishga tushirish uchun yaratilgan
"""

import os
import sys
import subprocess
import time
import webbrowser
from pathlib import Path

def check_python():
    """Python versiyasini tekshirish"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 yoki undan yuqori versiya kerak")
        sys.exit(1)
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} topildi")

def check_ffmpeg():
    """FFmpeg mavjudligini tekshirish"""
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        print("✅ FFmpeg topildi")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ FFmpeg topilmadi")
        print("📥 FFmpeg o'rnatish kerak:")
        print("   Windows: https://ffmpeg.org/download.html")
        print("   Linux: sudo apt install ffmpeg")
        print("   Mac: brew install ffmpeg")
        return False

def setup_backend():
    """Backend ni sozlash"""
    backend_dir = Path("backend")
    if not backend_dir.exists():
        print("❌ Backend papkasi topilmadi")
        return False
    
    os.chdir(backend_dir)
    
    # Virtual environment yaratish
    venv_dir = Path("venv")
    if not venv_dir.exists():
        print("📦 Virtual environment yaratilmoqda...")
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
    
    # Virtual environment ni faollashtirish
    if os.name == 'nt':  # Windows
        activate_script = venv_dir / "Scripts" / "activate.bat"
        pip_path = venv_dir / "Scripts" / "pip.exe"
    else:  # Linux/Mac
        activate_script = venv_dir / "bin" / "activate"
        pip_path = venv_dir / "bin" / "pip"
    
    # Paketlarni o'rnatish
    print("📦 Kerakli paketlar o'rnatilmoqda...")
    subprocess.run([str(pip_path), "install", "-r", "requirements.txt"], check=True)
    
    print("✅ Backend sozlandi")
    return True

def start_backend():
    """Backend server ni ishga tushirish"""
    backend_dir = Path("backend")
    os.chdir(backend_dir)
    
    if os.name == 'nt':  # Windows
        python_path = Path("venv/Scripts/python.exe")
    else:  # Linux/Mac
        python_path = Path("venv/bin/python")
    
    print("🚀 Backend server ishga tushirilmoqda...")
    try:
        subprocess.Popen([str(python_path), "app.py"])
        time.sleep(3)  # Server ishga tushish uchun kutish
        print("✅ Backend server http://localhost:5000 da ishga tushdi")
        return True
    except Exception as e:
        print(f"❌ Backend server ishga tushirishda xatolik: {e}")
        return False

def start_frontend():
    """Frontend ni ishga tushirish"""
    frontend_dir = Path("frontend")
    if not frontend_dir.exists():
        print("❌ Frontend papkasi topilmadi")
        return False
    
    os.chdir(frontend_dir)
    
    # Node modules o'rnatish
    if not Path("node_modules").exists():
        print("📦 Node.js paketlari o'rnatilmoqda...")
        subprocess.run(["npm", "install"], check=True)
    
    print("🚀 Frontend ishga tushirilmoqda...")
    try:
        subprocess.Popen(["npm", "start"])
        time.sleep(5)  # Frontend ishga tushish uchun kutish
        print("✅ Frontend http://localhost:3000 da ishga tushdi")
        return True
    except Exception as e:
        print(f"❌ Frontend ishga tushirishda xatolik: {e}")
        return False

def open_browser():
    """Brauzerda sahifani ochish"""
    print("🌐 Brauzerda sahifa ochilmoqda...")
    webbrowser.open("http://localhost:3000")

def main():
    """Asosiy funksiya"""
    print("🎵 Audio Downloader - Ishga tushirish")
    print("=" * 50)
    
    # Python versiyasini tekshirish
    check_python()
    
    # FFmpeg ni tekshirish
    if not check_ffmpeg():
        print("\n⚠️ FFmpeg o'rnatilmagan bo'lsa ham davom etish mumkin, lekin ba'zi funksiyalar ishlamasligi mumkin")
    
    # Backend ni sozlash
    if not setup_backend():
        print("❌ Backend sozlashda xatolik")
        return
    
    # Backend ni ishga tushirish
    if not start_backend():
        print("❌ Backend ishga tushirishda xatolik")
        return
    
    # Frontend ni ishga tushirish
    if not start_frontend():
        print("❌ Frontend ishga tushirishda xatolik")
        return
    
    # Brauzerda ochish
    open_browser()
    
    print("\n🎉 Ilova muvaffaqiyatli ishga tushdi!")
    print("📝 Foydalanish:")
    print("   - Frontend: http://localhost:3000")
    print("   - Backend: http://localhost:5000")
    print("\n🛑 Ilovani to'xtatish uchun Ctrl+C bosing")
    
    try:
        # Ilovani ishlab turish
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Ilova to'xtatildi")

if __name__ == "__main__":
    main() 