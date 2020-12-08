from django.db import models


# Create your models here.
class Menu(models.Model):
    image = models.ImageField(upload_to='menu/image/')
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    menu = models.ForeignKey(to=Menu, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title
