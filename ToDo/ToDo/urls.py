
from django.contrib import admin
from django.urls import path
from user import views as user_views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', include('list.urls')),
    path('register/', user_views.register, name='register'),
]
