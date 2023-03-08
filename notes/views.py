from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
# from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

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

     def form_valid(self, form):
          self.object = form.save(commit=False)
          self.object.user = self.request.user
          self.object.save()
          return HttpResponseRedirect(self.get_success_url())
class NotesListView(LoginRequiredMixin, ListView):
     model = Notes
     context_object_name = "notes"
     template_name = "notes/notes_list.html"
     login_url = '/admin/'

     def get_queryset(self):
          return self.request.user.notes.all()

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