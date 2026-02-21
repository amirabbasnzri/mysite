from django.contrib import admin
from .models import Portfolio, Project, Category, AboutMe, Message

admin.site.register(Portfolio)
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(AboutMe)

# messages
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    ordering = ('-created_at',)
    
    def has_change_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request):
        return False 
    def has_delete_permission(self, request, obj=None):
        return True