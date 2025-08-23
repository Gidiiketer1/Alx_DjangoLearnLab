from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from .models import Book
import datetime

# Custom Filter for Publication Year
class PublicationYearFilter(SimpleListFilter):
    title = 'Publication Year'
    parameter_name = 'publication_year'

    def lookups(self, request, model_admin):
        # Gather unique publication years
        years = set(
            obj.published_date.year
            for obj in model_admin.model.objects.all()
            if obj.published_date
        )
        return [(year, str(year)) for year in sorted(years)]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(published_date__year=self.value())
        return queryset


# Register Book Model with Custom Admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year', 'isbn', 'pages')
    search_fields = ('title', 'author', 'isbn')
    list_filter = (PublicationYearFilter,)  # using the custom year filter

    # Custom method to display publication year
    def publication_year(self, obj):
        return obj.published_date.year if obj.published_date else '-'
    publication_year.short_description = 'Publication Year'
