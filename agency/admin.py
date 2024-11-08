from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import SliderImage


@admin.register(SliderImage)
class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return '<img src="%s" width="100" height="100" />' % obj.image.url

    image_preview.allow_tags = True
    image_preview.short_description = 'Preview'
