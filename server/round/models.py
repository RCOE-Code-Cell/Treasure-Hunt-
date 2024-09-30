from django.db import models

class Groups(models.Model):
    group_name = models.CharField( max_length=50)
    leader_name = models.CharField( max_length=50)
    group_email = models.EmailField( max_length=254)
    round1 = models.BooleanField(default=False)  #digital round 25 teams 
    round2 = models.BooleanField(default=False)  #20 teams 
    round3 = models.BooleanField(default=False)  #15 teams 
    round4 = models.BooleanField(default=False)  #5 teams
    winner = models.BooleanField(default=False)  #1 teams

    def __str__(self) :
        return self.group_name