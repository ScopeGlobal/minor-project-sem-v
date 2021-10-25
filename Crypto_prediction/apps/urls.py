
from django.conf.urls import url
from django.urls import path
from apps import views

urlpatterns = [

    # The home page
    path('index', views.index, name='index'),
    # path('signin', views.signin, name='signin'),
    # path('signup', views.signup, name='signup'),
    path('signin/', views.signinPage, name="signin"),
    path('signup/', views.registerPage, name="signup"),
    path('logout',views.logoutUser,name='logout'), 
    url(r'profile/(?P<username>.+)/$', views.profile, name="profile"),
    path('coin-info',views.coin_info, name="coin-info"),
    path('real_time_test',views.real_time_test, name="real_time_test"),
    path('detailed-prediction',views.detailed_prediction, name="detailed-prediction"),
    path('payment',views.payment, name="payment"),

    
    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
