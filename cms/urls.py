from django.conf.urls import include, url
from django.contrib import admin
from cms import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
#    url(r'back_user/searchform/$','back_user.views.searchform'),
#    url(r'back_user/search/$','back_user.views.search'),
#    url(r'back_user/index/$',      'back_user.views.index'),
#    url(r'back_user/demo/$','back_user.views.demo'),
#    url(r'back_user/publisherdate/$','back_user.views.publisherdate'),
    url(r'back_user/cmsindex/$','back_user.views.cmsindex'),
    url(r'back_user/indexleft/$','back_user.views.indexleft'),


    url(r'back_user/allusediv/$','back_user.views.allusediv'),
    url(r'back_user/footer/$','back_user.views.footer'),
    url(r'back_user/top/$','back_user.views.top'),
    url(r'back_user/welcome/$','back_user.views.welcome'),

    url(r'back_user/login/$','back_user.views.login'),
    url(r'back_user/dologin/$','back_user.views.dologin'),
    url(r'back_user/logout/$','back_user.views.logout'),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),

]
