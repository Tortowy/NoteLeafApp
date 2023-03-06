from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView,UpdateView,CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Note
from django.utils import timezone

from .forms import NoteUpdateForm
# Create your views here.



class NotesListView(ListView):
    template_name = "notes/list_view.html"
    queryset = Note.objects.all()



@login_required(login_url="/users/login_user/")
def notes_passed_by_method(request):
    query_set = Note.objects.all()
    loggedUser = request.user

    proper_set = Note.objects.filter(owner_id=loggedUser)
    for note in proper_set:
        if len(note.content)>150:
            note.content = note.content[:150]
            note.content = note.content + str("...")

    context = {
        "object_list" : proper_set
    }

    return render(request,"notes/list_view.html",context)


class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self,request,*args,**kwargs):

        if not self.request.user.is_authenticated:
            messages.error(request,("You have to log in to be able to view notes!"))
            return redirect('/users/login_user')

        flag = False

        if str(request.path) == '/notes/create_view/':
            flag = True

        proper_set = Note.objects.filter(owner_id=request.user.id)
        for i in proper_set:
            if str(i.owner_id) == str(request.user) and str(i.id) == str(self.kwargs.get('id')):
                flag = True
        if flag == False:
            messages.error(request,("This note does not exist!"))
            return redirect('/notes')
        return super(UserAccessMixin,self).dispatch(request,*args,**kwargs)



class NoteDetailView(UserAccessMixin,DetailView,LoginRequiredMixin):
    login_url = "/users/login_user/"
    template_name = 'notes/detail_view.html'
    model = Note
    permission_required = 'notes.view_notes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Note,id=id_)


class NoteUpdateView(UserAccessMixin,UpdateView,LoginRequiredMixin):
    login_url = "/users/login_user/"
    model = Note
    permission_required = 'dupa'
    form_class = NoteUpdateForm
    template_name = 'notes/edit_view.html'
    queryset = Note.objects.all()

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Note,id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class NoteCreateView(UserAccessMixin,CreateView,LoginRequiredMixin):
    login_url = "/users/login_user/"
    model = Note
    permission_required = 'dup'
    form_class = NoteUpdateForm




    template_name = 'notes/edit_view.html'
    queryset = Note.objects.all()


    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Note,id=id_)

    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     return super().form_valid(form)

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner_id = user if user else None
        return super(NoteCreateView, self).form_valid(form)