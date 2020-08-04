#https://docs.python-guide.org/scenarios/scrape/

from lxml import html
import requests
import json



oga = []
urls =[]

# primera pagina
urls.append('https://www.infocasas.com.py/alquiler/casas-y-departamentos/asuncion/')


#print( len(urls) )        
for uri in urls:
    #page = requests.get('https://www.infocasas.com.py/alquiler/casas-y-departamentos/asuncion/pagina3/')
    page = requests.get(uri)
    tree = html.fromstring(page.content)


    #This will create a list of buyers:
    buyers = tree.xpath('//a/p/text()')
    #This will create a list of prices
    prices = tree.xpath('//div[@class="precio"]/text()')
    #This will create a list of domitorios
    dormitorios = tree.xpath('//div[@class="iconos first"]//span[@class="descri-numero"]/text() ')
    banos = tree.xpath('//div[@class="iconos middle"]//span[@class="descri-numero"]/text() ')
    m2s =  tree.xpath('//div[@class="iconos last"]//span[@class="descri-numero"]/text() ')

    # oga = casa()
    for buy in buyers:
        aux = "{'people': [ { 'nombre':'@nombre','valor':'@valor','dormitorios':'@dormitorios','banos':'@banos','m2':'@m2' } ]}"
        aux = aux.replace('@nombre',buy)
        for precio in prices:
            aux = aux.replace('@valor',precio)
            for dormi in dormitorios:
                aux = aux.replace('@dormitorios',dormi)
                for bano in banos:
                    aux = aux.replace('@banos',bano)
                    for m2 in m2s:
                        aux = aux.replace('@m2',m2)

        oga.append( aux.replace('\n                          ','').replace('\n                        ','') )



data = json.dumps(oga, indent=4)


f = open("datajson.txt", "w")
f.write(data)
f.close()