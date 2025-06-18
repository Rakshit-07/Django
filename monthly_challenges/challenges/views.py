from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

month_name = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for atleast 20 minutes every day!",
    "march": "Learn Django for atleast 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for atleast 20 minutes every day!",
    "june": "Learn Django for atleast 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for atleast 20 minutes every day!",
    "october": "Learn Django for atleast 20 minutes every day!",
    "november": "Eat no meat for the entire month!",
    "december": "Walk for atleast 20 minutes every day!"
}

def index(request):
    month_total = list(month_name.keys())
    list_items = ''
    # for month in month_total:
    #    list_items +=  f"<li><a href=\"{reverse("monthly-chal", args=[month])}\">{month}</a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    return render(request, "challenges/index.html")


def monthly_challenge_num_type(request, month):
    mon_name = list(month_name.keys())
    if month > len(mon_name):
        return HttpResponseNotFound('Enter valid month name!')
    else:
        mon = mon_name[month - 1]
        redirect_mon = reverse("monthly-chal", args=[mon])
        return HttpResponseRedirect(redirect_mon)

def monthly_challenge(request, month):
   try:
       challenge_text = month_name[month]
    #    response_data = render_to_string("challenges/challenge.html")
    #    return HttpResponse(response_data)
       return render(request, "challenges/challenge.html", {
           "text" : challenge_text,
           "month" : month
       })

   except:
       return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    