# -*- coding: cp1251 -*-

from django.contrib import admin
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from library.models import Book, Author, Publisher, BookImage


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email',)
    list_display_links = ('first_name', 'last_name',)
    ordering  = ('last_name', 'first_name',)

admin.site.register(Author, AuthorAdmin)


class BookImageInline(generic.GenericTabularInline):
   model = BookImage


class BookAdmin(admin.ModelAdmin):

    def avatar_small(self, image):
        link = ""
        for i in BookImage.objects.filter(id = image.id):
            link = i.show_avatar()
            return link
    avatar_small.allow_tags = True

    def count(self, image):
        cnt = 0
        for i in BookImage.objects.filter(id = image.id):
            if i.avatar:
                cnt += 1
        return cnt
    count.allow_tags = True    
    
    list_display = ('id', 'title', 'publisher', 'count', 'avatar_small')
    list_display_links = ('title',)
    list_editable = ('publisher',)
    list_filter = ('authors', 'publisher', 'publication_date')
    ordering  = ('title',)
    date_hierarchy = 'publication_date'
    fieldsets = (
        (None, {'fields': ('title', 'authors')}),
        ('Выходные данные', {
            'classes': ('collapse',),
            'description': u'Данные об издательстве и издании',
            'fields': ('publisher', 'publication_date'),
            }),
    )
    filter_horizontal = ('authors',)
    inlines = (BookImageInline,)

    def print_version(self, obj):
        return "издание №%d" % obj.version

admin.site.register(Book, BookAdmin)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'country', 'city')
    list_display_links = ('title',)
    list_filter = ('country', 'city',)
    ordering  = ('title',)
    fieldsets = (
        (None, {'fields': ('title', 'website')}),
        ('Контактная информация', {
            'classes': ('collapse',),
            'fields': ('country', 'city', 'address'),
            }),
    )

admin.site.register(Publisher, PublisherAdmin)


class BookImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'fkey', 'show_avatar',)

admin.site.register(BookImage, BookImageAdmin)
