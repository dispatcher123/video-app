from django.contrib import admin
from .models import Course,CourseModule,Profile
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=('course_name','is_premium')

@admin.register(CourseModule)
class CourseModuleAdmin(admin.ModelAdmin):
    list_display=('course_module_name','can_view')

admin.site.register(Profile)