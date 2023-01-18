from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login', views.login_view, name='login_view'),
    path('logout', views.logout_view, name='logout_view'),
    path('register', views.register, name='register'),
    path('corp_register', views.corp_register, name='corp_register'),
    path('insert_pothole', views.insert_pothole, name='insert_pothole'),
    path('assign_pothole', views.assign_pothole, name='assign_pothole'),
    path('user', views.user, name='user'),
    path('contractor', views.contractor, name='contractor'),
    path('corporator', views.corporator, name='corporator'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
