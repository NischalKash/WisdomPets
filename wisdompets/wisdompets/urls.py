from django.conf.urls import url
from django.contrib import admin
from adoptions import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.home,name='home'),
    url(r'^adoptions/(\d+)/',views.pet_detail,name = 'pet_detail'),
]
