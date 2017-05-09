from django.conf.urls import url
from django.contrib import admin
from angelapp.views import get_product_analytics, get_product_list, set_image_rating, set_text_rating, get_homepage
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_homepage),
    url(r'^text/create/$', set_text_rating),
    url(r'^image/create/$', set_image_rating),

    url(r'^(?P<cslug>[\w-]+)/$', get_product_list),
    url(r'^(?P<cslug>[\w-]+)/(?P<pslug>[\w-]+)/$', get_product_analytics)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
