from django.db import models
from Person.models import Person
from datetime import datetime
# Create your models here.
class Event(models.Model):
    category_list=(
        ("M",'Musique'),
        ('C','Cinema'),
        ('S','Sport'),
    )
    title=models.CharField(max_length=50)
    description =models.TextField()
    image=models.ImageField(null=True,blank=True,upload_to="images/")
    category=models.CharField(max_length=20,choices=category_list)
    state=models.BooleanField(default=False)
    nbe_participant=models.IntegerField(default=0)
    evt_date=models.DateTimeField()
    creation_date=models.DateField(auto_now_add=True)
    update_date=models.DateField(auto_now=True)
    organizer=models.ForeignKey(
        Person,
        on_delete=models.SET_NULL,
        null=True
    )
    participant=models.ManyToManyField(
        Person,
        related_name="paticipants"
    )
    class Meta:
        contraints=[
            models.CheckConstraint(check=models.Q(
                evt_date__gt=datetime.now()
            ))
        ]
class Participants(models.Model):
    person=models.ForeignKey(Person,on_delete=models.CASCADE)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    participation_date=models.DateTimeField(datetime.now(),auto_now_add=True)
    class Meta:
        unique_together=['person','event']