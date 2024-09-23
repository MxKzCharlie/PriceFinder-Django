from rest_framework import status
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt



# Datos para enviar al front
# "url": "https://www.mercadolibre.com.mx/realme-air-6-pro-50db-hifi-unit-dual-coaxial-40h-battery-color-twilight-black-luz-twilight-black/p/MLM37848885?pdp_filters=item_id:MLM3285850022#wid=MLM3285850022&sid=search&is_advertising=true&searchVariation=MLM37848885&position=1&search_layout=grid&type=pad&tracking_id=45d63465-61d2-451a-96b3-ca21e1d8a62f&is_advertising=true&ad_domain=VQCATCORE_LST&ad_position=1&ad_click_id=MDgwNTY3ZjEtMmM5OS00NTM4LTlmYWItZDUzOTg1MDVkOTI0",
# "urlImg": "https://http2.mlstatic.com/D_NQ_NP_788638-MLU75358764299_032024-O.webp",
# "precio": "59.99",
# "titulo": "Realme Air 6 Pro 50db Hifi Unit Dual Coaxial 40h Battery Color Twilight black Luz Twilight black",
# "storeId": 1


def default_view(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

def get_api(request):
    if request.method == 'POST':

        return JsonResponse({"status": status.HTTP_200_OK})
