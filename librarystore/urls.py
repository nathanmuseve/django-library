from django.urls import path
from . import views

app_name = "librarystore"

# views
urlpatterns = [
    path('', views.main, name='home'),
    path('novels/', views.novel_list, name='novel_list'),
    path('add/', views.add_novel_form, name='add'),
    path('all_detail/', views.all_detail, name='all_detail'),
    path('novel_detail/', views.novel_datail, name='novel_detail'),
    path('novel_details/<int:id>/', views.novel_details, name='novel_detail'),
    
    # path('novels/create/', views.NovelCreateView.as_view(), name='novel_create'),
    # path('novels/<int:id>/update/', views.NovelUpdateView.as_view(), name='novel_update'),
    # path('novels/<int:id>/delete/', views.NovelDeleteView.as_view(), name='novel_delete'),



]
