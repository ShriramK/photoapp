from django.conf.urls import patterns, include, url

urlpatterns = patterns('photo.views',
	url(r"^media/", "media"),
)
