from django.contrib import admin
from .models import Meetup,Location,Participant
# Register your models here.
class MeetupAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','date')
    list_filter = ('location','date')

admin.site.register(Meetup,MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)

