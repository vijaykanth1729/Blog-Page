from django.urls import path
from myapp.views import  HomeView, EntryDetail, CreateEntry
app_name = 'myapp'
urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('<int:pk>/', EntryDetail.as_view(), name='detail'),
    path('create/', CreateEntry.as_view(success_url='/'), name='create'),

    #searching
   # path('search/', search_query, name='search'),


]