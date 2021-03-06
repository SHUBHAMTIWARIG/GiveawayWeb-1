from django.conf.urls import url


from products.views import addProducts, addGiveaway, viewGiveaway, viewProduct, viewGiveawayDetail, viewProductDetail, \
    update_entry

urlpatterns = [
    url(r'^add_product$', addProducts, name='add_product'),
    url(r'^add_product$', addProducts, name='save_product'),
    url(r'^add_giveaway$', addGiveaway, name='add_giveaway'),
    url(r'^add_giveaway$', addGiveaway, name='save_giveaway'),
    url(r'^giveaway$', viewGiveaway, name='view_giveaway'),
    url(r'^giveaway/(?P<id>\d)/$',viewGiveawayDetail, name='view_giveaway_detail'),
    url(r'^giveaway/(?P<id>\d)/(?P<s>\w+)/$',update_entry, name='view_giveaway_detail'),
    url(r'^product/$', viewProduct, name='view_product'),
    url(r'^product/(?P<id>\d)/$', viewProductDetail, name='view_product_detail'),

]
