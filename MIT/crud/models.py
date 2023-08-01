from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=30,blank=False,null=False)
    school = models.CharField(max_length=50,blank=False,null=False)
    email = models.EmailField()
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    TimeStamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# makemigrations creates the models

# migrate updates the models
