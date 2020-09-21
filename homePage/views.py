from django.views.generic import TemplateView

class homeView(TemplateView):
    template_name = "homeView.html"
    
class aboutView(TemplateView):
    template_name = "aboutView.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['name'] = "Nadim Mahmud"
        context['id'] = "201915004"
        
        return context