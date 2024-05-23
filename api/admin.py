from django.contrib import admin

# Register your models here.


from .models import Book, YourModel
from .forms import BookCKEditorForm, YourModelForm

class YourModelAdmin(admin.ModelAdmin):
    form = YourModelForm


class BookAdmin(admin.ModelAdmin):
    form = BookCKEditorForm
    list_display = ('title', 'detail')
    search_fields = ['title']
    list_filter = [
        'title'
    ]


admin.site.register(YourModel, YourModelAdmin)
admin.site.register(Book, BookAdmin)
