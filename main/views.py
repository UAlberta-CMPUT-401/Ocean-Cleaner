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

    quiz4 = Quiz()
    quiz4.prompt = "Test Prompt4"
    quiz4.title = "Quiz 4"
    quiz4.id = 4
    quiz4.correctAnswer = True

    quizzes.append(quiz4)

    quiz5 = Quiz()
    quiz5.prompt = "Test Prompt5"
    quiz5.title = "Quiz 5"
    quiz5.id = 5
    quiz5.correctAnswer = True

    quizzes.append(quiz5)

    quiz6 = Quiz()
    quiz6.prompt = "Test Prompt6"
    quiz6.title = "Quiz 6"
    quiz6.id = 6
    quiz6.correctAnswer = True

    quizzes.append(quiz6)

    context = {'title': 'Home', 'quizzes': quizzes}  # add more stuff here

    return render(request, 'home.html', context)


def about(request):
    context = {'title': 'About'}
    # Other programs can be called here and we can output the results on the page by providing it in the dictionary
    return render(request, 'about.html', context)