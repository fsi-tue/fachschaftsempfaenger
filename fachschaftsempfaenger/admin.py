from django.contrib import admin

from .models import Menu, Food, Advertisement, Member, Mastodon


class FoodAdmin(admin.ModelAdmin):
    search_fields = ['meal']
    list_display = ['meal', 'price']


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'start_date', 'end_date', 'image']


class MemberAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    ordering = ['last_name']


class MastodonAdmin(admin.ModelAdmin):
    list_display = ['visible', 'instance', 'username']


admin.site.register(Food, FoodAdmin)
admin.site.register(Menu)
admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Mastodon, MastodonAdmin)
