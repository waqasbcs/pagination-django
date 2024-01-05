
from django.contrib import admin
from django.urls import path
from waqas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.post_list),
]
