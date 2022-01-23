from django.urls import path
from django.contrib.auth import views as auth_views
from common.views import account_views, profile_views


app_name = 'common'

urlpatterns = [
    # 로그인 로그아웃 회원가입
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('sighup/', account_views.signup, name='signup'),

    # 비밀번호 변경
    path('password_change/', account_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', views.PasswordChangeView.as_view(), name='password_change_done'),

    # 비밀번호 초기화
    path('password_reset/', account_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', account_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # 프로필
    path('profile/base/<int:user_id>/', profile_views.profile_base, name='profile_base'),
    path('profile/question/<int:user_id>/', profile_views.ProfileQuestionListView.as_view(), name='profile_question'),
    path('profile/answer/<int:user_id>/', profile_views.ProfileAnswerListView.as_view(), name='profile_answer'),
    path('profile/comment/<int:user_id>/', profile_views.ProfileCommentListView.as_view(), name='profile_comment'),
    path('profile/vote/<int:user_id>/', profile_views.ProfileVoteListView.as_view(), name='profile_vote'),
]