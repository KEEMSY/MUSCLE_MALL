from django.contrib import admin

# Register your models here.
from userapp.models import User, Coach


class CoachInline(admin.StackedInline):
    model = Coach


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'fullname', 'gender', ]
    readonly_fields = ('username', 'join_date',)
    search_fields = ('username', 'fullname')

    # 생성 시 write 가능, 수정 시 readonly field로 설정
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('username', 'join_date',)
        else:
            return ('join_date',)

    fieldsets = (
        ("info", {'fields': ('username', 'fullname', 'join_date')}),
        ('permissions', {'fields': ('is_admin', 'is_active', 'approved_user')}),
    )

    inlines = (
        CoachInline,
    )


class CoachAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'phone_number', 'kind']
    search_fields = ('nickname', 'kind')

    fieldsets = (
        ("info", {'fields': ('nickname', 'phone_number', 'kind')}),
        ('permissions', {'fields': ('approved_coach',)}),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Coach, CoachAdmin)
