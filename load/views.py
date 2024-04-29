from django.http import JsonResponse
import time
import math
from django.views.decorators.csrf import csrf_exempt

# Modified from https://qxf2.com/blog/generate-cpu-load/
def generate(request):
    interval = request.GET.get("interval") or 1
    utilization = float(request.GET.get("utilization")) or 50.0

    start = time.time()
    start_time = time.time()
    for i in range(0,int(interval)):
        while time.time()-start_time < utilization/100.0:
            a = math.sqrt(64*64*64*64*64)
        time.sleep(1-utilization/100.0)
        start_time += 1
    finish = time.time()

    return JsonResponse({'status': 200, 'message': "success", "time": finish-start})
