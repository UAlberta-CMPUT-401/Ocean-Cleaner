from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Quiz


def home(request):

    quizzes = []

    firstQuiz = Quiz.objects.get(pk=1)
    quizzes.append(firstQuiz)

    secondQuiz = Quiz.objects.get(pk=2)
    quizzes.append(secondQuiz)

    thirdQuiz = Quiz.objects.get(pk=3)
    quizzes.append(thirdQuiz)

' UNCOMMENT OUT WHEN WE HAVE 4th, 5th, AND 6th IMAGES + QUIZZES

'''    fourthQuiz = Quiz.objects.get(pk=4)
    quizzes.append(fourthQuiz)

    fifthQuiz = Quiz.objects.get(pk=5)
    quizzes.append(fifthQuiz)

    sixthQuiz = Quiz.objects.get(pk=6)
    quizzes.append(sixthQuiz) '''

    context = {'title': 'Home', 'quizzes': quizzes}  # add more stuff here

    return render(request, 'home.html', context)


def about(request):
    context = {'title': 'About'}
    # Other programs can be called here and we can output the results on the page by providing it in the dictionary
    return render(request, 'about.html', context)