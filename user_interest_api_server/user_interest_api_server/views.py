from django.http import JsonResponse, Http404
from djangoApiDec.djangoApiDec import queryString_required, date_proc
import json, re, os, random

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


@queryString_required(['portion', 'num'])
def momoapi(request):
    """Generate list of term data source files
    Returns:
        if contains invalid queryString key, it will raise exception.
    """
    portion = json.loads(request.GET['portion'])
    num = int(request.GET['num'])

    data = json.load(open('momo_data.json','r'))

    categoryArray = ['tissue','notebook','lodging','fragrance','sportswear','makeup','health','organicfood','watch','underwear'
                        ,'girlshoes','pregnant','appliances','camping','bag','book','video','stationery','religion','anime']
    portion_num = 0
    for n in portion:
        portion_num += int(n)
    x = 0
    result = []
    
    for category in categoryArray:
        sample = int(num * (portion[x] / portion_num) + 0.5)
        if sample > 10 : sample = 10
        sampleArray = random.sample(data[category], sample)
        
        for ele in sampleArray:
            result.append(ele)
        
        x += 1
    
    return JsonResponse(result, safe=False)