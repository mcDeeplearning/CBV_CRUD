from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Question
from django.urls import reverse_lazy
# Create your views here.

class QuestionListView(ListView):
    model = Question
    
class QuestionDetailView(DetailView):
    model = Question
    
class QuestionCreateView(CreateView):
    model = Question
    fields = ('title','answerA','answerB')

class QuestionUpdateView(UpdateView):
    model = Question
    fields = ('title','answerA','answerB')

class QuestionDeleteView(DeleteView):
    model = Question
    success_url = reverse_lazy('questions:list')