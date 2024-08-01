from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from users import views

urlpatterns = [
    path("login/", views.AuthView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
