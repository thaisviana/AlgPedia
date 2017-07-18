from algorithm.ajax import *
from algorithm.views import *
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = [
    url(r'^$', show_main_page),
    url(r'^sync/$', sync_database),
    url(r'^clearDB/$', clear_database),
    url(r'^accounts/profile/$', profile),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^ontoviz/$', ontoviz),
    url(r'^signin/$', signin),
    url(r'^contact/$', contact),
    url(r'^rules/$', rules),
    url(r'^about/$', about),
    url(r'^advanced_search/$', advanced_search),
    url(r'^show/cat/all$', show_all_classifications),
    url(r'^show/cat/id/(\d+)', show_classification_by_id),
    url(r'^add/cat/id/(\d+)', insert_algorithm),  # shows the page where we can add an algorithm by category
    url(r'^show/alg/id/(\d+)', show_algorithm_by_id),
    url(r'^show/alg/all$', show_all_algorithms, name='show_all_algorithms'),

    url(r'^show/para/id/(\d+)', show_paradigm_by_id),
    url(r'^show/para/all$', show_all_paradigms),

    url(r'^add/alg/id/(\d+)$', insert_implementation),
    url(r'^moderator/$', moderator_dashboard, name='moderator_dashboard'),

    url(r'^algorithm/add/$', insert_algorithm),

    # ajax
    url(r'^ajax/moderator_action/$', moderator_action, name='moderator_action'),
    url(r'^ajax/moderator_add/$', moderator_add, name='moderator_add'),
    url(r'^ajax/tag_add/$', tag_add, name='ajax-tag_add'),
    url(r'^ajax/global_search_autocomplete/$', global_search_autocomplete, name='ajax-global_search_autocomplete'),

    # serving static files in development
    # (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : './algorithm/static/'}),

    url(r'^admin/', include(admin.site.urls)),
]

# STATICS
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
