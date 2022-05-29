from django.contrib import admin 
from .models import EarlyUser, Profile, Product
from django.contrib.auth.admin import UserAdmin


class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_joined'
    list_display = ('username','prenom', 'nom', 'date_de_naissance', 'is_active', 'is_staff', 'last_login')
    list_filter = ('date_joined', 'last_login')



class EarlyUserAdmin(admin.ModelAdmin):
    list_display = ('nom', 'phone', 'registered')
    
admin.site.register(Product)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(EarlyUser,EarlyUserAdmin)