#!/usr/bin/env python3
"""
Script to add sample images for testing the gallery.
Creates placeholder images using Pillow.
"""

import os
import sys
import django

# Setup Django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projek.settings')
django.setup()

from django.core.files.base import ContentFile
from PIL import Image as PILImage
import io
from image.models import Image

def create_sample_image(name, caption, size=(800, 600), color=(255, 100, 100)):
    """Create a sample image with gradient effect"""
    # Create image with gradient
    img = PILImage.new('RGB', size, color=color)
    
    # Add some visual variation
    pixels = img.load()
    for i in range(size[0]):
        for j in range(size[1]):
            r = min(255, color[0] + (i % 50))
            g = min(255, color[1] + (j % 50))
            b = min(255, color[2] + ((i + j) % 50))
            pixels[i, j] = (r, g, b)
    
    # Save to bytes
    buffer = io.BytesIO()
    img.save(buffer, format='JPEG', quality=85)
    buffer.seek(0)
    
    return ContentFile(buffer.read(), name=f"{name}.jpg")

def main():
    print("Creating sample images...")
    
    samples = [
        ("landscape_1", "Beautiful Landscape", (1200, 800), (34, 139, 34)),
        ("portrait_1", "Portrait Shot", (800, 1200), (255, 105, 180)),
        ("sunset", "Amazing Sunset", (1024, 768), (255, 140, 0)),
        ("ocean", "Ocean View", (1200, 900), (0, 105, 148)),
        ("mountain", "Mountain Peak", (1024, 768), (139, 90, 43)),
        ("city", "City Lights", (1200, 800), (72, 61, 139)),
        ("forest", "Deep Forest", (800, 1000), (0, 100, 0)),
        ("abstract", "Abstract Art", (900, 900), (255, 20, 147)),
        ("minimal", "Minimal Design", (1024, 768), (245, 245, 220)),
        ("vibrant", "Vibrant Colors", (1200, 800), (255, 69, 0)),
    ]
    
    created_count = 0
    for filename, caption, size, color in samples:
        try:
            # Check if already exists
            if Image.objects.filter(caption=caption).exists():
                print(f"⏭️  Skipping: {caption} (already exists)")
                continue
            
            # Create and save image
            image_file = create_sample_image(filename, caption, size, color)
            image = Image(caption=caption)
            image.image.save(f"{filename}.jpg", image_file, save=True)
            
            print(f"✅ Created: {caption} ({image.width}x{image.height}, {image.file_size_mb} MB)")
            created_count += 1
            
        except Exception as e:
            print(f"❌ Error creating {caption}: {e}")
    
    print(f"\n✨ Done! Created {created_count} sample images.")
    print(f"📊 Total images in database: {Image.objects.count()}")

if __name__ == "__main__":
    main()
