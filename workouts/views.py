from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt


from . import models
from django.contrib.auth import logout
from django.shortcuts import redirect

#Date and time for timer
from django.utils import timezone
import datetime
# Create your views here.

from django.http import JsonResponse
from datetime import datetime, timedelta
import json
from .models import Event

def countdown_timer(request):
    event = Event.objects.first()
    if event:
        time_remaining = event.event_date - timezone.now()
        total_seconds = time_remaining.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        data = {
            'name': event.name,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        }
    else:
        data = {
            'name': "No Event",
            'hours': 0,
            'minutes': 0,
            'seconds': 0
        }
    return render(request, 'myapp.html', {'data': data})




@csrf_exempt  # Only use this decorator if necessary and if CSRF protection is properly handled
def set_time(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            time_to_set = data.get('time')
            # Validate the time format and save it to your database or variable
            # For demonstration, assuming it's valid and saving to a variable
            stored_time = time_to_set  # Replace with actual saving logic

            return JsonResponse({'stored_time': stored_time})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def current_datetime(request):
    current_time = datetime.now()
    added_time = current_time + timedelta(minutes=5)
    
    return JsonResponse({
        'added_time': added_time.strftime('%Y-%m-%d %H:%M:%S')
    })

def home(request):
    workouts = models.Workout.objects.all()
    current_time = timezone.now()
    current_date = datetime.date.today()
    context = {
        'workouts': workouts,
        'current_time': current_time,
        'current_date': current_date,
    }
    return render(request, "workouts/home.html", context)
    

class WorkoutListView(ListView):
    model = models.Workout
    template_name = 'workouts/home.html'
    context_object_name = 'workouts'



class WorkoutDetailView(DetailView):
    model = models.Workout

class WorkoutCreateView(LoginRequiredMixin, CreateView):
    model = models.Workout
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class WorkoutUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Workout
    fields = ['title', 'description']

    def test_func(self):
        workout = self.get_object()
        return self.request.user == workout.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class WorkoutDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Workout
    success_url = reverse_lazy('workouts-home')

    def test_func(self):
        workout = self.get_object()
        return self.request.user == workout.author
    

def about(request):
    return render(request, "workouts/about.html", {'title': 'about us page'})


def logout_view(request):
    logout(request)
 
    return redirect('user-login2') 

