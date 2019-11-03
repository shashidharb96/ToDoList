
from django.contrib import admin
from django.urls import path
from user import views as user_views
from list import views as list_views
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', include('list.urls')),
    path('register/', user_views.register, name='register'),
    path('APIView/',  list_views.API_LIST.as_view() )

]


urlpatterns=format_suffix_patterns(urlpatterns)