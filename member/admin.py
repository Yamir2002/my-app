from django.contrib import admin
from .models import Register
# Register your models here.
@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('sellername', 'email', 'phone', 'address','additionaldetail')
    ordering = ('sellername', 'email', 'phone', 'address','additionaldetail')
    search_fields = ('sellername', 'email', 'phone', 'address','additionaldetail')
    list_filter = ('sellername', 'email', 'phone', 'address','additionaldetail')