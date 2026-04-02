# 🗄️ PostgreSQL Setup Guide

## Overview

Aplikasi Image Gallery sekarang menggunakan **PostgreSQL** sebagai database backend untuk production-ready performance.

---

## 📋 Prerequisites

- PostgreSQL 12+ installed
- Python 3.8+
- `psycopg2-binary` installed

---

## 🔧 Installation

### 1. Install PostgreSQL

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
```

**macOS (Homebrew):**
```bash
brew install postgresql
```

**Windows:**
Download dari https://www.postgresql.org/download/

### 2. Install Python Adapter

```bash
pip install psycopg2-binary
```

---

## 🚀 Database Setup

### Option A: Automatic Setup (Recommended)

Jalankan script setup otomatis:

```bash
python3 setup_db.py
```

Script ini akan:
- ✅ Cek PostgreSQL installation
- ✅ Buat database `image_gallery`
- ✅ Berikan instruksi selanjutnya

### Option B: Manual Setup

1. **Login ke PostgreSQL:**
   ```bash
   sudo -u postgres psql
   ```

2. **Create database:**
   ```sql
   CREATE DATABASE image_gallery;
   ```

3. **Exit PostgreSQL:**
   ```sql
   \q
   ```

4. **Verify database created:**
   ```bash
   sudo -u postgres psql -c "\l" | grep image_gallery
   ```

---

## ⚙️ Configuration

### Environment Variables

Buat file `.env` di root project:

```bash
cp .env.example .env
```

Edit `.env`:

```bash
# Database Configuration
DB_NAME=image_gallery
DB_USER=postgres
DB_PASSWORD=your_password_here
DB_HOST=localhost
DB_PORT=5432

# Django Settings
DEBUG=True
SECRET_KEY=your-secret-key-here
```

### Database Settings di Django

Settings sudah dikonfigurasi di `projek/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'image_gallery'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'postgres'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
```

---

## 🔐 PostgreSQL User Setup (Optional)

### Create Dedicated User

1. **Login ke PostgreSQL:**
   ```bash
   sudo -u postgres psql
   ```

2. **Create user:**
   ```sql
   CREATE USER image_gallery_user WITH PASSWORD 'secure_password';
   ```

3. **Grant privileges:**
   ```sql
   GRANT ALL PRIVILEGES ON DATABASE image_gallery TO image_gallery_user;
   ```

4. **Update `.env`:**
   ```bash
   DB_USER=image_gallery_user
   DB_PASSWORD=secure_password
   ```

---

## 📊 Migrations

Setelah database setup, jalankan migrations:

```bash
python3 manage.py migrate
```

Output yang diharapkan:
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, image, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  ...
```

---

## 🧪 Testing Connection

### Test Database Connection

```bash
python3 manage.py dbshell
```

Jika berhasil, Anda akan masuk ke PostgreSQL shell:
```sql
image_gallery=# \dt
image_gallery=# \q
```

### Check Database Info

```bash
psql -U postgres -d image_gallery -c "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"
```

---

## 🔄 Migration from SQLite

Jika sebelumnya menggunakan SQLite, migrate data:

### 1. Export SQLite Data

```bash
python3 manage.py dumpdata --natural-foreign --natural-primary --exclude auth.permission --exclude contenttypes.contenttype > backup.json
```

### 2. Setup PostgreSQL

Ikuti langkah setup PostgreSQL di atas.

### 3. Run Migrations

```bash
python3 manage.py migrate
```

### 4. Import Data

```bash
python3 manage.py loaddata backup.json
```

---

## 🛠️ Management Commands

### Create Superuser

```bash
python3 manage.py createsuperuser
```

### Collect Static Files

```bash
python3 manage.py collectstatic
```

### Database Shell

```bash
python3 manage.py dbshell
```

### Check Database

```bash
python3 manage.py check --database default
```

---

## 🔍 Troubleshooting

### Error: "database does not exist"

```bash
# Verify database exists
sudo -u postgres psql -c "\l" | grep image_gallery

# If not exists, create it
sudo -u postgres psql -c "CREATE DATABASE image_gallery;"
```

### Error: "role does not exist"

```bash
# Create role
sudo -u postgres psql -c "CREATE ROLE postgres WITH LOGIN SUPERUSER;"
```

### Error: "authentication failed"

Check `.env` file:
```bash
DB_PASSWORD=correct_password
```

Check `pg_hba.conf`:
```bash
# Location: /etc/postgresql/*/main/pg_hba.conf
# Ensure this line exists:
local   all             postgres                                md5
```

### Connection Refused

Start PostgreSQL service:

**Ubuntu/Debian:**
```bash
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

**macOS:**
```bash
brew services start postgresql
```

---

## 📈 Database Optimization

### Create Indexes

Model sudah memiliki indexes untuk performa:

```python
class Meta:
    indexes = [
        models.Index(fields=['-uploaded_at']),
        models.Index(fields=['is_active', '-uploaded_at']),
    ]
```

### Vacuum Database

```bash
psql -U postgres -d image_gallery -c "VACUUM ANALYZE;"
```

### Check Database Size

```bash
psql -U postgres -d image_gallery -c "SELECT pg_size_pretty(pg_database_size('image_gallery'));"
```

---

## 🎯 Production Deployment

### Environment Variables for Production

```bash
DB_NAME=production_image_gallery
DB_USER=prod_user
DB_PASSWORD=strong_secure_password_here
DB_HOST=your-db-host.com
DB_PORT=5432
DEBUG=False
SECRET_KEY=your-production-secret-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

### PostgreSQL Production Settings

Edit `postgresql.conf`:
```
max_connections = 100
shared_buffers = 256MB
work_mem = 8MB
```

Edit `pg_hba.conf` for remote access:
```
host    image_gallery   prod_user   0.0.0.0/0   md5
```

---

## 📚 Additional Resources

- [Django PostgreSQL Documentation](https://docs.djangoproject.com/en/4.2/ref/databases/#postgresql-notes)
- [PostgreSQL Official Docs](https://www.postgresql.org/docs/)
- [psycopg2 Documentation](https://www.psycopg.org/docs/)

---

## ✅ Checklist

- [ ] PostgreSQL installed
- [ ] Database `image_gallery` created
- [ ] `.env` file configured
- [ ] Migrations applied
- [ ] Superuser created
- [ ] Connection tested
- [ ] App running successfully

---

**Happy coding with PostgreSQL! 🚀**
