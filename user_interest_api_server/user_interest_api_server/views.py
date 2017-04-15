from django.http import JsonResponse, Http404
from djangoApiDec.djangoApiDec import queryString_required, date_proc
import json, re, os

@queryString_required(['event', 'num'])
def api(request):
	"""Generate list of term data source files
	Returns:
		if contains invalid queryString key, it will raise exception.
	"""
	event = request.GET['event']
	num = int(request.GET['num'])
	try:
		result = json.load(open(event+'.json','r'))[:num]
	except Exception as e:
		result = ["invalid parameter"]
	return JsonResponse(result, safe=False)