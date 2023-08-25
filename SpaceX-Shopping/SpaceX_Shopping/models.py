from django.db import models

# Create your models here.
class credential(models.Model):
    fname=models.CharField(("First Name"), max_length=50)
    lname=models.CharField(("Last Name"), max_length=50)
    email=models.CharField(("Email"), max_length=50)
    password=models.CharField(("Password"), max_length=50)

    def __str__(self):
        return self.email

class cart(models.Model):
    product_id=models.CharField(("id"), max_length=50)
    user=models.CharField(("user"), max_length=50)
    email=models.CharField(("Email"), max_length=50)
    photo=models.CharField(("photo"), max_length=50)
    name=models.CharField(("name"), max_length=50)
    size=models.CharField(("size"), max_length=50)
    quantity=models.IntegerField(("quantity"), default=0)
    

    def __str__(self):
        return self.user