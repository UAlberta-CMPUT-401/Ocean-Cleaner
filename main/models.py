from django.db import models

'''
    The Quiz class contains the data related to a quiz object.
    
    Quiz data is referenced when the User interacts with a quiz element on the main page.
'''


class Quiz(models.Model):

    title = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    prompt = models.CharField(max_length=200)

    #choice1 = models.CharField(max_length=200)
    #choice2 = models.CharField(max_length=200)
    #choice3 = models.CharField(max_length=200)
    correctAnswer = models.BooleanField(default=False)
    userAnswer = models.BooleanField(default=None)

    def __str__(self):
        return self.prompt

    def isUserCorrect(self):
        return self.userAnswer == self.correctAnswer



