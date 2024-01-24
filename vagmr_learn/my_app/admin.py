from django.contrib import admin
from my_app.models import Books
# Register your models here.


class BooksAdmin(admin.ModelAdmin):
    list_display = ('bid', 'isbn', 'title', 'author', 'pages', 'price')
    fieldsets = [
        ("编号", {"fields": ['isbn']}),
        ("书籍信息", {"fields": ['title', 'author', 'pages']}),
        ("价钱", {"fields": ['price']})
    ]


admin.site.register(Books, BooksAdmin)
