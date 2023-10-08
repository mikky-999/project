from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from base.models import Dish
from django.core.validators import MaxValueValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Creates a one to one interaction with the user from the db
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    address = models.CharField(max_length=100, default="")
    phone_number = models.CharField(max_length=11, default="23481234567")
    date_joined = models.DateTimeField(default=timezone.now)

    image = models.ImageField(default='default.jpg', upload_to='profile_pics')  # default is default.jpg, uploaded pics go to profile_pics

    
    def __str__(self):
        return f"""This profile belongs to {self.user.profile.name} {self.user.profile.surname}. 
            This user joined on {self.user.profile.date_joined}, 
            and has been an amaaazing customer ever since."""
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)   # Overiding the save option so we can scale down profile pics  sizes to 300X300 before the image is saved

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Order(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = price = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)],
        help_text="Enter the price as an integer (maximum 99999).")