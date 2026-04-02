from django.contrib import admin
from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['caption', 'file_size_mb', 'width', 'height', 'uploaded_at', 'is_active']
    list_filter = ['is_active', 'uploaded_at']
    search_fields = ['caption']
    readonly_fields = ['file_size', 'width', 'height', 'aspect_ratio', 'uploaded_at', 'updated_at']
    list_editable = ['is_active']
    
    fieldsets = (
        ('Informasi Utama', {
            'fields': ('caption', 'image')
        }),
        ('Metadata (Auto-generated)', {
            'fields': ('file_size', 'width', 'height', 'aspect_ratio'),
            'classes': ('collapse',)
        }),
        ('Status & Timestamps', {
            'fields': ('is_active', 'uploaded_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def aspect_ratio(self, obj):
        return obj.aspect_ratio if obj.aspect_ratio else '-'
    
    def file_size_mb(self, obj):
        return f"{obj.file_size_mb} MB" if obj.file_size else '-'
    
    file_size_mb.short_description = 'Ukuran File'
