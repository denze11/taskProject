from django.contrib import admin
from .models import Task, Department, Category


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'department', 'description',)
    list_display_links = ('id', 'department', 'description',)
    list_filter = ('category', 'department',)
    search_fields = ('description',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
