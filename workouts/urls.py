from django.urls import path
from . import views
#from . views import logout_view

'app/model_viewtype'
'workout/workout_detail.html'

urlpatterns = [
    path('', views.WorkoutListView.as_view(), name="workouts-home"),
    path('workout/<int:pk>/', views.WorkoutDetailView.as_view(), name="workouts-detail"),
    path('workout/create', views.WorkoutCreateView.as_view(), name="workouts-create"),
    path('workout/<int:pk>/update/', views.WorkoutUpdateView.as_view(), name="workouts-update"),
    path('workout/<int:pk>/delete/', views.WorkoutDeleteView.as_view(), name="workouts-delete"),
    path('about/', views.about, name="workouts-about"),
    
]
