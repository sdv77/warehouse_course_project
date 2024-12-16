from django.urls import path
from .views import login_view, register_view, profile_view, logout_view, home, get_item_info

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('get_item_info/<int:item_id>/', get_item_info, name='get_item_info'),
    path('logout/', logout_view, name='logout'),
    path('', home, name='home'),
     
]