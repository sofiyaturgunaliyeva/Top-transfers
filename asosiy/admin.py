from django.contrib import admin

from.models import *

# Vazifa

# 2-topshiriq  Admin panelda club jadvaliga qidirish, davlati bo'yicha filterlash imkoniyatini qo'shing.

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ("id","nom", "davlat")
    search_fields = ("nom",)
    search_help_text = "Clubni nomi bo'yicha qidirish"
    list_filter = ("davlat",)

# admin.site.register(Club)

# 3-topshiriq  Admin panelda playerni qidirish, clubi bo'yicha filterlash,
# yangi player qo'shishda clubini ham qidirish imkoniyati bo'lsin.

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("id","ism", "club","pozitsiya")
    search_fields = ("ism","club__nom")
    search_help_text = "O'yinchining ismi v Clubni nomi bo'yicha qidirish"
    list_filter = ("club",)
    autocomplete_fields = ("club",)
    list_editable = ("ism",)

# admin.site.register(Player)

# 4-topshiriq 4. Admin panelda transferni qidirish, mavsumi bo'yicha filterlash,
# ma'lumot qo'shishda eski, yangi klublari va futbolchini qidirish imkoniyatlari bo'lsin.

@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ("id","player","tr_narx")
    search_fields = ("id","eski__nom","yangi__nom","player__ism")
    search_help_text = "O'yinchining id si , ismi , eski va yangi Clubni nomi bo'yicha qidirish"
    list_filter = ("mavsum",)
    autocomplete_fields = ("player","eski","yangi")


# admin.site.register(Transfer)

admin.site.register(HozirgiMavsum)