from django.urls import path

from . import views

# namespace the urls with app_name
# reference from templates with format 'namespace:name' ie 'polls:detail'
app_name = 'polls'
urlpatterns = [
    #base is /polls/
    path('', views.index, name='index'),
    #ex: /polls/5/
    path('<int:question_id>/', views.detail, name="detail"),
    #ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name="results"),
    #ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name="vote"),
]