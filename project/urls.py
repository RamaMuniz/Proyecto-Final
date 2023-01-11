"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from miblog.views import (index, PostDetalle, PostListar, 
                               PostCrear, PostBorrar, PostActualizar,
                               UserSignUp, UserLogin, UserLogout, 
                               AvatarActualizar, UserActualizar, MensajeCrear, MensajeListar, MensajeDetalle, about )
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('miblog/', index, name="miblog-index"),
    path('miblog/<int:pk>/detalle/', PostDetalle.as_view(), name="miblog-detalle"),
    path('miblog/listar/', PostListar.as_view(), name="miblog-listar"),
    path('miblog/crear/', staff_member_required(PostCrear.as_view()), name="miblog-crear"),
    path('miblog/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="miblog-borrar"),
    path('miblog/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="miblog-actualizar"),
    path('miblog/signup/', UserSignUp.as_view(), name ="miblog-signup"),
    path('miblog/login/', UserLogin.as_view(), name= "miblog-login"),
    path('miblog/logout/', UserLogout.as_view(), name="miblog-logout"),
    path('miblog/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="miblog-avatars-actualizar"),
    path('miblog/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="miblog-users-actualizar"),
    path('miblog/mensajes/crear/', MensajeCrear.as_view(), name="miblog-mensajes-crear"),
    path('miblog/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="miblog-mensajes-detalle"),
    path('miblog/mensajes/listar/', MensajeListar.as_view(), name="miblog-mensajes-listar"),
    path('miblog/about', about, name="miblog-about"),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
