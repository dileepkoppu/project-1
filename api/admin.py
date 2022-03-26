from django.contrib import admin

from .models import Kid,Image




class MyModelAdmin(admin.ModelAdmin):
    readonly_fields=('updated_on','image_preview')
    radio_fields={'food_group':admin.HORIZONTAL}
    list_display=('kid_name','food_group','created_on')

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'image Preview'
    image_preview.allow_tags = True


admin.site.register(Kid)
admin.site.register(Image,MyModelAdmin)
