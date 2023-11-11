from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Voter, Scope, Person
import random
from .forms import VoterForm
from django.core.mail import EmailMessage
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.views import View
from django.contrib import messages


class Home(View):

    def get(self, request, *args, **kwargs):
        persons = list(Person.objects.filter(voted=False).values_list("name", flat=True))
        return render(request, "home.html", {"persons":sorted(persons)})
    
    def post(self, request):
        form = VoterForm(request.POST)

        if form.is_valid():
            userIP = request.META.get('HTTP_X_FORWARDED_FOR')
            ip = userIP.split(',')[0] if userIP else request.META.get('REMOTE_ADDR')

            email = request.POST["email"]
            name = request.POST["name"]

            scope = list(Scope.objects.filter(Q(isChosen=False) & ~Q(name__icontains=name)).values_list("name", flat=True).order_by("?"))

            #handle case if scope is empty
            try:
                chosen = random.choice(scope)
            except IndexError:
                alreadyVoted = "Brak osób do wylosowania!"
                persons = list(Person.objects.filter(voted=False).values_list("name", flat=True))
                return render(request, "home.html", {"persons":sorted(persons), "alreadyVoted":alreadyVoted})

            chosen_obj = Scope.objects.get(name=chosen)
            
            #get Person object and handle exception if doesnt exists
            try:
                person_obj = Person.objects.get(name=name, voted=False)
            except ObjectDoesNotExist:
                alreadyVoted = "Ta osoba już wylosowała!"
                persons = list(Person.objects.filter(voted=False).values_list("name", flat=True))
                return render(request, "home.html", {"persons":sorted(persons), "alreadyVoted":alreadyVoted})

            #create and save voter with proper data
            voter_obj = Voter(name=name,email=email, ip_address=ip, chosen_person=chosen_obj)
            voter_obj.save()

            #mark scope person as chosen
            chosen_obj.isChosen = True
            chosen_obj.save()

            # mark voting person as voted
            person_obj.voted = True
            person_obj.save()

            #send email confirmation
            email = EmailMessage(
                f"Świąteczne losowanie",
                f"Cześć {name}, <br> Wylosowana przez Ciebie osoba to: <strong>{chosen}</strong>.<br>"
                "Wesołych Świąt!",
                settings.DEFAULT_FROM_EMAIL,
                [email]
            )
            email.content_subtype="html"
            email.send()

            #request.session["chosen"] = chosen
            messages.info(request, chosen)
            return HttpResponseRedirect(request.path)
