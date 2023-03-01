from django.db import models
from django.core.validators import FileExtensionValidator
import os


class Country(models.Model):
    country_code = models.CharField(verbose_name='Country', max_length=2)


class City(models.Model):
    city = models.CharField(verbose_name="City", max_length=50)
    country = models.ForeignKey('webapp.Country', on_delete=models.CASCADE)


class Club(models.Model):
    name = models.CharField(verbose_name="Club title", max_length=50, null=True, blank=True)
    EGDName = models.CharField(verbose_name='EGDName', max_length=6, null=True, blank=True)

    def __str__(self):
        return f'{self.id}. {self.name} - {self.EGDName}'


class Game(models.Model):
    black = models.ForeignKey('webapp.Player', on_delete=models.CASCADE, related_name="black_player", null=True, blank=True)
    white = models.ForeignKey('webapp.Player', on_delete=models.CASCADE, related_name="white_player", null=True, blank=True)
    result = models.CharField(verbose_name="Result", max_length=10, null=True, blank=True)
    black_score = models.PositiveIntegerField(verbose_name="Black score")
    white_score = models.PositiveIntegerField(verbose_name='White score')
    board_number = models.PositiveIntegerField(verbose_name="BoardNumber", default=0)
    date = models.DateTimeField(verbose_name='Date')
    tournament = models.ForeignKey('webapp.Tournament', on_delete=models.CASCADE)
    round_num = models.PositiveIntegerField(verbose_name="Round")

    def __str__(self):
        return f'{self.id}. {self.black} : {self.white} = {self.result}'


class Tournament(models.Model):
    name = models.CharField(verbose_name="Tournament name", max_length=50, null=True, blank=True)
    city = models.ForeignKey('webapp.City', on_delete=models.CASCADE, null=True, blank=True)
    board_size = models.PositiveIntegerField(verbose_name="Board size", default=19)
    rounds = models.PositiveIntegerField(verbose_name='Total rounds')

    def __str__(self):
        return f'{self.id}. {self.name} - {self.board_size}'


class Player(models.Model):
    first_name = models.CharField(verbose_name="First name", max_length=50, blank=True, null=True)
    last_name = models.CharField(verbose_name="Last name", max_length=50, blank=True, null=True)
    age = models.PositiveIntegerField(verbose_name='Age', blank=True, null=True)
    clubs = models.ManyToManyField('webapp.Club', related_name='players')
    country = models.ForeignKey('webapp.Country', on_delete=models.CASCADE)
    tournaments = models.ManyToManyField('webapp.Tournament', through='webapp.PlayerInTournament')

    def __str__(self):
        return f'{self.id} - {self.last_name}: {self.first_name}'


class PlayerInTournament(models.Model):
    game_id = models.PositiveIntegerField(verbose_name="Game id")
    player = models.ForeignKey('webapp.Player', on_delete=models.CASCADE)
    tournament = models.ForeignKey('webapp.Tournament', on_delete=models.CASCADE)
    GoLevel = models.CharField(verbose_name='GoLevel', max_length=3 , blank=True, null=True)
    rating = models.PositiveIntegerField(verbose_name='Rating', blank=True, null=True)


class File(models.Model):
    file = models.FileField(upload_to= 'files/',null=True,validators=[FileExtensionValidator(allowed_extensions=['xml'], message=['Загрузите файл в формате XML'], code='invalid_extension')])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def delete(self,*args,**kwargs):
        if os.path.isfile(self.file.path):
            os.remove(self.file.path)
        super(File, self).delete(*args, **kwargs)
