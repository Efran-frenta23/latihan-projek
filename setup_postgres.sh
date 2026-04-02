#!/bin/bash

# Script untuk setup PostgreSQL database untuk Image Gallery

echo "🚀 Setting up PostgreSQL for Image Gallery..."
echo ""

# Database configuration
DB_NAME="image_gallery"
DB_USER="postgres"

echo "📋 Database Configuration:"
echo "   Database Name: $DB_NAME"
echo "   Database User: $DB_USER"
echo ""

# Check if PostgreSQL is installed
if ! command -v psql &> /dev/null; then
    echo "❌ PostgreSQL is not installed!"
    echo ""
    echo "Please install PostgreSQL first:"
    echo "   Ubuntu/Debian: sudo apt-get install postgresql postgresql-contrib"
    echo "   macOS: brew install postgresql"
    echo "   Windows: Download from https://www.postgresql.org/download/"
    exit 1
fi

echo "✅ PostgreSQL found: $(psql --version)"
echo ""

# Create database
echo "📦 Creating database '$DB_NAME'..."
sudo -u postgres psql -c "CREATE DATABASE $DB_NAME;" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "✅ Database created successfully!"
else
    echo "⚠️  Database might already exist or there was an error"
fi
echo ""

# Set permissions (optional)
echo "🔧 Setting up permissions..."
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"
echo ""

echo "✅ PostgreSQL setup complete!"
echo ""
echo "📝 Next steps:"
echo "   1. Copy .env.example to .env (optional):"
echo "      cp .env.example .env"
echo ""
echo "   2. Run migrations:"
echo "      python3 manage.py migrate"
echo ""
echo "   3. Create superuser (optional):"
echo "      python3 manage.py createsuperuser"
echo ""
echo "   4. Run the server:"
echo "      python3 manage.py runserver"
echo ""
