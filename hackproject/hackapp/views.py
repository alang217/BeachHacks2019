from django.views.generic import TemplateView
from .forms import HomeForm
from django.shortcuts import render
from . import sound_check as sc

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
            client = sc.instantiate_client()
            document = sc.make_document(text)

            f = form.save(commit=False)
            f.tone = sc.tone_analysis(client, document)
            f.emotion = sc.emotion_analysis(client, document)
            f.professionalism = sc.professionalism_analysis(client, document)
            f.offensiveness = sc.offensiveness_analysis(client, document)
            f.reading_level = sc.reading_level_analysis(client, document)
            

            ## save the other stuff here
            text = form.cleaned_data['post']
            print(f)

        args = {'form': form, 'text':text}

        return render(request, self.template_name, args)



