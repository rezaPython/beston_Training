from django.conf.urls import url
from . import views


urlpatterns = [
    url('^submit/expense/$', views.submit_expense, name='submit_expense'),
    url('^submit/income/$', views.income, name='income'),

]
