from django.contrib import admin

from school.models.course import CourseModel


@admin.register(CourseModel)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "code",
        "description"
    )
    list_display_links = (
        "id",
        "code"
    )
    list_per_page = 10
    search_fields = (
        "code"
    )
