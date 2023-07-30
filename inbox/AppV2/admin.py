from django.contrib import admin
from AppV2.models import Client

class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'name' , 'phone', 'email', 'subject', 'message', 'file')
    list_display = ['name', 'email', 'subject', 'received_at', 'situation',]
    list_filter = ['name', 'phone', 'email', 'subject', 'message', 'file']
    search_fields = ['name', 'phone', 'email', 'subject']
    list_per_page = 10
    
admin.site.register(Client, ClientAdmin)