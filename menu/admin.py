from django.contrib import admin

# Register your models here.
from menu.models import Menu, MenuItem


@admin.register(MenuItem)
class MenuItemadmin(admin.ModelAdmin):
    pass


@admin.register(Menu)
class Menuadmin(admin.ModelAdmin):
    pass
