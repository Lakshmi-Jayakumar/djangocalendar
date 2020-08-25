from django.conf.urls import url
from . import views
from django.urls import path,include
app_name = 'cal'
urlpatterns = [
    path('',views.index,name="index"),
    path('calendar/', views.CalendarView.as_view(), name='calendar'), 
    path('event/new/', views.event, name='event_new'),
	path('event/<int:event_id>/details/', views.event, name='event_edit'),
	path('event/edit/<int:event_id>/delete/', views.deleteevent, name='event_delete'),

]