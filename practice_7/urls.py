from django.conf.urls import patterns, include, url
from django.conf import settings
from orders.views import CustomersList, CustomerDetails
from library.views import BookList, AuthorList, BookDetail, AuthorDetail

from django.contrib.auth.views import login, logout
from django.contrib.auth.forms import AuthenticationForm
from library.views import registration

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^$', BookList.as_view()),
                       url(r'^library/$', BookList.as_view()),
                       url(r'^library/books/$', BookList.as_view()),
                       url(r'^library/books/(?P<pk>\d+)/$', BookDetail.as_view(), name='book_card.html'),
                       url(r'^library/authors/(?P<pk>\d+)/$', AuthorDetail.as_view(), name='author_card.html'),
                       url(r'^library/authors/$', AuthorList.as_view(), name='authors.html'),
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
                       url(r'^orders/$', CustomersList.as_view()),
                       url(r'^orders/customers/(?P<pk>\d+)/$', CustomerDetails.as_view(template_name='customer.html')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^login/$', login),
                       url(r'^logout/$', logout),
                       url(r'^registration/$', registration), )
