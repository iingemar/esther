from django.contrib import admin
from app.models import Food, Category, RecipeRow, Commentator


class RecipeInline(admin.StackedInline):
    model = RecipeRow

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', )
    filter_horizontal = ('categories',)
    inlines = [
        RecipeInline,
        ]

admin.site.register(Category)
admin.site.register(Commentator)
admin.site.register(Food, FoodAdmin)