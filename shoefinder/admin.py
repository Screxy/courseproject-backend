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
        (None, {"fields": ["name", "brand"]}),
    ]
    inlines = [ShoeColorsInline]


class PurchaseLinksAdmin(admin.ModelAdmin):
    list_display = ["store_name", "url", "display_model_name", "price", "inexpensive"]
    list_display_links = ["store_name", "url"]
    list_filter = ["model"]
    search_fields = ["store_name"]
    fieldsets = [
        ("Название магазина", {"fields": ["store_name"]}),
        ("Остальная информация", {"fields": ["url", "model", "price"]}),
    ]

    def display_model_name(self, obj):
        return obj.model.name

    display_model_name.short_description = "Модель обуви"


class ShoeStylesAdmin(admin.ModelAdmin):
    list_display = ['display_styles', 'display_shoes']
    list_display_links = ['display_styles', 'display_shoes']
    filter_horizontal = ['shoe', 'style']
    list_filter = ['shoe', 'style']
    def display_styles(self, obj):
        return ", ".join([str(style) for style in obj.style.all()])

    def display_shoes(self, obj):
        return ", ".join([str(shoe) for shoe in obj.shoe.all()])

    display_styles.short_description = 'Стили'
    display_shoes.short_description = 'Кроссовки'


class ShoeColorAdmin(admin.ModelAdmin):
    list_display = ['color', 'shoe']
    list_filter = ['color']
    search_fields = ["shoe"]


admin.site.register(Brand)
admin.site.register(ShoeModels, ShoeModelsAdmin)
admin.site.register(PurchaseLinks, PurchaseLinksAdmin)
admin.site.register(Colors)
admin.site.register(ShoeColors, ShoeColorAdmin)
admin.site.register(Styles)
admin.site.register(ShoeStyles, ShoeStylesAdmin)
