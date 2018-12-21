from django.views.generic import TemplateView

class EnterPage(TemplateView):
    template_name = 'enter.html'

class ExitPage(TemplateView):
    template_name = 'exit.html'

class HomePage(TemplateView):
    template_name = 'index.html'