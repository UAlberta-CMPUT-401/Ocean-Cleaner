from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Quiz


def home(request):

    quizzes = []

    quiz1 = Quiz()
    quiz1.prompt = "Do over 1000 turtles die every year from plastic waste?"
    quiz1.title = "Turtles"
    quiz1.id = 1
    quiz1.correctAnswer = True

    quizzes.append(quiz1)

    quiz2 = Quiz()
    quiz2.prompt = "Test Prompt2"
    quiz2.title = "Quiz 2"
    quiz2.id = 2
    quiz2.correctAnswer = False

    quizzes.append(quiz2)

    quiz3 = Quiz()
    quiz3.prompt = "Test Prompt3"
    quiz3.title = "Quiz 3"
    quiz3.id = 3
    quiz3.correctAnswer = True

    quizzes.append(quiz3)

    context = {'title': 'Home', 'quizzes': quizzes}  # add more stuff here

    return render(request, 'home.html', context)


def about(request):
    context = {'title': 'About'}
    # Other programs can be called here and we can output the results on the page by providing it in the dictionary
    return render(request, 'about.html', context)