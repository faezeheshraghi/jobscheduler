from django.db import models

# Create your models here.
class basket(models.Model):
    basket_id = models.CharField(max_length=250, blank=True)
    # user = models.OneToOneField(Account, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100,unique=True, blank=True)
    subject = models.CharField(max_length=100, blank=True)
    date_add =  models.DateTimeField(auto_now_add=True)
    count = models.IntegerField()

    def __str__(self):
        return self.email
    class Meta:
        ordering = ['date_add']

class keepemail(models.Model):
    email = models.EmailField(max_length=100,unique=True, blank=True)

    def __str__(self):
        return self.email
