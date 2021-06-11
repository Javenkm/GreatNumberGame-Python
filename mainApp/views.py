from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    return render(request, "index.html")

def game(request):
    attempts = 5
    secret_number = random.randint(1, 100)

    for attempt in range(attempts):
        guess = int(input('Take a guess: '))

        if guess < secret_number:
            print('Higher...')
        elif guess > secret_number:
            print('Lower...')
        else:
            print()
            print('You guessed it! The number was ', secret_number)
            print('You guess it in', attempts, 'attempts')

            break

    if guess != secret_number:
        print()
        print('Sorry you reached the maximum number of tries')
        print('The secret_number was', secret_number)

    return render(request)

def attemptMax(request):
    if attempts > 5:
        print('Sorry you reached the maximum number of tries')
        print('The secret_number was', secret_number)

    return render(HttpResponse)