from django.shortcuts import render
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
# from django.views.generic.edit import DeleteView
from .forms import NotesForm
from .models import Notes

class NotesDeleteView(DeleteView):
     model = Notes
     success_url = '/smart/notes'
     template_name = 'notes/notes_delete.html'
class NotesUpdateView(UpdateView):
     model = Notes
     form_class = NotesForm
     success_url = '/smart/notes'
class NotesCreateView(CreateView):
     model = Notes
     # fields = ['title', 'text']
     form_class = NotesForm
     success_url = '/smart/notes'
class NotesListView(ListView):
     model = Notes
     context_object_name = "notes"
     template_name = "notes/notes_list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'

    
# def details(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")
#     return render(request, 'notes/notes_detail.html', {
#         'note': note
#     })