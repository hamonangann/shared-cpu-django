from django.http import JsonResponse
import time
import math
from django.views.decorators.csrf import csrf_exempt

# Modified from https://qxf2.com/blog/generate-cpu-load/
def generate(request):
    start = time.time()

    # Length in milliseconds. Default is 100
    length = float(request.GET.get("length")) if request.GET.get("length") else 100.0

    res = 0
    while time.time()-start < length / 1000.0:
        res = math.sqrt(64*64*64*64*64)

    return JsonResponse({'status': 200, 'message': "success", "time": time.time()-start})
