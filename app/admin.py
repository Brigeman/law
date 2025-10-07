from django.contrib import admin
from .models import Client, Request, Case, Staff, Appointment, Service, About


# Inline админки
class AppointmentInline(admin.TabularInline):
    model = Appointment
    extra = 0
    fields = ('subject', 'meeting_date', 'is_completed', 'notes')
    readonly_fields = ('created_at',)


class CaseInline(admin.TabularInline):
    model = Case
    extra = 0
    fields = ('title', 'case_number', 'status', 'assigned_to')
    readonly_fields = ('created_at',)


# Кастомизированная админка для Service
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('is_active',)
    ordering = ('-created_at',)


# Кастомизированная админка для Client
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company_name', 'phone', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'company_name', 'phone')
    readonly_fields = ('user', 'created_at', 'updated_at')
    inlines = [CaseInline]
    ordering = ('-created_at',)


# Кастомизированная админка для Request
@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('subject', 'client', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('subject', 'description')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('status',)
    ordering = ('-created_at',)
    
    actions = ['mark_as_contacted', 'mark_as_converted']
    
    def mark_as_contacted(self, request, queryset):
        updated = queryset.update(status='contacted')
        self.message_user(request, f'{updated} заявок отмечено как "Связались"')
    mark_as_contacted.short_description = 'Отметить как "Связались"'
    
    def mark_as_converted(self, request, queryset):
        updated = queryset.update(status='converted')
        self.message_user(request, f'{updated} заявок отмечено как "Преобразована в дело"')
    mark_as_converted.short_description = 'Преобразовать в дело'


# Кастомизированная админка для Case
@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('case_number', 'title', 'client', 'status', 'assigned_to', 'created_at')
    list_filter = ('status', 'created_at', 'assigned_to')
    search_fields = ('case_number', 'title', 'description', 'client__name')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('status', 'assigned_to')
    inlines = [AppointmentInline]
    ordering = ('-created_at',)
    
    actions = ['mark_as_completed', 'mark_as_in_progress']
    
    def mark_as_completed(self, request, queryset):
        updated = queryset.update(status='completed')
        self.message_user(request, f'{updated} дел отмечено как "Завершено"')
    mark_as_completed.short_description = 'Отметить как завершенные'
    
    def mark_as_in_progress(self, request, queryset):
        updated = queryset.update(status='in_progress')
        self.message_user(request, f'{updated} дел отмечено как "В работе"')
    mark_as_in_progress.short_description = 'Отметить как "В работе"'


# Кастомизированная админка для Staff
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role', 'is_active', 'created_at')
    list_filter = ('role', 'is_active', 'created_at')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('user', 'created_at', 'updated_at')
    list_editable = ('is_active', 'role')
    ordering = ('name',)


# Кастомизированная админка для Appointment
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('subject', 'case', 'meeting_date', 'is_completed', 'created_at')
    list_filter = ('is_completed', 'meeting_date', 'created_at')
    search_fields = ('subject', 'notes', 'case__title')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('is_completed',)
    ordering = ('-meeting_date',)
    
    actions = ['mark_as_completed']
    
    def mark_as_completed(self, request, queryset):
        updated = queryset.update(is_completed=True)
        self.message_user(request, f'{updated} встреч отмечено как завершенные')
    mark_as_completed.short_description = 'Отметить как завершенные'


# Кастомизированная админка для About
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
