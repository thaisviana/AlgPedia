from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from algorithm.views import *
#show_main_page, sync_database, clear_database, show_all_classifications, show_classification_by_id

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

	url(r'^$', show_main_page),
	url(r'^sync/$', sync_database),
	url(r'^clearDB/$', clear_database),
	url(r'^accounts/profile/$', profile),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'accounts/login.html'}),
	url(r'^accounts/logout/$', logout),
	url(r'^signin/$', signin),
	url(r'^contact/$', contact),
	url(r'^rules/$', rules),
	url(r'^about/$', about),
	url(r'^show/cat/all$', show_all_classifications),
	url(r'^show/cat/id/(\d+)', show_classification_by_id), 
	url(r'^add/cat/id/(\d+)', display_add_algorithm), #shows the page where we can add an algorithm by category
	url(r'^show/alg/id/(\d+)', show_algorithm_by_id),
	url(r'^show/alg/all$', show_all_algorithms),
	url(r'^add/alg/id/(\d+)$', display_add_implementation),
	
	# serving static files in development
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : './algorithm/static/'}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
