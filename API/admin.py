from django.contrib import admin
from .models import Task, Book, BTSMembers
# Register your models here.
admin.site.register(Task)
admin.site.register(Book)


@admin.register(BTSMembers)
class BTSAdmin(admin.ModelAdmin):
    list_display = ['id', 'MemberName', 'age', 'GoodThingAboutHim']
