#coding:utf-8
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
    url(r'back_user/toEditPassword/$','back_user.views.toEditPassword'),
    url(r'back_user/editPassword/$','back_user.views.editPassword'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),

    url(r'^back_theme/themeIndex$', 'back_theme.views.themeIndex'),
    url(r'^back_theme/searchTheme$', 'back_theme.views.searchTheme'),
    url(r'^back_theme/exportExcel$', 'back_theme.views.exportExcel'),
    url(r'^back_theme/hideTheme$', 'back_theme.views.hideTheme'),
    url(r'^back_theme/addThemePage$', 'back_theme.views.addThemePage'),
    url(r'^back_theme/editThemePage$', 'back_theme.views.editThemePage'),
    url(r'^back_theme/saveTheme$', 'back_theme.views.saveTheme'),
    url(r'^back_theme/initThemeType$', 'back_theme.views.initThemeType'),
    url(r'^back_theme/saveThemeType$', 'back_theme.views.saveThemeType'),
    url(r'^back_theme/uploadImg$', 'back_theme.views.uploadImg'),

    url(r'^back_question/questionIndex$', 'back_question.views.questionIndex'),
    url(r'^back_question/addQuestionPage$', 'back_question.views.addQuestionPage'),
    url(r'^back_question/editQuestionPage$', 'back_question.views.editQuestionPage'),
    url(r'^back_question/saveQuestion$', 'back_question.views.saveQuestion'),
    url(r'^back_question/hideQuestion$', 'back_question.views.hideQuestion'),
    url(r'^back_question/searchQuestion$', 'back_question.views.searchQuestion'),

    url(r'^back_answer/answerIndex$', 'back_answer.views.answerIndex'),
    url(r'^back_answer/searchQuestion$', 'back_answer.views.searchQuestion'),

    url(r'^back_virtualuser/virtualUserIndex$', 'back_virtualuser.views.virtualUserIndex'),
    url(r'^back_virtualuser/searchVirtualUser$', 'back_virtualuser.views.searchVirtualUser'),
    url(r'^back_virtualuser/showVirtualUser$', 'back_virtualuser.views.showVirtualUser'),
    url(r'^back_virtualuser/editVirtualUserPage$', 'back_virtualuser.views.editVirtualUserPage'),
    url(r'^back_virtualuser/addVirtualUserPage$', 'back_virtualuser.views.addVirtualUserPage'),

    url(r'^back_realuser/realuserIndex$', 'back_realuser.views.realuserIndex'),
    url(r'^back_realuser/searchRealUser$', 'back_realuser.views.searchRealUser'),

    url(r'^back_user/initAddUser$', 'back_user.views.initAddUser'),
    url(r'^back_user/initEditUser$', 'back_user.views.initEditUser'),
    url(r'^back_user/addUser$', 'back_user.views.addUser'),
    url(r'^back_user/editUser$', 'back_user.views.editUser'),
    url(r'^back_user/showUsers$', 'back_user.views.showUsers'),
    url(r'^back_user/showUsersToJson$', 'back_user.views.showUsersToJson'),
    url(r'^back_user/removeUser$', 'back_user.views.removeUser'),
    url(r'^back_user/modifyUserStatus$', 'back_user.views.modifyUserStatus'),
    url(r'^back_user/menuManager$', 'back_user.views.menuManager'),
    url(r'^back_user/addMenu$', 'back_user.views.addMenu'),


    #p2pmsg p2p消息
    url(r'^p2pmsg/hudong/$','p2pmsg.views.hudong'),
    url(r'^p2pmsg/userType/$','p2pmsg.views.userType'),
    url(r'^p2pmsg/virtualUserList/$','p2pmsg.views.virtualUserList'),
    url(r'^p2pmsg/realUserList/$','p2pmsg.views.realUserList'),
    url(r'^p2pmsg/p2pmessage/$','p2pmsg.views.p2pmessage'),
    url(r'^p2pmsg/viranswer/$','p2pmsg.views.viranswer'),
    url(r'p2pmsg/reanswer/$','p2pmsg.views.reanswer'),
    url(r'^p2pmsg/guanli/$','p2pmsg.views.guanli'),
    url(r'^p2pmsg/yunweiList/$','p2pmsg.views.yunweiList'),
]
