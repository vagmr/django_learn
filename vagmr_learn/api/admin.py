from django.contrib import admin
from django.utils.html import format_html
from api.models import Course

# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    def formatted_created_at(self, obj):
        return format_html("<span style='white-space: nowrap;'>{}</span>", obj.created_at.strftime("%Y-%m-%d %H:%M:%S"))
    formatted_created_at.admin_order_field = 'created_at'  # Allows column order sorting
    formatted_created_at.short_description = '创建时间'  # Column header
    list_display = ('name', 'info', 'price', 'teacher',
                    'formatted_created_at', 'updated_at')
    # 可以搜索的字段
    search_fields = ('name', 'info', 'price', 'teacher')
    # 可以过滤的字段
    list_filter = search_fields
    fieldsets = [
        ("课程名", {"fields": ['name']}),
        ("课程信息", {"fields": ['info']}),
        ("课程价格", {"fields": ['price']}),
        ("课程讲师", {"fields": ['teacher']}),
    ]
