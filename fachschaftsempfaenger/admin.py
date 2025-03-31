from django.contrib import admin

from .models import Menu, Food, Advertisement, Member, Mastodon


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    search_fields = ['meal']
    list_display = ['meal', 'price']


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'start_date', 'end_date', 'image']


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    ordering = ['last_name']


@admin.register(Mastodon)
class MastodonAdmin(admin.ModelAdmin):
    list_display = ['visible', 'instance', 'username']


admin.site.register(Menu)

