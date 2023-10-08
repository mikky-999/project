from django.db import models
from django.core.validators import MaxValueValidator
   

class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)],
        help_text="Enter the price as an integer (maximum 99999).")
    image = models.ImageField(default='default.jpg', upload_to='dish_pics')
    
    def __str__(self):
        return f"{self.name} dish. Price: ₦{self.price}"
