from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.conf import settings
from django_htmx.http import retarget, trigger_client_event
from .models import Image
from .form import ImageForm, ImageSearchForm


class GalleryView(ListView):
    """
    View utama untuk menampilkan gallery gambar
    dengan pagination dan search
    """
    model = Image
    template_name = "image/gallery.html"
    context_object_name = "images"
    paginate_by = 12

    def get_queryset(self):
        queryset = Image.objects.filter(is_active=True)
        
        # Search functionality
        search_query = self.request.GET.get('q', '').strip()
        if search_query:
            queryset = queryset.filter(
                Q(caption__icontains=search_query) |
                Q(image__icontains=search_query)
            )
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ImageForm()
        context['search_form'] = ImageSearchForm(initial={'q': self.request.GET.get('q', '')})
        context['page_title'] = 'Image Gallery'
        return context


def upload_image(request):
    """
    Handle upload gambar (support regular POST dan htmx)
    """
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        
        if form.is_valid():
            form.save()
            
            # Jika request dari htmx
            if request.headers.get('HX-Request'):
                response = HttpResponse()
                response = trigger_client_event(
                    response, 
                    'showToast', 
                    {'message': 'Gambar berhasil diupload!', 'type': 'success'}
                )
                response = trigger_client_event(
                    response,
                    'galleryUpdated'
                )
                return response
            
            messages.success(request, 'Gambar berhasil diupload!')
            return redirect('home')
        else:
            # Jika request dari htmx dengan error
            if request.headers.get('HX-Request'):
                return render(request, "image/partials/upload_form.html", 
                            {'form': form}, 
                            headers={'HX-Reswap': 'outerHTML'})
    
    form = ImageForm()
    return render(request, "image/partials/upload_form.html", {'form': form})


def delete_image(request, pk):
    """
    Hapus gambar dengan konfirmasi
    """
    image = get_object_or_404(Image, pk=pk)
    
    if request.method == "POST":
        caption = image.caption
        image.delete()
        
        if request.headers.get('HX-Request'):
            response = HttpResponse()
            response = trigger_client_event(
                response,
                'showToast',
                {'message': f'Gambar "{caption}" berhasil dihapus', 'type': 'success'}
            )
            response = trigger_client_event(
                response,
                'galleryUpdated'
            )
            return response
        
        messages.success(request, f'Gambar "{caption}" berhasil dihapus')
        return redirect('home')
    
    return render(request, "image/partials/delete_confirm.html", {'image': image})


def search_images(request):
    """
    Live search untuk gallery (htmx powered)
    """
    search_query = request.GET.get('q', '').strip()
    
    images = Image.objects.filter(is_active=True)
    if search_query:
        images = images.filter(
            Q(caption__icontains=search_query) |
            Q(image__icontains=search_query)
        )
    
    return render(request, "image/partials/image_grid.html", 
                 {'images': images, 'search_query': search_query})


def image_detail(request, pk):
    """
    Detail view untuk单个 gambar (lightbox)
    """
    image = get_object_or_404(Image, pk=pk)
    return render(request, "image/partials/image_detail.html", {'image': image})


def toggle_image_status(request, pk):
    """
    Toggle status aktif/non-aktif gambar
    """
    if request.method == "POST":
        image = get_object_or_404(Image, pk=pk)
        image.is_active = not image.is_active
        image.save()
        
        if request.headers.get('HX-Request'):
            status = "aktif" if image.is_active else "non-aktif"
            response = HttpResponse()
            response = trigger_client_event(
                response,
                'showToast',
                {'message': f'Gambar di{status}', 'type': 'info'}
            )
            return response
    
    return redirect('home')


def about(request):
    """
    Halaman about sederhana
    """
    return render(request, "image/about.html")
