from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.views.generic import FormView
from .forms import ConTROLLForm
import os
import subprocess

class ConTROLLView(FormView):
    form_class = ConTROLLForm
    template_name = 'conTROLL.html'
    success_url = '/action/'

    def form_valid(self, form):
        command = self.request.POST.keys()
        os.system("qmmp --%s" % command[1])
        return super(ConTROLLView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ConTROLLView, self).get_context_data(**kwargs)
        actions = [
            'play-pause', 'volume 0',
            'volume-inc', 'volume-dec',
            'next', 'previous',
            'play', 'stop'
            ]
        context['actions'] = actions
        #context['current_song'] = os.system("qmmp --nowplaying \"%f\"")

        proc = subprocess.Popen(['qmmp --nowplaying "%p - %t \(%f\)"', ""],
                stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        context['current_song'] = out
        return context



def home(request):
    #os.system("qmmp --next")
    return HttpResponse('1')

#def action(request, action):
    #return HttpResponse(action)
