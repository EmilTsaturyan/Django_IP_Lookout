from django.shortcuts import render
import requests

# Create your views here.

def get_info_by_ip(ip: str) -> dict:
    response = requests.get(f'http://ip-api.com/json/{ip}')
    response = response.json()
    return response

def create_google_maps(info):
    link = f'https://www.google.com/maps/@{info["lat"]},{info["lon"]},19z?entry=ttu'
    info['google maps'] = link
    return link

def index(request):
    ip_info = None

    if request.method == 'POST':
        ip = request.POST.get('ip')
        ip_info = get_info_by_ip(ip)
        if ip_info['status'] != 'fail':
            create_google_maps(ip_info)

    return render(request, 'index.html', context={
        'ip_info': ip_info
    })

