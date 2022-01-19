from django.http import JsonResponse,HttpResponse

def home (request):
    return HttpResponse("working")