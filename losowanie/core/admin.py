from django.contrib import admin
from .models import Scope, Voter, Person

class Timestamp(admin.ModelAdmin):
    readonly_fields = ("timestamp",)

admin.site.register(Scope)
admin.site.register(Person)
admin.site.register(Voter, Timestamp)