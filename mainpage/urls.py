from django.conf.urls import url
from .views import ProjectListAndFormView

urlpatterns = [
    url('', ProjectListAndFormView.as_view(), name='main')
]
