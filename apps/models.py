from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, TextChoices


class User(AbstractUser):
    class JobChoiceField(TextChoices):
        FULL_STACK_DEVELOPER = "full stack developer", "Full Stack Developer"
        DESIGNER = "designer", "Designer"

    phone = CharField(max_length=12, default="998991234567")
    mobile = CharField(max_length=12, default="998997654321")
    address = CharField(max_length=255, default="Samarqand , Oq oltin")
    job = CharField(max_length=255, choices=JobChoiceField.choices, default=JobChoiceField.FULL_STACK_DEVELOPER)

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"


class Category(Model):
    name = CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.name

# center:
#     qahramon
#     daler
#     daniyor
#
#      1-17 talik
#
#
# left:
#     yulduz
#     behruz
#     mahsud
#     sarvinoz
#
#     2-(7,5)
#
# right:
#     umar
#     hasan
#     lochin
#
#     3-(13,3)
