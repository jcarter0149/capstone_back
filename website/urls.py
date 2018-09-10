from django.conf.urls import url

from . import views

app_name = "website"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^addmember$', views.addmember, name='addmember'), 
    url(r'^adddetainee$', views.add_detainee, name='detainee'),
    url(r'^addsession$', views.session, name='addsession'),
    url(r'^session/(?P<pk>\d+)/$', views.updatesessionrole.as_view(), name='updatesession'),
    url(r'^detainee/(?P<pk>\d+)/$', views.detainee, name='detaineedetail'),
    url(r'^createreport$', views.report, name='report'),
    url(r'^report/(?P<pk>\d+)/$', views.singlereport, name='singlereport'),
]