from django.conf.urls import patterns, include, url

urlpatterns = patterns('photo.views',
	url(r"^search/$", "search"),
	url(r"^update/$", "update"),
	url(r"^image/(\d+)/$", "image"),
	url(r"^(\d+)/(full|thumbnails|edit)/$", "album"),
	url(r"^media/", "media"),
	url(r"", "main"),
)
