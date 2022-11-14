from django.contrib import admin
from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "balance"]
    list_display_links = ["name"]
    filter = ["category"]
    search_fields = ["name", "description"]
    exclude = []
    readonly_fields = ["created_at", "updated_at"]


admin.site.register(Product, ProductAdmin)
