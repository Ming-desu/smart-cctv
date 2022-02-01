from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  sex = models.CharField(
    choices=[
      ('Male', 'Male'),
      ('Female', 'Female')
    ],
    max_length=10
  )
  role = models.CharField(
    max_length=10,
    choices=[
      ('Admin', 'Admin'),
      ('Operator', 'Operator')
    ],
    default='Operator'
  )

  def full_name(self):
    return self.user.first_name + ' ' + self.user.last_name

@receiver(post_save, sender=User)
def post_save_receiver(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
  instance.profile.save()
