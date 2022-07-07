from django.contrib import admin

from .models import *


# Register your models here.


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("nom",)


@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ("num",)


@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):
    list_display = ("num", "nom")


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ("id", "nom")


@admin.register(Accompli)
class AccompliAdmin(admin.ModelAdmin):
    list_display = ("id", "salarie", "tache")


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ("id", "date_fin", "date_debut", "chef")


@admin.register(Tache)
class TacheAdmin(admin.ModelAdmin):
    list_display = ("id", "nom")


@admin.register(Salarie)
class SalarieAdmin(admin.ModelAdmin):
    list_display = ("id", "nom", "prenom", "salaire")
