from django.shortcuts import render
from django.views.generic import View, CreateView

from store.forms import CreateGigForm

# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'store/home.html')

class ManageGigView(CreateView):
    form_class = CreateGigForm
    template_name = 'store/create-gig.html'

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return super().form_valid(form)

    # def get(self, request):
    #     form = CreateGigForm()
    #     context = {'form': form}
    #     return render(request, 'store/create-gig.html', context)