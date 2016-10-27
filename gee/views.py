from django.shortcuts import render

def maps_list(request):
	return render(request, 'gee/maps_list.html', {})
