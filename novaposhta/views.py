
from django.http import JsonResponse

from model_search import model_search

from novaposhta.models import Warehouse


def autocomplete(request):

    query = request.GET.get('query')

    if query:

        warehouses = Warehouse.objects.all()

        suggestions = []

        for warehouse in model_search(query, warehouses, Warehouse.search_fields):
            if warehouse.full_name not in suggestions:
                suggestions.append(warehouse.full_name)

        suggestions = suggestions[:10]

    else:
        suggestions = []

    return JsonResponse({
        'query': query,
        'suggestions': suggestions
    })
