from django.urls import path
from .views import GetAllUsersView, GetMyUserView, MyTokenObtainPairView, MyTokenRefreshView, Admin_View, Cliente_View

urlpatterns = [
    path('login', MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh', MyTokenRefreshView.as_view(), name='token_refresh'),
    path('logon/admin', Admin_View.as_view()),
    path('logon/cliente', Cliente_View.as_view()),
    path('myuser', GetMyUserView.as_view()),
    path('users/all', GetAllUsersView.as_view()),
]
