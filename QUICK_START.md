# ⚡ Quick Start Guide

## 🚀 Menjalankan Aplikasi

### Cara Termudah (SQLite - Default)

```bash
# 1. Pastikan di folder project
cd /home/aesbe/latihan-projek

# 2. Jalankan server
python3 manage.py runserver
```

**✅ Selesai!** Aplikasi sudah berjalan di: **http://localhost:8000**

---

## 🎨 Tema Baru: Kuning-Putih ☀️

Aplikasi sekarang menggunakan tema **kuning-putih** yang cerah dan modern!

**Warna Utama:**
- 🟡 Kuning Emas (#eab308)
- ⚪ Putih Bersih (#ffffff)
- 🟡 Krem Lembut (#fefce8)

**Fitur Visual:**
- ✨ Background putih bersih
- 🟡 Tombol kuning cerah
- 🎯 Hover effects kuning
- 📱 Responsive di semua device

---

## 🗄️ Database Setup (Optional)

### Default: SQLite
Tidak perlu setup! Database SQLite sudah siap digunakan.

### Production: PostgreSQL

Jika ingin menggunakan PostgreSQL untuk production:

#### 1. Install PostgreSQL

**Ubuntu/Debian:**
```bash
sudo apt-get install postgresql postgresql-contrib
```

**macOS:**
```bash
brew install postgresql
```

#### 2. Buat Database

```bash
sudo -u postgres psql -c "CREATE DATABASE image_gallery;"
```

#### 3. Set Environment Variables

```bash
export DB_NAME=image_gallery
export DB_PASSWORD=your_password
```

Atau buat file `.env`:
```bash
cp .env.example .env
# Edit file .env dengan credentials Anda
```

#### 4. Migrate

```bash
python3 manage.py migrate
```

#### 5. Run

```bash
python3 manage.py runserver
```

📖 **Lihat:** `POSTGRES_SETUP.md` untuk panduan lengkap

---

## 📋 Commands yang Berguna

```bash
# Jalankan server
python3 manage.py runserver

# Buat superuser (admin)
python3 manage.py createsuperuser

# Build CSS (jika ada perubahan)
npm run build:css

# Watch CSS changes
npm run gentw

# Migrate database
python3 manage.py migrate

# Create sample images
python3 create_samples.py

# Collect static files (production)
python3 manage.py collectstatic
```

---

## 🎯 Fitur Aplikasi

### 1. Upload Gambar
- Klik tombol **"Upload"** di navbar
- Drag & drop atau klik untuk select file
- Tambahkan caption (opsional)
- Upload otomatis menampilkan preview

### 2. Gallery View
- Grid responsive (1-4 kolom)
- Hover untuk lihat info gambar
- Klik untuk buka lightbox
- Download atau delete dari lightbox

### 3. Search
- Ketik di search bar
- Filter instant oleh HTMX
- Hasil real-time tanpa reload

### 4. Pagination
- 12 gambar per halaman
- Navigate dengan tombol prev/next
- Total images ditampilkan

---

## 🔧 Troubleshooting

### Server tidak bisa start?

```bash
# Check Django
python3 manage.py check

# Check database
python3 manage.py migrate --check

# Clear cache
find . -name "*.pyc" -delete
find . -name "__pycache__" -delete
```

### CSS tidak update?

```bash
# Rebuild CSS
npm run build:css

# Clear browser cache (Ctrl+Shift+R)
```

### Database error?

```bash
# Untuk SQLite, reset database
rm db.sqlite3
python3 manage.py migrate
python3 create_samples.py
```

---

## 📚 Dokumentasi Lengkap

| File | Deskripsi |
|------|-----------|
| `README.md` | Dokumentasi utama |
| `UPDATE_SUMMARY.md` | Summary perubahan terbaru |
| `POSTGRES_SETUP.md` | Panduan setup PostgreSQL |
| `CHANGES.md` | Log perubahan sebelumnya |
| `.env.example` | Template environment variables |

---

## 🎊 Selesai!

Aplikasi sudah berjalan dengan:
- ✅ Tema kuning-putih yang cerah
- ✅ Database SQLite (ready untuk PostgreSQL)
- ✅ 10 sample images
- ✅ Semua fitur berfungsi

**Buka browser:** http://localhost:8000

**Selamat menggunakan! 🎉**
