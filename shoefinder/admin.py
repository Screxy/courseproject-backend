from django.contrib import admin

from .models import Brand, ShoeModels, PurchaseLinks, Colors, Styles, ShoeColors, ShoeStyles


class ShoeColorsInline(admin.StackedInline):
    model = ShoeColors
    extra = 1


class ShoeStylesInline(admin.TabularInline):
    model = ShoeStyles
    extra = 1


class ShoeModelsAdmin(admin.ModelAdmin):
    list_display = ["name", "brand"]
    fieldsets = [
        (None, {"fields": ["name"]}),
        ("Бренд", {"fields": ["brand"], "classes": ["collapse"]}),
    ]
    inlines = [ShoeColorsInline, ShoeStylesInline]


class PurchaseLinksAdmin(admin.ModelAdmin):
    list_display = ["store_name", "url", 'model', 'price', 'inexpensive']
    list_filter = ['model']
    search_fields = ["store_name"]
    fieldsets = [
        ("Название магазина", {"fields": ["store_name"]}),
        ("Остальная информация", {"fields": ["url", 'model', 'price']}),
    ]


admin.site.register(Brand)
admin.site.register(ShoeModels, ShoeModelsAdmin)
admin.site.register(PurchaseLinks, PurchaseLinksAdmin)
admin.site.register(Colors)
admin.site.register(ShoeColors)
admin.site.register(Styles)
admin.site.register(ShoeStyles)
