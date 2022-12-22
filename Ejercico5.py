def pib_pais(link, pais):
    from urllib import request
    from urllib.error import URLError
    try:
        with request.urlopen(link) as url:
            datos = url.read().decode('utf-8').split('\n')
    except URLError:
        return ('El link ' + link + ' no existe!')
    else:
        datos = [info.split('\t') for info in datos]
        datos = [list(map(str.strip, info)) for info in datos]
        for info in datos:
            info[0] = info[0][-2:]
        datos[0][0] = 'años'
        datos = {info[0]:info[1:] for info in datos}
        return {datos["años"][info]: datos[pais][info] for info in range(len(datos['años']))}

pais = input('Introduce las iniciales de un pais Europeo:\n')
print('Producto Interior Bruto per capita de', pais)
print('Formato: AÑO:PIB')
link = 'https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/' \
       'BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true'
print(pib_pais(link, pais))

