from django.db import models

class Club(models.Model):
    nom = models.CharField(max_length=30)
    davlat = models.CharField(max_length=30)
    logo = models.FileField()
    prezident = models.CharField(max_length=50, blank = True)
    murabbiy = models.CharField(max_length=50, blank=True)
    eng_qimmmat_sotuv = models.CharField(max_length=50, blank=True)
    eng_qimmat_transfer = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nom


class Player(models.Model):
    ism = models.CharField(max_length=30)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    t_yil = models.CharField(max_length=50)
    tr_narx = models.PositiveSmallIntegerField()
    pozitsiya = models.CharField(max_length=50)
    davlat = models.CharField(max_length=30, blank = True)

    def __str__(self):
        return self.ism


class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    eski = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="sotganlari")
    yangi = models.ForeignKey(Club, on_delete=models.CASCADE,related_name="olgaanlari")
    tr_narx = models.PositiveSmallIntegerField()
    taxmin_narx = models.PositiveSmallIntegerField()
    mavsum = models.CharField(max_length=6)


class HozirgiMavsum(models.Model):
    mavsum = models.CharField(max_length=10)

