from django.db import models

аpp_label = 'firstapp'


class Food(models.Model):
    type = models.TextField()
    count = models.TextField()
    weight = models.TextField()
    name = models.TextField()
    structure = models.TextField()
    image = models.TextField()
    price = models.TextField()
    text = models.TextField()

    class Meta  :
        db_table = 'food'

class Cart(models.Model):
    user = models.TextField()
    product = models.TextField()
    total_price = models.TextField()

    class Meta  :
        db_table = 'cart'

class User(models.Model):
    username = models.TextField()
    email = models.TextField()

    class Meta  :
        db_table = 'user'



class Post:
    pass
