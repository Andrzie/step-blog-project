
from django.urls import path
from . import views

urlpatterns = [

    path('', views.posts ),
    path('post/<int:pk>/', views.post, name='post')
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)