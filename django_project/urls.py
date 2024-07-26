"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from uploader.router import router as uploader_router
from rest_framework.routers import DefaultRouter
from form.views import StatesViewSet, HobbiesViewSet, ProgLangViewSet, FormsViewSet

router = DefaultRouter()

router.register(r'states', StatesViewSet)
router.register(r'hobbies', HobbiesViewSet)
router.register(r'languages', ProgLangViewSet)
router.register(r'forms', FormsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/media/', include(uploader_router.urls))
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)



