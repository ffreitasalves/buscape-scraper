#URL http://www.buscape.com.br/pesquise-uma-loja.html?pg=1
#from 1 to 21265
# $('.size1of3').each(function() {var x =  $(this).find('a:first');console.log(z.attr('title') + ' ' + x.attr('href'))});

import requests
try:
	import bs4
except ImportError:
	import BeautifulSoup as bs4
import openpyxl
import logging
from openpyxl import Workbook

#iniciar o arquivo de log
logging.basicConfig(filename='arq_links.log',level=logging.WARNING)

#iniciar a planilha do excel otimizada para escrita
wb = Workbook(write_only = True)
ws = wb.create_sheet()

for i in range(1,21266):	
	try:
		payload = {'pg':str(i)}
		response = requests.get('http://www.buscape.com.br/pesquise-uma-loja.html', params = payload)

		soup = bs4.BeautifulSoup(response.text)

		for div in soup.find_all(class_='size1of3'):
			ws.append([
				div.find('a')['title'], 
				div.find('a')['href'],
				'http://www.buscape.com.br/pesquise-uma-loja.html?pg=%s' % i,
				i,
				])
		
		print ("#%s" % i),

	except Exception as err:
		print ("Erro na pagina %s" % i)
		logging.exception(u"Erro na pagina %s" % i) 


wb.save('lojas.xlsx')
