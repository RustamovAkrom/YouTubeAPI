from django.db.models import TextChoices


class CategoryChoice(TextChoices):
    MUSIC = "music"
    GAMING = "gaming"
    BEAUTY_AND_FASHION = "beauty & fashion"
    VLOGGING = "vlogging"
    EDUCATION = "education"
    COMEDY = "comedy"
    SCIENCE_AND_TECHNOLOGY = "science & technology"
    TRAVEL = "travel"
    FOOD = "food"
    HELTH_AND_WELLNESS = "helth & wellness"
    DIY_AND_HOW_TO = "DIY & how-to"
    NEWS_AND_POLITICS = "news & politics"
    SPORTS = "sports"
    ENTERTAINMENT = "entertainment"
    PETS_AND_ANIMALS = "pets & animals"
    BUSSINESS_AND_PARENTING = "bussiness & parenting"
    CARS_AND_VEHICLES = "cars & vehicles"
    ART_AND_DESIGN = "art & design"
    SPIRITUAL_AND_RELIGIOUS = "spiritual & religious"
    