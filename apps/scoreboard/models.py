from django.db import models
from django.utils.translation import ugettext as _
from .app_settings import *


class Team(models.Model):
    name = models.CharField(max_length=50)
    shortname = models.CharField(_('Short Name'), max_length=50)
    logo = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.name


class Championship(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Round(models.Model):
    championship = models.ForeignKey('Championship')
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Match(models.Model):
    championship_round = models.ForeignKey('Round')
    team1 = models.ForeignKey(
        'Team', related_name='local', verbose_name='Team 1')
    scoret1 = models.SmallIntegerField('Score Team 1', default=0)
    trybonust1 = models.BooleanField('Try Bonus', default=False)
    team2 = models.ForeignKey('Team', related_name='visitor')
    scoret2 = models.SmallIntegerField('Score Team 2', default=0)
    trybonust2 = models.BooleanField('Try Bonus', default=False)
    date = models.DateField(_('Date'), blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.team1.shortname + ' vs ' + self.team2.shortname + " - " + self.championship_round.name

    @property
    def winner(self):
        if not self.scoret1 == self.scoret2:
            return self.team1 if self.scoret1 > self.scoret2 else self.team2
        return None

    @property
    def is_draw(self):
        return self.scoret1 == self.scoret2

    @property
    def loser(self):
        if not self.is_draw:
            return self.team1 if self.scoret1 < self.scoret2 else self.team2
        return None

    @property
    def loser_bonus(self):
        if self.loser:
            if abs(self.scoret1 - self.scoret2) <= 7:
                return True
        return False

    @property
    def points(self):
        if not self.is_draw:
            if self.winner == self.team1:
                t1 = WIN_POINTS
                t2 = LOSE_POINTS + LOSING_BONUS_POINTS if self.loser_bonus else 0
            else:
                t2 = WIN_POINTS
                t1 = LOSE_POINTS + LOSING_BONUS_POINTS if self.loser_bonus else 0
        else:
            t1, t2 = DRAW_POINTS, DRAW_POINTS
        t1 += TRY_BONUS_POINTS if self.trybonust1 == True else 0
        t2 += TRY_BONUS_POINTS if self.trybonust2 == True else 0
        return t1, t2
