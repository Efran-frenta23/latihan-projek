# 🖼️ Modern Image Gallery

A clean, fast, and beautiful image gallery application built with Django, Tailwind CSS, and HTMX.

**Theme:** Yellow & White ☀️

## ✨ Features

- **🚀 Fast & Lightweight** - Minimal JavaScript, powered by HTMX for dynamic interactions
- **🎨 Modern UI** - Beautiful yellow & white theme with Tailwind CSS and DaisyUI
- **📱 Fully Responsive** - Works perfectly on all devices
- **🖼️ Drag & Drop Upload** - Easy image upload with preview
- **🔍 Live Search** - Filter images instantly
- **💡 Lightbox Gallery** - Beautiful image viewing with zoom
- **📊 Image Metadata** - Auto-detect dimensions and file size
- **🔒 Secure** - Built-in validation and CSRF protection
- **⚡ Pagination** - Efficient handling of large image collections
- **🗄️ PostgreSQL** - Production-ready database backend

## 🛠️ Tech Stack

- **Backend**: Django 4.2
- **Database**: PostgreSQL
- **Frontend**: Tailwind CSS + DaisyUI (Yellow & White theme)
- **Interactivity**: HTMX + Alpine.js
- **Image Processing**: Pillow

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+
- PostgreSQL 12+
- pip

### Installation

1. **Install Python dependencies:**
   ```bash
   pip install --break-system-packages psycopg2-binary pillow
   ```

2. **Install Node dependencies:**
   ```bash
   npm install
   ```

3. **Setup PostgreSQL Database:**
   
   **Option A: Automatic setup (Linux/Mac)**
   ```bash
   python3 setup_db.py
   ```
   
   **Option B: Manual setup**
   ```bash
   # Create database
   sudo -u postgres psql -c "CREATE DATABASE image_gallery;"
   
   # Or use psql directly
   psql -U postgres
   CREATE DATABASE image_gallery;
   \q
   ```

4. **Configure environment (optional):**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

5. **Build CSS:**
   ```bash
   npm run build:css
   ```

6. **Run migrations:**
   ```bash
   python3 manage.py migrate
   ```

7. **Create superuser (optional):**
   ```bash
   python3 manage.py createsuperuser
   ```

8. **Start development server:**
   ```bash
   python3 manage.py runserver
   ```

9. **Open browser:**
   Navigate to `http://localhost:8000`

## 📁 Project Structure

```
latihan-projek/
├── image/                      # Main Django app
│   ├── models.py              # Image model with metadata
│   ├── views.py               # Class-based views + HTMX handlers
│   ├── form.py                # Forms with validation
│   ├── urls.py                # URL routing
│   ├── admin.py               # Admin configuration
│   ├── templates/image/       # Templates
│   │   ├── base.html         # Base template
│   │   ├── gallery.html      # Main gallery page
│   │   ├── about.html        # About page
│   │   └── partials/         # Reusable components
│   └── static/image/         # Static files
│       ├── input.css         # Tailwind source
│       └── style.css         # Compiled CSS
├── projek/                    # Django project settings
├── media/                     # Uploaded images
└── manage.py                  # Django management script
```

## 🎯 Usage

### Upload Images

1. Click the **Upload** button in the navbar
2. Drag and drop an image or click to select
3. Add an optional caption
4. Click **Upload Image**

### View Images

- Click any image to open the lightbox
- Use the zoom and download options
- Delete images with confirmation

### Search

- Use the search bar to filter images by caption
- Results update instantly with HTMX

### Admin Panel

Access the admin panel at `/admin/` to:
- Manage all images
- View metadata (dimensions, file size)
- Bulk operations

## ⚙️ Configuration

### Database Settings

Edit `projek/settings.py` or use environment variables:

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

### Environment Variables (.env)

```bash
DB_NAME=image_gallery
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

### Upload Limits

Edit `projek/settings.py`:

```python
IMAGE_UPLOAD_MAX_SIZE = 5 * 1024 * 1024  # 5MB
IMAGE_UPLOAD_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
```

### Pagination

Edit `image/views.py` - `GalleryView.paginate_by`:

```python
paginate_by = 12  # Images per page
```

### Theme

Edit `tailwind.config.js`:

```javascript
daisyui: {
  themes: ["dim", "dark"],
  darkTheme: "dim",
}
```

## 🔧 Development

### Watch CSS changes:
```bash
npm run gentw
```

### Build production CSS:
```bash
npm run build:css
```

### Create migrations:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

## 📝 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main gallery page |
| `/upload/` | POST | Upload image |
| `/search/` | GET | Search images |
| `/image/<id>/` | GET | Image detail |
| `/image/<id>/delete/` | POST | Delete image |
| `/admin/` | GET | Admin panel |

## 🎨 Customization

### Add custom themes:
1. Edit `tailwind.config.js`
2. Add to `daisyui.themes`
3. Rebuild CSS

### Modify grid layout:
Edit `image/templates/image/partials/image_grid.html`:
```html
<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
```

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [Django](https://www.djangoproject.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [DaisyUI](https://daisyui.com/)
- [HTMX](https://htmx.org/)
- [Alpine.js](https://alpinejs.dev/)

---

Made with ❤️ using Django + Tailwind + HTMX
