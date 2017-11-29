from django.conf.urls import patterns, include, url
from album.views import Upload

urlpatterns=patterns('',
                url(r'^$', Upload,
                    # view=Upload.as_view(),
                    # name='upload'
                    ),
             )