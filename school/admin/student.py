from django.contrib import admin

from school.models.student import StudentModel


@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "cpf",
        "b_day",
        "phone"
    )
    list_display_links = (
        "id",
        "name"
    )
    list_per_page = 10
    search_fields = (
        "name"
    )