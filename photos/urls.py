from django.urls import path
from .import views
urlpatterns = [
    path('add-photo', views.add_photo, name='add-photo'),
    path('update-photo/<int:p_id>', views.update_photo, name='update-photo'),
    path('delete-photo/<int:p_id>', views.delete_photo, name='delete-photo'),

]
