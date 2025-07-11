from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('search', views.search, name='search'),
    path('set', views.set, name="set"),
    path('changepass', views.changepass, name="changepass"),

    re_path(r"^accounts/", include('accounts.urls', namespace="accounts")),
    re_path(r"^projects/", include("projects.urls", namespace="projects")),
    re_path(r"^issues/", include("issues.urls", namespace="issues")),
    re_path(r"^chats/", include("chats.urls", namespace="chats")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
