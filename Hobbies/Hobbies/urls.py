from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from hobbies import views

handler404 = 'views.view_404'
handler500 = 'views.view_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hobbies.urls', namespace='hobbies')),
]