# 🎵 Audio Downloader

YouTube, Instagram, X (Twitter), Pinterest, va Threads dan audio yuklab olish uchun web ilovasi.

## ✨ Xususiyatlar

- 🎥 YouTube videolaridan audio yuklash
- 📸 Instagram post va story lardan audio yuklash  
- 🐦 X (Twitter) post laridan audio yuklash
- 📌 Pinterest video laridan audio yuklash
- 🧵 Threads post laridan audio yuklash
- 🎨 Chiroyli va foydalanuvchi do'stona interfeys
- ⚡ Tez va ishonchli yuklash
- 📱 Responsive dizayn

## 🚀 O'rnatish

### Backend o'rnatish

1. Backend papkasiga o'ting:
```bash
cd backend
```

2. Virtual environment yarating:
```bash
python -m venv venv
```

3. Virtual environment ni faollashtiring:
```bash
# Windows uchun:
venv\Scripts\activate

# Linux/Mac uchun:
source venv/bin/activate
```

4. Kerakli paketlarni o'rnating:
```bash
pip install -r requirements.txt
```

5. FFmpeg o'rnating (audio konvertatsiya uchun):
   - Windows: https://ffmpeg.org/download.html
   - Linux: `sudo apt install ffmpeg`
   - Mac: `brew install ffmpeg`

### Frontend o'rnatish

1. Frontend papkasiga o'ting:
```bash
cd frontend
```

2. Kerakli paketlarni o'rnating:
```bash
npm install
```

## 🏃‍♂️ Ishga tushirish

### Backend server ni ishga tushiring:
```bash
cd backend
python app.py
```
Server http://localhost:5000 da ishga tushadi

### Frontend ni ishga tushiring:
```bash
cd frontend
npm start
```
Frontend http://localhost:3000 da ishga tushadi

## 📖 Foydalanish

1. Frontend sahifasini oching (http://localhost:3000)
2. YouTube, Instagram, X, Pinterest yoki Threads linkini kiriting
3. "Yuklab olish" tugmasini bosing
4. Audio fayl avtomatik ravishda yuklanadi

## 🛠️ Texnik ma'lumotlar

### Backend
- **Flask** - Web framework
- **yt-dlp** - Video yuklash kutubxonasi
- **FFmpeg** - Audio konvertatsiya
- **CORS** - Cross-origin requests

### Frontend
- **React** - Frontend framework
- **Modern CSS** - Styling
- **Fetch API** - Backend bilan aloqa

## ⚠️ Muhim eslatmalar

- Faqat shaxsiy foydalanish uchun
- Mualliflik huquqlariga hurmat bering
- Tijorat maqsadlarida foydalanmang
- Server xavfsizligini ta'minlang

## 🐛 Xatoliklarni tuzatish

### Umumiy muammolar:

1. **"FFmpeg not found" xatosi**
   - FFmpeg to'g'ri o'rnatilganligini tekshiring
   - PATH ga qo'shilganligini tekshiring

2. **"Video unavailable" xatosi**
   - Video mavjudligini tekshiring
   - Private video bo'lishi mumkin

3. **CORS xatosi**
   - Backend server ishga tushganligini tekshiring
   - Port 5000 da ishlayotganini tekshiring

4. **Download failed**
   - Internet aloqasini tekshiring
   - URL to'g'ri ekanligini tekshiring

## 📝 Litsenziya

Bu loyiha ochiq manba va shaxsiy foydalanish uchun yaratilgan.

## 🤝 Hissa qo'shish

1. Repository ni fork qiling
2. Yangi branch yarating
3. O'zgarishlarni commit qiling
4. Pull request yuboring

## 📞 Aloqa

Savollar yoki takliflar uchun GitHub da issue oching. 