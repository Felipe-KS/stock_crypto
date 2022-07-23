from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.views.generic import TemplateView

import requests

# Create your views here.
class IndexPage(TemplateView):
    template_name = 'API/dashboard.html'
    '''
    Nome: Exibe o nome da moeda.
    Símbolo: Exibe o símbolo da moeda.
    Preço: Exibe o preço da moeda.
    Sinalização: Exibe a variação (em %) do preço da moeda nas últimas 24h. Caso tenha aumentado, a variação precisa estar com a cor verde, do contrário, vermelha.
    '''    

    '''def get(self, request, *args, **kwargs):
        
        crypto = request.query_params.get('c')
        r = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms='+ crypto +'&tsyms=BRL')
        r = r.json()
        raw = r['RAW']
        display = r['DISPLAY']
        info = [[] for i in range(len(r['DISPLAY']))]
        for valores in r['DISPLAY']:
            for i in range(len(r['DISPLAY'])):
                coinraw = raw[valores]['BRL']

                info[i].append(valores)
                info[i].append(coinraw['FROMSYMBOL'])
                info[i].append(coinraw['PRICE'])
                info[i].append(((coinraw['PRICE']*100)/coinraw['OPEN24HOUR'])-100)
        template = loader.get_template('API/dashboard.html')
        context = {
                'info':info
            }
        return HttpResponse(info)'''