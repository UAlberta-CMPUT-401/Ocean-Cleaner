from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Quiz


def home(request):

    quizzes = []

    quiz1 = Quiz()
    quiz1.prompt = "In the ocean, plastic debris injures and kills fish, seabirds and marine mammals. " \
                   "Marine plastic pollution has impacted at least 267 species worldwide, including 86% of all sea turtle species, " \
                   "44% of all seabird species and 43% of all marine mammal species. The impacts include fatalities as a result of ingestion," \
                   " starvation, suffocation, infection, drowning, and entanglement. " \
                   "Over 1000 turtles die from plastic waste a year"
    quiz1.title = "Plastic Waste"
    quiz1.id = 1
    quiz1.correctAnswer = True

    quizzes.append(quiz1)

    quiz2 = Quiz()
    quiz2.prompt = "Sewage can adversely affect the growth, reproduction, and development of many marine animals."
    quiz2.title = "Sewage"
    quiz2.id = 2
    quiz2.correctAnswer = False

    quizzes.append(quiz2)

    quiz3 = Quiz()
    quiz3.prompt = "the increased volume of fishing activity worldwide is having a very serious effect on the health of the oceans as a whole"
    quiz3.title = "Overfishing"
    quiz3.id = 3
    quiz3.correctAnswer = True

    quizzes.append(quiz3)

    quiz4 = Quiz()
    quiz4.prompt = "As waters rapidly warm, corals lose the components that give them color and help them produce food, a process called bleaching. That slows their growth and makes them vulnerable to algae, disease, and death"
    quiz4.title = "Dying Corals"
    quiz4.id = 4
    quiz4.correctAnswer = True

    quizzes.append(quiz4)

    quiz5 = Quiz()
    quiz5.prompt = "Ocean acidification can have a dramatic effect on some calcifying species, including oysters, clams, sea urchins, shallow water corals, deep sea corals, and calcareous plankton."
    quiz5.title = "Ocean Acidification"
    quiz5.id = 5
    quiz5.correctAnswer = True

    quizzes.append(quiz5)

    quiz6 = Quiz()
    quiz6.prompt = "heavy metals, toxic substances and hazardous chemicals are used in the manufacture of electrical and electronic equipment. It’s after their useful life, when they’re landfilled, incinerated or dumped into waterways, that they prove most devastating."
    quiz6.title = "E-waste"
    quiz6.id = 6
    quiz6.correctAnswer = True

    quizzes.append(quiz6)

    context = {'title': 'Home', 'quizzes': quizzes}  # add more stuff here

    return render(request, 'home.html', context)


def about(request):
    context = {'title': 'About'}
    # Other programs can be called here and we can output the results on the page by providing it in the dictionary
    return render(request, 'about.html', context)