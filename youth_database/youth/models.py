from django.db import models

class Youth(models.Model):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]

    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    quarter = models.CharField(max_length=20)
    birthday = models.CharField(max_length=10)  # Format: DD-MM-YYYY or MM-YYYY
    field_of_study = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    talent_1 = models.CharField(max_length=50)
    talent_2 = models.CharField(max_length=50, blank=True)
    talent_3 = models.CharField(max_length=50, blank=True)
    gift_1 = models.CharField(max_length=50, blank=True)
    gift_2 = models.CharField(max_length=50, blank=True)
    gift_3 = models.CharField(max_length=50, blank=True)
    orphant = models.BooleanField(default=False)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.name