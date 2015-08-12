from django.contrib import admin

from main.models import State, StateCapital, City

# Register your models here.
#class StateCapitalAdmin(admin.ModelAdmin):
	#list_display = ('name', 'abbreviation', 'capital')
	#search_fields = ('name',)
	#inlines = [StateCapitalInline]

class StateAdmin(admin.ModelAdmin):
	list_display = ('name', 'abbreviation',)
	#list_display = ('name', 'abbreviation', 'capital')
	search_fields = ('name',)
	#inlines = [StateCapitalInline]

admin.site.register(State, StateAdmin)
admin.site.register(StateCapital)
admin.site.register(City)
