from django.conf.urls import patterns, include, url
from zone.views import agewise1
#from django.conf import settings
#from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$','zone.views.home'),
    url(r'^boys.html/$', 'zone.views.boys'),
    #url(r'^home/()/$',boys),
    #url(r'home/boys(?P<num>\d+)/$',boys),
    #url(r'^home/.',direct_to_template, {'template':'boys.html'),
    url(r'^girls.html/$','zone.views.girls'),
    url(r'^babies.html/$','zone.views.babies'),
    url(r'^agewise/$','zone.views.agewise1'),
    # Examples:
    # url(r'^$', 'kids.views.home', name='home'),
    # url(r'^kids/', include('kids.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
