from django.contrib import admin

# Register your models here.
from .models import *


class ImageInLine(admin.TabularInline):
    model = CodeImage
    min_num = 1
    max_num = 5

@admin.register(Problema)
class ProblemAdmin(admin.ModelAdmin):
    inlines = [ImageInLine, ]


admin.site.register(Reply)
admin.site.register(Comment)
