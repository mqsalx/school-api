from django.contrib import admin

from school.models.registration import RegistrationModel


@admin.register(RegistrationModel)
class RegistrationsAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "course", "period")
    list_display_links = ("id", "student")
    list_per_page = 10
    search_fields = ("student",)
