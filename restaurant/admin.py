from django.contrib import admin
from .models import Menu, Booking


# Register your models here.
#admin.site.register(Booking)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
        list_display = ('first_name', 'last_name', 'guest_number', 'comment')


admin.site.register(Menu)