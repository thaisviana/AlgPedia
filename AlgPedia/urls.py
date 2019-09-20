from algorithm.ajax import *
import algorithm.views
import django
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib.auth import views as auth_views

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = [
    url(r'^$', algorithm.views.show_main_page),
    url(r'^sync/$', algorithm.views.sync_database),
    url(r'^clearDB/$', algorithm.views.clear_database),
    url(r'^accounts/profile/$', algorithm.views.profile),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^ontoviz/$', algorithm.views.ontoviz),
    url(r'^signin/$', algorithm.views.signin),
    url(r'^contact/$', algorithm.views.contact),
    url(r'^rules/$', algorithm.views.rules),
    url(r'^about/$', algorithm.views.about),
    url(r'^advanced_search/$', algorithm.views.advanced_search),
    url(r'^show/cat/all$', algorithm.views.show_all_classifications),
    url(r'^show/cat/id/(\d+)', algorithm.views.show_classification_by_id),
    url(r'^add/cat/id/(\d+)', algorithm.views.insert_algorithm),  # shows the page where we can add an algorithm by category
    url(r'^show/alg/id/(\d+)', algorithm.views.show_algorithm_by_id),
    url(r'^show/alg/all$', algorithm.views.show_all_algorithms),

    url(r'^show/para/id/(\d+)', algorithm.views.show_paradigm_by_id),
    url(r'^show/para/all$', algorithm.views.show_all_paradigms),

    url(r'^add/alg/id/(\d+)$', algorithm.views.insert_implementation),
    url(r'^moderator/$', algorithm.views.moderator_dashboard, name='moderator_dashboard'),

    url(r'^algorithm/add/$', algorithm.views.insert_algorithm),

    # ajax
    url(r'^ajax/moderator_action/$', moderator_action, name='moderator_action'),
    url(r'^ajax/moderator_add/$', moderator_add, name='moderator_add'),
    url(r'^ajax/tag_add/$', tag_add, name='ajax-tag_add'),
    url(r'^ajax/global_search_autocomplete/$', global_search_autocomplete, name='ajax-global_search_autocomplete'),

    # serving static files in development
    # (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : './algorithm/static/'}),

    url(r'^admin/', admin.site.urls),
]

# STATICS
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
