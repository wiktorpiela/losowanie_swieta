from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Voter, Scope, Person
import random
from .forms import VoterForm
from django.core.mail import EmailMessage

def home(request):

    if request.method == "POST":

        form = VoterForm(request.POST)
        if form.is_valid():
            userIP = request.META.get('HTTP_X_FORWARDED_FOR')
            email = request.POST["email"]
            name = request.POST["name"]

            scope = list(Scope.objects.filter(Q(isChosen=False) & ~Q(name__icontains=name)).values_list("name", flat=True).order_by("?"))
            chosen = random.choice(scope)
            chosen_obj = Scope.objects.get(name=chosen)
            person_obj = Person.objects.get(name=name)

            #create and save voter with proper data
            voter_obj = Voter(name=name,email=email, ip_address="abc", chosen_person=chosen_obj)
            voter_obj.save()

            #mark scope person as chosen
            chosen_obj.isChosen = True
            chosen_obj.save()

            # mark voting person as voted
            person_obj.voted = True
            person_obj.save()

            request.session["chosen"] = chosen
            return HttpResponseRedirect(request.path)

    else:
        persons = list(Person.objects.filter(voted=False).values_list("name", flat=True))
        return render(request, "home.html", {"persons":persons})
