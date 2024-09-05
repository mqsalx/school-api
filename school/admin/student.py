from django.contrib import admin

from school.models.student import StudentModel


@admin.register(StudentModel)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "cpf", "b_day", "phone")
    list_display_links = ("id", "name")
    list_per_page = 10
    search_fields = ("name",)
