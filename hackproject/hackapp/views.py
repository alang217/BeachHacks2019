from django.views.generic import TemplateView
from .forms import HomeForm
from django.shortcuts import render


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']

            '''
            f = form.save(commit=False)
            f.tone =
            f.emotion =
            f.professionalism =
            f.offensiveness =
            f.reading_level =
            
            '''

            ## save the other stuff here
            text = form.cleaned_data['post']

        args = {'form': form, 'text':text}

        return render(request, self.template_name, args)



