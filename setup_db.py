#!/usr/bin/env python3
"""
Script untuk setup PostgreSQL database untuk Image Gallery.
Jalankan script ini untuk membuat database secara otomatis.
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run shell command and print status"""
    print(f"⏳ {description}...")
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"✅ {description} - Success!")
            return True
        else:
            print(f"❌ {description} - Failed!")
            if result.stderr:
                print(f"   Error: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"❌ {description} - Exception: {e}")
        return False

def check_postgresql():
    """Check if PostgreSQL is installed"""
    print("🔍 Checking PostgreSQL installation...")
    try:
        result = subprocess.run(
            ["psql", "--version"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"✅ {result.stdout.strip()}")
            return True
        else:
            print("❌ PostgreSQL is not installed!")
            return False
    except FileNotFoundError:
        print("❌ PostgreSQL is not installed!")
        print("\nPlease install PostgreSQL first:")
        print("   Ubuntu/Debian: sudo apt-get install postgresql postgresql-contrib")
        print("   macOS: brew install postgresql")
        print("   Windows: Download from https://www.postgresql.org/download/")
        return False

def create_database(db_name):
    """Create PostgreSQL database"""
    print(f"\n📦 Creating database '{db_name}'...")
    
    # Try to create database using postgres user
    commands = [
        f"sudo -u postgres psql -c \"CREATE DATABASE {db_name};\"",
        f"psql -U postgres -c \"CREATE DATABASE {db_name};\"",
    ]
    
    for command in commands:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"✅ Database '{db_name}' created successfully!")
            return True
        elif "already exists" in result.stderr.lower():
            print(f"⚠️  Database '{db_name}' already exists!")
            return True
    
    print("⚠️  Could not create database automatically.")
    print("   Please create it manually:")
    print(f"   sudo -u postgres psql -c \"CREATE DATABASE {db_name};\"")
    return False

def main():
    print("=" * 60)
    print("🚀 PostgreSQL Setup for Image Gallery")
    print("=" * 60)
    print()
    
    # Configuration
    DB_NAME = "image_gallery"
    DB_USER = "postgres"
    
    print("📋 Database Configuration:")
    print(f"   Database Name: {DB_NAME}")
    print(f"   Database User: {DB_USER}")
    print()
    
    # Check PostgreSQL
    if not check_postgresql():
        sys.exit(1)
    
    # Create database
    if not create_database(DB_NAME):
        print("\n⚠️  Database setup requires manual intervention.")
    
    print("\n" + "=" * 60)
    print("✅ Setup Complete!")
    print("=" * 60)
    print()
    print("📝 Next steps:")
    print("   1. Run migrations:")
    print("      python3 manage.py migrate")
    print()
    print("   2. Create superuser (optional):")
    print("      python3 manage.py createsuperuser")
    print()
    print("   3. Run the server:")
    print("      python3 manage.py runserver")
    print()
    print("   4. Access the app:")
    print("      http://localhost:8000")
    print()

if __name__ == "__main__":
    main()
