from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'common'

urlpatterns = [
    # 로그인 로그아웃 계정생성
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('sighup/', views.signup, name='signup'),

    # 비밀번호 변경
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
]