from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import Collection, Piece
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import authenticate,login
# Create your views here.

class index(generic.ListView):
    template_name = 'genre/genretemplate.html'
    def get_queryset(self):
        return Collection.objects.all()

# def index(request):
#     all_collection = Collection.objects.all()
#     context = {
#         "all_collection": all_collection
#     }
#     return render(request,"genre\\genretemplate.html",context)

class details(generic.DetailView):
    model = Collection
    template_name = "genre/detailtemplate.html"


class UserFormView(View):
    form_class = UserForm
    template_name = 'genre/formtemplate.html'

# def details(request,genre_id):
#     citem = Collection.objects.get(pk=genre_id)
#     pitem = Piece.objects.filter(collection=citem)

#     context = {
#     "pitem": pitem
#     }
#     return render(request,"genre\\detailtemplate.html",context)


def get(self,request):
    form = self.form_class(None)
    return render(request,self.template_name,{'form': form})

def post(self,request):
    form=self.form_class(request.POST)

    if form.is_valid():
        user = form.save()
        username = form.cleaned_data('username')
        password = form.cleaned_data('password')
        user.set_password(password)
        user.save()

        newuser = authenticate(username=username,password=password)

        if newuser is not None:
            if newuser.is_active:
                login(request,newuser)
                return redirect("/genre")
    return render(request,self.template_name,{'form':form})