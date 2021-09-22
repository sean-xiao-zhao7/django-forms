from django.http.response import HttpResponseRedirect
from formsapp.forms import ReviewsForm
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Review
from .forms import ReviewsForm
from django.views import View

# Create your views here.

class ReviewView(CreateView):
    model = Review
    form_class = ReviewsForm
    template_name = 'formsapp/index.html'
    success_url = '/reviewlist'
            
class ThankyouView(TemplateView):
    template_name = 'formsapp/thankyou.html'

class ReviewListView(ListView):
    template_name = 'formsapp/review_list.html'
    model = Review
    context_object_name = "reviews"

class SingleReviewView(DetailView):
    template_name = 'formsapp/single_review.html'
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['favorite'] = self.request.session.get('fav_review_id') == str(self.object.id)
        return context

class FavoriteReview(View):
    def post(self, req): 
        id = req.POST['id']
        req.session['fav_review_id'] = id
        return HttpResponseRedirect("/single-review/" + id)
    