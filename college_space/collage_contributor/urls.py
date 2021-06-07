from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings


admin.site.site_header = 'Collage-Contributor admin'
admin.site.site_title = 'Collage-Contributor admin'

admin.site.index_title = 'Collage-Contributor administration'

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^users/', include(('users.urls', 'users'), namespace='users')),
    

    url(r'', include(('contributor.urls', 'contributor'), namespace='contributor')),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
