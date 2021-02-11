from django.urls import path

from bboard.views import index
from bboard.views import by_rubric
from bboard.views import BbCreateView


urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
]