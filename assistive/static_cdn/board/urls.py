from django.conf.urls import url
from django.contrib import admin

from .views import (
	BoardDetailView,
	board_list,
	board_create,
	#start_page,
	#link,
	#donate,
	#contact,
	board_update,
	board_delete,
	board_detail
	#board_update,
	#board_delete,
	#board_detail,
	#BoardDetailView
	)

urlpatterns = [
	# url(r'^home/$', start_page,name='home'),
	# url(r'^link/$', link,name='link'),
	# url(r'^donate/$', donate,name='donate'),
	# url(r'^contact/$', contact,name='contact'),
	url(r'^blist/$', board_list, name='board'),
	# url(r'^blogs/$', post_list, name='list'),
    #url(r'^blogs/create/$', post_create),
    url(r'^create/$', board_create),
    #url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    #url(r'^(?P<slug>[\w-]+)/$', board_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/$', BoardDetailView.as_view(), name='detail'),
    #url(r'^(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='detail'), #Django Code Review #3 on joincfe.com/youtube/
    #url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/edit/$', board_update, name='board_update'),
    #url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    url(r'^(?P<slug>[\w-]+)/delete/$', board_delete, name='deleteb'),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
