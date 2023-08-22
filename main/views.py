from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LocationForm, SeasonForm, FeatureForm
from .models import Location, Season, Feature
from django.contrib.auth.decorators import login_required
from django_htmx.http import HttpResponseClientRedirect
# Create your views here.

def view_all_location(request):
    locations = Location.objects.all()
    context = {'locations':locations}
    return render(request, "home.html", context)


def location_details_view(request, pk):
    location = Location.objects.get(pk=pk)
    seasons = location.season_set.all()
    l_des = location.l_description
    l_des = l_des.split('\n')
    features = Feature.objects.filter(season__location=location)
    context = {'location': location, 'seasons':seasons, 'features':features, 'l_des':l_des}
    return render(request, "location_details.html", context)


def submit_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST, request.FILES)
        if form.is_valid():
            location = form.save()
            return redirect('create_season', l_id = location.id)
    else:
        form = LocationForm()
        context = {'location_form' : form}
        return render(request, 'location_form.html', context)

def season(request, l_id):
    if request.method == "POST":
        location_id = l_id
        form = SeasonForm(request.POST)
        if form.is_valid():
            location = Location.objects.get(pk=location_id)
            tagline = form.cleaned_data['s_tagline']
            name = form.cleaned_data['s_name']
            des = form.cleaned_data['s_description']

            season = Season.objects.create(
                s_tagline =tagline, 
                s_name=name, 
                s_description=des, 
                location=location
            )
            return redirect('create_feature', s_id=season.id)
    else:
        s_form = SeasonForm()
        context = {'season_form' : s_form}
        return render(request, 'season_form.html', context)

def create_feature(request, s_id):
    context = {'feature_form': FeatureForm, 's_id':s_id}
    return render(request, 'feature_form.html', context)

def dynamic_feature(request, s_id):
    if request.method == "POST":
        form = FeatureForm(request.POST)
        if form.is_valid():
            season = Season.objects.get(pk=s_id)
            title = form.cleaned_data['sf_title']
            des = form.cleaned_data['sf_description']

            season = Feature.objects.create(
                sf_title =title, 
                sf_description=des, 
                season=season
            )
            return HttpResponseClientRedirect("/")
    else:
        form = FeatureForm()
        return render(request, 'dynamic_form.html', {'feature_form': form, 's_id':s_id})