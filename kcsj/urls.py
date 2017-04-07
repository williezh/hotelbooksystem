from django.conf.urls import include, url

from django.contrib import admin
from qiniuyun import views as qiniuyun_views
from DJangoHotel.viewspackage.aboutView import about
from DJangoHotel.viewspackage.indexView import index
from DJangoHotel.viewspackage.orderResultView import orderResult
from DJangoHotel.viewspackage.orderView import order
from DJangoHotel.viewspackage.roomInfoView import roomInfo
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    # Examples:
    # url(r'^$', 'kcsj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', RedirectView.as_view(url='/upload/', permanent=True),name='home'),
    url(r'^upload/$', qiniuyun_views.upload, name='upload'),
    url(r'^upload/done/$', qiniuyun_views.upload_result, name='upload_done'),
    url(r'^images/$', qiniuyun_views.show_imgs, name='show_imgs'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', about),
    url(r'^roominfo/', roomInfo),
    url(r'^$', index, name='home'),
    url(r'^order/',order),
    url(r'^orderresult/',orderResult)
]


