from django.urls import path
from . import views
app_name = 'questions'

urlpatterns = [
    path('',views.QuestionListView.as_view(),name='list'),
    path('<int:pk>/',views.QuestionDetailView.as_view(),name='detail'),
    path('create/',views.QuestionCreateView.as_view()),
    path('update/<int:pk>/',views.QuestionUpdateView.as_view()),
    path('delete/<int:pk>/',views.QuestionDeleteView.as_view()),
]