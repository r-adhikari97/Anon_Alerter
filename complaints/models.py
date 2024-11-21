from Demos.OpenEncryptedFileRaw import bkup_fname
from django.db import models
from users.models import User

# Create your models here.
class PublicComplaint(models.Model):
    """ Class for Modelling Public Complaints """
    POST_CHOICES = [
        ('Police', 'Police'),
        ('Civil', 'Civil'),
        ('Cidco', 'Cidco'),
    ]

    status_choices = [
        ('Investigating', 'Investigating'),
        ('Under review', 'Under review'),
        ('Resolved', 'Resolved'),
        ('Action Taken', 'Action Taken')
    ]

    complaint_id = models.AutoField(primary_key=True)
    complaint_date = models.DateTimeField(auto_now_add=True)
    complaint_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    complaint_title = models.CharField(max_length=255, null=False, blank=False)
    complaint_img = models.ImageField(null=True, blank=True, default="default.jpg")
    complaint_description = models.TextField()
    complaint_address = models.CharField(max_length=255, null=False, blank=False)
    complaint_official = models.CharField(max_length=15, choices=POST_CHOICES)
    complaint_status_choice = models.CharField(max_length=15, choices=status_choices)
    complaint_isvalid = models.BooleanField(default=False)


    def __str__(self):
        return self.complaint_title

