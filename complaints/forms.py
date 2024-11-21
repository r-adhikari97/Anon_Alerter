from django.forms import ModelForm
from .models import PublicComplaint

class ComplaintForm(ModelForm):
    """ Class Respinsible for Validating Complaints """
    class Meta:
        model=PublicComplaint
        fields = ["complaint_title",
                  "complaint_img",
                  "complaint_description",
                  "complaint_official",
                  "complaint_address",
                  ]
