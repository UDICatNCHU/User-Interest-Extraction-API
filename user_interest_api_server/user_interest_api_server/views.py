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
		result = sorted(json.load(open(event+'.json','r'))[:num], key=lambda x:x['time'], reverse=True)
	except Exception as e:
		result = json.load(open(event+'.json','r'))['item'][:num]
	return JsonResponse(result, safe=False)