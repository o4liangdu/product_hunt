from django.db import models
from django.contrib.auth.models import User

# Create your models here.做完models之后migrate
class Product(models.Model):
    title=models.CharField(default='这是app标题',max_length=50)
    intro = models.TextField(default='这是app介绍')
    url = models.CharField(default='Http://',max_length=100)
    icon = models.ImageField(default='1.png',upload_to='images/')
    image = models.ImageField(default='default.jpg',upload_to='images/')

    votes=models.IntegerField(default=1)
    pub_date=models.DateTimeField()
    hunter=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title