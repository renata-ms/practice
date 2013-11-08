from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'library.views.books'),
                       url(r'^library/$', 'library.views.books'),
                       url(r'^library/books/$', 'library.views.books'),
                       url(r'^library/books/(\d+)/$', 'library.views.book'),
                       url(r'^library/authors/$', 'library.views.authors'),
                       url(r'^library/authors/(\d+)/$', 'library.views.author'),
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
                       url(r'^admin/', include(admin.site.urls)),
                       )
