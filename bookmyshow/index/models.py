from django.db import models

class cities(models.Model):
    city = models.CharField(max_length = 500)
    city_name = models.CharField(max_length = 20)
    
