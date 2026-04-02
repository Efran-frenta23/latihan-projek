from django import forms
from django.core.exceptions import ValidationError
from django.conf import settings
from .models import Image


class ImageForm(forms.ModelForm):
    """Form untuk upload gambar dengan validasi lengkap"""
    
    class Meta:
        model = Image
        fields = ["caption", "image"]
        widgets = {
            'caption': forms.TextInput(attrs={
                'placeholder': 'Tambahkan caption (opsional)...',
                'class': 'input input-bordered w-full',
                'maxlength': '200',
            }),
            'image': forms.FileInput(attrs={
                'class': 'file-input file-input-bordered w-full',
                'accept': 'image/*',
            }),
        }

    def clean_caption(self):
        """Validasi caption"""
        caption = self.cleaned_data.get('caption', '').strip()
        if len(caption) > 200:
            raise ValidationError("Caption terlalu panjang (max 200 karakter)")
        return caption

    def clean_image(self):
        """Validasi file gambar"""
        image = self.cleaned_data.get('image')
        
        if not image:
            raise ValidationError("Gambar wajib diupload")
        
        # Validasi ukuran file (max 5MB)
        max_size = getattr(settings, 'IMAGE_UPLOAD_MAX_SIZE', 5 * 1024 * 1024)
        if image.size > max_size:
            raise ValidationError(
                f"Ukuran file terlalu besar (max {max_size // 1024 // 1024}MB)"
            )
        
        # Validasi tipe file
        allowed_extensions = getattr(
            settings, 
            'IMAGE_UPLOAD_EXTENSIONS',
            ['.jpg', '.jpeg', '.png', '.gif', '.webp']
        )
        ext = image.name.split('.')[-1].lower()
        if f'.{ext}' not in allowed_extensions:
            raise ValidationError(
                f"Tipe file tidak didukung. Gunakan: {', '.join(allowed_extensions)}"
            )
        
        return image


class ImageSearchForm(forms.Form):
    """Form untuk pencarian gambar"""
    q = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Cari gambar...',
            'class': 'input input-sm input-bordered w-full',
        })
    )
