from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^products/$', views.products, name='products'),
    url(r'^services/$', views.services, name='services'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^about/$', views.about, name='about'),
    url(r'^product/(?P<product>\w+)$', views.product, name='product'),
]