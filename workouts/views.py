from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from . import models
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.
def home(request):
    workouts = models.Workout.objects.all()
    context = {
        'workouts': workouts
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