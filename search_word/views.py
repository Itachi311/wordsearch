from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .search import search_word 
import json

# Renders the search page.
def search_view(request):
    return render(request, 'search.html', {})

# Returns the autocomplete results while the user types in a letter.
def search_autocomplete(request):
    if request.is_ajax() and request.method == 'GET':
        query = request.GET.get('word','')
        results = search_word(query)
        data = json.dumps(results)
    else:
        data = 'Unfortunate Error Appeared'
    type = 'application/json'
    return HttpResponse(data, type)

# Returns a json response having the search results(25 words) containing the searched word(partially)
def getSearchResults(request):
    if request.method == 'GET':
        query = request.GET.get('word') 
        if len(query)!=0:
            searchResult = results = search_word(query)
            
            if len(searchResult) == 0:
                return JsonResponse({'Search_Result': "Word you entered was not found.",'Success':False})
            else:
                return JsonResponse({'Search_Result': searchResult,'Success':True})
        else:
            return redirect('/')
