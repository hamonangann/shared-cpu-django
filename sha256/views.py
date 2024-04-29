from django.http import JsonResponse
import hashlib
import time
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def generate(request):
    start = time.time()
    msg = request.POST.get('message') or "test"
    encoded = hashlib.sha256(msg.encode()).hexdigest()
    finish = time.time()
    return JsonResponse({'status': 200, 'data':{'msg': msg, 'encoded': encoded, 'time': finish-start}})
