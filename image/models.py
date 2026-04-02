import os
from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings


class Image(models.Model):
    """
    Model untuk menyimpan gambar yang diupload user.
    Dilengkapi dengan metadata untuk optimisasi dan tracking.
    """
    caption = models.CharField(
        max_length=200,
        help_text="Deskripsi atau caption untuk gambar"
    )
    image = models.ImageField(
        upload_to="images/%Y/%m/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'webp']
            )
        ],
        help_text="File gambar (max 5MB)"
    )
    file_size = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Ukuran file dalam bytes"
    )
    width = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Lebar gambar dalam pixel"
    )
    height = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Tinggi gambar dalam pixel"
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Tanggal dan waktu upload"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Tanggal dan waktu update terakhir"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Status aktif/tidak aktif gambar"
    )

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = "Image"
        verbose_name_plural = "Images"
        indexes = [
            models.Index(fields=['-uploaded_at']),
            models.Index(fields=['is_active', '-uploaded_at']),
        ]

    def __str__(self):
        return self.caption or f"Image {self.pk}"

    def save(self, *args, **kwargs):
        """Override save untuk menyimpan metadata gambar"""
        # Simpan file terlebih dahulu jika ini adalah instance baru
        is_new = self.pk is None
        
        if self.image:
            # Simpan file size
            try:
                self.file_size = self.image.size
            except Exception:
                pass
        
        # Save first to store the file
        super().save(*args, **kwargs)
        
        # Now read dimensions from saved file
        if self.image and is_new:
            try:
                from PIL import Image as PILImage
                img_path = self.image.path
                with PILImage.open(img_path) as img:
                    self.width, self.height = img.size
                    # Update without triggering another file save
                    Image.objects.filter(pk=self.pk).update(
                        width=self.width,
                        height=self.height
                    )
            except Exception as e:
                print(f"Error reading image dimensions: {e}")

    def delete(self, *args, **kwargs):
        """Hapus file gambar saat record dihapus"""
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    @property
    def file_size_mb(self):
        """Return file size in MB"""
        if self.file_size:
            return round(self.file_size / (1024 * 1024), 2)
        return 0

    @property
    def aspect_ratio(self):
        """Return aspect ratio gambar"""
        if self.width and self.height:
            return round(self.width / self.height, 2)
        return 0

    @property
    def is_landscape(self):
        """Check apakah gambar landscape"""
        return self.aspect_ratio > 1 if self.aspect_ratio else False

    @property
    def is_portrait(self):
        """Check apakah gambar portrait"""
        return self.aspect_ratio < 1 if self.aspect_ratio else False

    @property
    def thumbnail_url(self):
        """Return URL gambar (bisa dimodifikasi untuk thumbnail)"""
        return self.image.url if self.image else ''
