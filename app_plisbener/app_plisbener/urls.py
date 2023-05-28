from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("upload/", include("upload.urls")),
    path('admin/', admin.site.urls),
    path('download/<int:image_id>/', download_image_view, name='download_image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
