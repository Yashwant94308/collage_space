from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # home page
    url(r'^$', views.index, name='index'),
    # routines
    url(r'^routines/$', views.routines, name='routines'),
    url(r'^books/$', views.books, name='books'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^books_upload/$', views.books_upload, name='books_upload'),
    url(r'^routine_upload/$', views.routines_upload, name='routine_upload'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

