from django.db import models

# Create your models here.
class Cars(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tbl_car"
        verbose_name = 'Car'
        verbose_name_plural ='Cars'
