from django.contrib import admin

# Register your models here.

from .models import *

from django.utils.safestring import mark_safe


class BookConfig(admin.ModelAdmin):

    def deletes(self):
        return mark_safe("<a href=''>删除</a>")

    list_display = ["title", "price", 'publisher', deletes]
    list_display_links = ["price"]
    list_filter = ["price", "title", "authors", "publisher"]
    list_editable = ["title", ]

    search_fields = ["title", "price"]

    def patch_init(self, request, queryset):
        queryset.update(price=100)

    patch_init.short_description = "批量初始化"

    actions = [patch_init, ]

    # change_list_template="list.html"
    fields = ('title',)


admin.site.register(Book, BookConfig)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(AuthorDetail)
