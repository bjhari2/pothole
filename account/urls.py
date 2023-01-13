from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login', views.login_view, name='login_view'),
    path('logout', views.logout_view, name='logout_view'),
    path('register', views.register, name='register'),
    path('insert_pothole', views.insert_pothole, name='insert_pothole'),
    path('adminpage', views.admin, name='adminpage'),
    path('user', views.user, name='user'),
    path('contractor', views.contractor, name='contractor'),
    path('corporator', views.corporator, name='corporator'),
    path('section_officer', views.section_officer, name='section_officer'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
