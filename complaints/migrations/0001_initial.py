# Generated by Django 5.1.1 on 2024-11-21 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PublicComplaint",
            fields=[
                ("complaint_id", models.AutoField(primary_key=True, serialize=False)),
                ("complaint_date", models.DateTimeField(auto_now_add=True)),
                ("complaint_title", models.CharField(max_length=255)),
                (
                    "complaint_img",
                    models.ImageField(
                        blank=True, default="default.jpg", null=True, upload_to=""
                    ),
                ),
                ("complaint_description", models.TextField()),
                ("complaint_address", models.CharField(max_length=255)),
                (
                    "complaint_official",
                    models.CharField(
                        choices=[
                            ("Police", "Police"),
                            ("Civil", "Civil"),
                            ("Cidco", "Cidco"),
                        ],
                        max_length=15,
                    ),
                ),
                ("complaint_status_choice", models.CharField(max_length=15)),
                ("complaint_isvalid", models.BooleanField(default=False)),
            ],
        ),
    ]
