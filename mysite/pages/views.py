from django.shortcuts import render
from .models import Notebook
from django.views.generic import ListView
# Create your views here.


class IndexListView(ListView):
    template_name = 'pages/index.html'

    def get(self, request):
        nout_list = Notebook.objects.all()
        return render(request, self.template_name, context={'nout_list':nout_list})


class NoutListView(ListView):
    template_name = 'pages/nout.html'

    def get(self, request):
        return render(request, self.template_name, context={})


class NoutInfoListView(ListView):
    template_name = 'pages/nout_info.html'

    def get(self, request):
        return render(request, self.template_name, context={})
