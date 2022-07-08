from django.contrib import admin

# Register your models here.
from productapp.models import ProductCategory, ProductDetailCategory, Product, Routine, Challenge


class ProductDetailCategoryInline(admin.StackedInline):
    model = ProductDetailCategory


class ProductInline(admin.StackedInline):
    model = Product


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['kind', ]
    readonly_fields = ('kind',)
    search_fields = ('kind', 'description')
    inlines = (
        ProductDetailCategoryInline,
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('kind',)
        else:
            return ('kind',)


class ProductDetailCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', ]
    readonly_fields = ('category',)
    inlines = (
        ProductInline,
    )
    fieldsets = (
        ("info", {'fields': ('name', 'description', 'category')}),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('category',)
        else:
            return ('category',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'difficulty', 'category']
    search_fields = ('name', 'category', 'difficulty')
    readonly_fields = ('category', 'user')
    fieldsets = (
        ("info", {'fields': ('user', 'name', 'description', 'difficulty')}),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('category', 'user')
        else:
            return ('category',)


class RoutineAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity']


class ChallengeAdmin(admin.ModelAdmin):
    list_display = ['user', 'status']


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductDetailCategory, ProductDetailCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Routine, RoutineAdmin)
admin.site.register(Challenge, ChallengeAdmin)
