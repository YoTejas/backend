from django.contrib import admin
from .models.agent import Agent
from .models.client import Client
from django.contrib.auth.models import User
from .forms import UserForm, CustomUserForm
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponse
import csv
from django.core import mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def download_clients_csv(modeladmin, request, queryset):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=clients.csv'

    writer = csv.writer(response)
    writer.writerow(["first_name", "last_name", "email", "phone", "is_active"])
    for s in queryset:
        writer.writerow([s.first_name, s.last_name, s.email, s.client.phone, s.is_active])
    
    return response

def download_agents_csv(modeladmin, request, queryset):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=clients.csv'

    writer = csv.writer(response)
    writer.writerow(["first_name", "last_name", "email", "phone", "is_active"])
    for s in queryset:
        writer.writerow([s.first_name, s.last_name, s.email, s.agent.phone, s.is_active])
    
    return response


class ClientUser(User):
    class Meta:
        proxy = True
        verbose_name = 'Client User'
        verbose_name_plural = 'Client Users'

class AgentUser(User):
    class Meta:
        proxy = True
        verbose_name = 'Agent User'
        verbose_name_plural = 'Agent Users'

class ClientInline(admin.StackedInline):
    model = Client
    can_delete = False
    verbose_name_plural = 'client'

class AgentInline(admin.StackedInline):
    model = Agent
    can_delete = False
    verbose_name_plural = 'agent'

class UserClientAdmin(admin.ModelAdmin):
    form = UserForm
    inlines = [ClientInline]
    list_display = ('email', 'first_name', 'last_name', 'is_active')
    actions = [download_clients_csv]

    def get_queryset(self, request):
        qs = super(UserClientAdmin, self).get_queryset(request)
        return qs.filter(client__isnull=False)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        return super(UserClientAdmin, self).get_inline_instances(request, obj)
    
    def save_model(self, request, obj, form, change):
        if change:
            original_obj = User.objects.get(pk=obj.pk)
            if original_obj.is_active != obj.is_active and obj.is_active:
                html_template = 'approval_update.html'
                html_message = render_to_string(
                    html_template, 
                    { 
                        'frontend_link': settings.FRONTEND_URL,
                        'first_name': obj.first_name, 
                        'last_name': obj.last_name 
                    })
                plain_message = strip_tags(html_message)
                mail.send_mail('Vista Residency: Account Approval Update', plain_message, settings.EMAIL_HOST_USER, [obj.email], html_message=html_message, fail_silently=False)
                
        super().save_model(request, obj, form, change)

class UserAgentAdmin(admin.ModelAdmin):
    form = UserForm
    inlines = [AgentInline]
    list_display = ('email', 'first_name', 'last_name', 'is_active')
    actions =[download_agents_csv]

    def get_queryset(self, request):
        qs = super(UserAgentAdmin, self).get_queryset(request)
        return qs.filter(agent__isnull=False)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        return super(UserAgentAdmin, self).get_inline_instances(request, obj)
    
    def save_model(self, request, obj, form, change):
        if change:
            original_obj = User.objects.get(pk=obj.pk)
            if original_obj.is_active != obj.is_active and obj.is_active:
                html_template = 'approval_update.html'
                html_message = render_to_string(
                    html_template, 
                    { 
                        'frontend_link': settings.FRONTEND_URL,
                        'first_name': obj.first_name, 
                        'last_name': obj.last_name 
                    })
                plain_message = strip_tags(html_message)
                mail.send_mail('Vista Residency: Account Approval Update', plain_message, settings.EMAIL_HOST_USER, [obj.email], html_message=html_message, fail_silently=False)
                
        super().save_model(request, obj, form, change)

       
admin.site.register(ClientUser, UserClientAdmin)
admin.site.register(AgentUser, UserAgentAdmin)


class CustomUserAdmin(UserAdmin):
    form = CustomUserForm
    list_display = ('username', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('date_joined',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('date_joined',)}),
    )

    def save_model(self, request, obj, form, change):
        obj.username = form.cleaned_data['email']  # Ensure username matches email
        if change:
            original_obj = User.objects.get(pk=obj.pk)
            if original_obj.is_active != obj.is_active and obj.is_active:
                html_template = 'approval_update.html'
                html_message = render_to_string(
                    html_template, 
                    { 
                        'frontend_link': settings.FRONTEND_URL,
                        'first_name': obj.first_name, 
                        'last_name': obj.last_name 
                    })
                plain_message = strip_tags(html_message)
                mail.send_mail('Vista Residency: Account Approval Update', plain_message, settings.EMAIL_HOST_USER, [obj.email], html_message=html_message, fail_silently=False)
        super().save_model(request, obj, form, change)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)