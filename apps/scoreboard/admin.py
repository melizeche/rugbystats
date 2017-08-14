from django.contrib import admin
from .models import Team, Championship, Round, Match

# class MatchAdmin(admin.ModelAdmin):
#     list_display =


class MatchInline(admin.StackedInline):
    model = Match


class RoundInline(admin.StackedInline):
    model = Round


class ChampionshipAdmin(admin.ModelAdmin):
    inlines = (RoundInline,)


class RoundAdmin(admin.ModelAdmin):
    list_display = ('name', 'championship')
    inlines = (MatchInline,)

admin.site.register(Team)
admin.site.register(Championship, ChampionshipAdmin)
admin.site.register(Round, RoundAdmin)
admin.site.register(Match)
