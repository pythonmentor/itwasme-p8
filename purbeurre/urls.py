"""purbeurre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from core import views as core_views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from favorites import views as fav_views
from search import views as search_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        core_views.HomePageView.as_view(),
        name="/"
    ),
    path(
        "account/<user>",
        core_views.AccountView.as_view(template_name="account.html"),
        name="account",
    ),
    path(
        "signup/",
        core_views.SignUpView.as_view(),
        name="signup"
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login"
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="logout.html"),
        name="logout",
    ),
    path(
        "search/",
        search_views.SearchView.as_view(),
        name="search"
    ),
    path(
        "search/substitutes/",
        fav_views.SubstituteView.as_view(),
        name="substitutes"
    ),
    path(
        "search/detail/<code>",
        search_views.ProductDetailView.as_view(),
        name="product_detail",
    ),
    path(
        "favorites/",
        fav_views.FavoritesView.as_view(),
        name="favorites"
    ),
    path(
        "legal-notice/",
        core_views.LegalNoticeView.as_view(),
        name="legal-notice"
    ),
]