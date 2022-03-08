from django.db import models

# Create your models here.
class date(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Addition(date):
    number1  = models.IntegerField(null = False, blank = False)
    number2  = models.IntegerField(null = False, blank = False)
    answer  = models.IntegerField(blank = True)
    is_available = models.BooleanField(default= True)

    def __str__(self):
        return str(self.number1) +" "+ str(self.number2) +" "+ str(self.created_at)

    def save(self, *args, **kwargs):
        self.answer = self.number1 + self.number2
        self.is_available = True
        super(Addition, self).save(*args, **kwargs)