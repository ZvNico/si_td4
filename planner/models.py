from django.db import models


# Create your models here.
class Region(models.Model):
    nom = models.CharField(primary_key=True,
                           max_length=255,
                           verbose_name="nom")

    def __str__(self):
        return self.nom


class Departement(models.Model):
    num = models.CharField(primary_key=True,
                           max_length=2,
                           verbose_name="numéro de département",
                           help_text="le n°1 de essonne est 91")
    region = models.ForeignKey(Region,
                               on_delete=models.CASCADE,
                               verbose_name="région",
                               null=True)

    def __str__(self):
        return self.num


class Commune(models.Model):
    num = models.CharField(primary_key=True,
                           max_length=5,
                           verbose_name="numéro de commune")
    nom = models.CharField(max_length=255,
                           verbose_name="nom")
    departement = models.ForeignKey(Departement,
                                    on_delete=models.CASCADE,
                                    verbose_name="département",
                                    null=True)

    def __str__(self):
        return f"{self.nom} - {self.num}"


class Division(models.Model):
    nom = models.CharField(max_length=255,
                           verbose_name="nom")

    def __str__(self):
        return self.nom


class Accompli(models.Model):
    date_participation_debut = models.DateField(verbose_name="date début de participation")
    date_participation_fin = models.DateField(verbose_name="date fin début de participation")
    salarie = models.ForeignKey('Salarie',
                                on_delete=models.CASCADE,
                                verbose_name="salarié")
    tache = models.ForeignKey('Tache',
                              on_delete=models.CASCADE,
                              verbose_name="tâche")

    def __str__(self):
        return f"{self.salarie} - {self.tache}"


class Projet(models.Model):
    theme = models.CharField(max_length=255,
                             verbose_name="theme")
    date_debut = models.DateField(verbose_name="date début")
    date_fin = models.DateField(verbose_name="date fin")
    duree_tache = models.IntegerField(verbose_name="durée du projet  en jours")
    chef = models.ForeignKey('Salarie',
                             on_delete=models.CASCADE,
                             verbose_name="chef de projet",
                             null=True)

    def __str__(self):
        return f"{self.theme} {self.chef}"


class Tache(models.Model):
    nom = models.CharField(max_length=255,
                           verbose_name="nom")
    description = models.TextField(max_length=1000,
                                   verbose_name="description",
                                   null=True,
                                   blank=True)
    date_plus_tot = models.DateField(verbose_name="date au plus tot")
    date_plus_tard = models.DateField(verbose_name="date au plus tard")
    duree_tache = models.IntegerField(verbose_name="durée de la tache en jours")
    projet = models.ForeignKey(Projet,
                               verbose_name="projet",
                               on_delete=models.CASCADE,
                               null=True)

    def __str__(self):
        return self.nom


class Salarie(models.Model):
    nom = models.CharField(max_length=255,
                           verbose_name="nom")
    prenom = models.CharField(max_length=255,
                              verbose_name="prénom")
    competence = models.CharField(max_length=9,
                                  choices=(('aucune', 'aucune'), ('anglais', 'anglais'),
                                           ('allemand', 'allemand'), ('espagnol', 'espagnol'),
                                           ('portugais', 'portuguais'), ('arabe', 'arabe'),
                                           ('russe', 'russe'), ('chinois', 'chinois'),
                                           ('autre', 'autre')),
                                  default='aucune')

    salaire = models.FloatField()
    isChef = models.BooleanField(verbose_name="est chef de division",
                                 default=False)
    division = models.ForeignKey(Division,
                                 on_delete=models.CASCADE,
                                 verbose_name="division",
                                 null=True)
    commune = models.ForeignKey(Commune,
                                on_delete=models.CASCADE,
                                verbose_name="commune",
                                null=True)
    taches = models.ManyToManyField(Tache,
                                    verbose_name="tâches",
                                    through=Accompli)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
