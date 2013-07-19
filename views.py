# Create your views here.

from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from mysite.settings import MEDIA_ROOT
from django.conf import settings


@staff_member_required
def media(request):
	f = None
	actualPath = settings.MEDIA_ROOT + "\\images"
	imageName = request.path.split("/")
	actualPath += "\\" + imageName[len(imageName)-1]
	actualPath = actualPath.replace('\\','/')
	print 'actualPath'
	print actualPath
	# 'b' binary mode required for image file
	f = open(actualPath, 'rb')
	if '.jpg' in request.path:
		imageTypeValue = "image/jpeg"
	elif '.png' in request.path:
		imageTypeValue = "image/png"
	return HttpResponse(f.read(), mimetype=imageTypeValue)
