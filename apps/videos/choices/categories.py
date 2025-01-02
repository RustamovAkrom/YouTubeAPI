from django.utils.translation import gettext_lazy as _
from django.db.models import TextChoices


class CategoryChoice(TextChoices):
    MUSIC = "music", _("Music")
    GAMING = "gaming", _("Gaming")
    BEAUTY_AND_FASHION = "beauty & fashion", _("Beauty & Fashion")
    VLOGGING = "vlogging", _("Vlogging")
    EDUCATION = "education", _("Education")
    COMEDY = "comedy", _("Comedy")
    SCIENCE_AND_TECHNOLOGY = "science & technology", _("Science & Technology")
    TRAVEL = "travel", _("Travel")
    FOOD = "food", _("Food")
    HELTH_AND_WELLNESS = "helth & wellness", _("Helth & Wellness")
    DIY_AND_HOW_TO = "DIY & how-to", _("Diy & How-to")
    NEWS_AND_POLITICS = "news & politics", _("News & Politics")
    SPORTS = "sports", _("Sports")
    ENTERTAINMENT = "entertainment", _("Entertainment")
    PETS_AND_ANIMALS = "pets & animals", _("Pets & Animals")
    BUSSINESS_AND_PARENTING = "bussiness & parenting", _("Bussiness & Parenting")
    CARS_AND_VEHICLES = "cars & vehicles", _("Cars & Vehicles")
    ART_AND_DESIGN = "art & design", _("Art & Design")
    SPIRITUAL_AND_RELIGIOUS = "spiritual & religious", _("Spiritual & Religious")
    