from django.urls import path
from .views import UserLoginView, user_logout_view, UserRegisterView, UserProfileEditView, UserProfileView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login"), # CLASS-BASED VIEW
    path('register/', UserRegisterView.as_view(), name="register"),
    path('logout/', user_logout_view, name="logout"), # function_based_view
    path('edit_profile/', UserProfileEditView.as_view(), name="edit_profile"),
    path('profile/<int:user_id>/', UserProfileView.as_view(), name="profile"),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]