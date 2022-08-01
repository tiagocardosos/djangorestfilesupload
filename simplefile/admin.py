from django.contrib import admin
from .models import (SimpleFile, SimpleFileCustom, SimpleUploadValidation,
                     SimpleFileDetails, SimpleFileId)

# Register your models here.
admin.site.register(SimpleFile)
admin.site.register(SimpleFileCustom)
admin.site.register(SimpleUploadValidation)


@admin.register(SimpleFileDetails)
class SimpleFileDetailsAdmin(admin.ModelAdmin):
    readonly_fields = ('identifier', 'name', 'hash_name', 'extension', 'size', 'content_type', 'full_path',)


@admin.register(SimpleFileId)
class SimpleFileIdAdmin(admin.ModelAdmin):
    readonly_fields = ('identifier', 'name', 'hash_name', 'extension', 'size', 'content_type', 'full_path',)
