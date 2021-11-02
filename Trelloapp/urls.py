from django.conf.urls import url
from django.urls.conf import path
from Trelloapp import views
# SET THE NAMESPACE!
app_name = 'Trelloapp'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    
]