from django.contrib import admin
from .models import Advertisement

class AdvetisementAdmin(admin.ModelAdmin):
    list_display = ['id','title','description', 'price', 'auction', 'created_date','updated_date']
    list_filter = ['auction','created_at']

    actions = ['make_auction_as_false', 'make_auction_as_true']

    @admin.action(description = 'Убрaть возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction = False)

    @admin.action(description = 'Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction = True)



    fieldsets = (
        ('Общее', {
            'fields' : ('title' ,'description'),
        }),
        ('Финанасы' , {
            'fields' : ('price', 'auction'),
            'classes' : ['collapse']
        }),
    )




admin.site.register(Advertisement, AdvetisementAdmin)

# Register your models here. Добавить возможность торга
