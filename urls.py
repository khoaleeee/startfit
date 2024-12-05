from django.urls import path
from django.contrib.auth import views as auth_views
from authapp import views

urlpatterns = [
    path('', views.Home, name = "Home"),
    path('signup', views.signup,name="signup"),
    path('login', views.handlelogin,name="handlelogin"),
    path('logout', views.handleLogout,name="handlelogout"),
    path('contact',views.contact,name="contact"),
    path('profile',views.profile,name="profile"),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]