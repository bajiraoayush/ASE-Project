from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='Cus_index'),
    path('signup/', views.signup, name='Cus_signup'),
    path('profile/', views.profile_page, name='Cus_profile'),
    path('logout/', views.user_logout, name='logout'),
    path('categories/', views.categories, name='Cus_categories'),
    path('res_area/', views.restaurants, name='res_area'),
    re_path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.activate, name='activate'),
    path('res_info/', views.res_info, name='Cus_resinfo'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='Customers/password_reset.html'),
         name='password_reset'),
    path('add_address/',views.add_address,name='add_address'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name=
                                                  'Customers/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name=
                                                     'Customers/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name=
                                                      'Customers/password_reset_complete.html'),
         name='password_reset_complete'),
]
