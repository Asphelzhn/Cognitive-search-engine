from detecht_api.models import Search_Autocomplete
'''
By Severn
'''

def get_autocomplete(query):
    query = query.lower()
    result = Search_Autocomplete.objects.filter(n_gram_iregex="^"+query)[:8]
    return result
