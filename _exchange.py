import requests
import json

api_key = '7c8eb82197a9c75b3f460ea8'
api_url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/'

bozulan_doviz = input('Bozulan döviz türü: ') #USD
alinan_doviz = input('Alınan döviz türü: ') #TRY
miktar = int(input(f'Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: '))

sonuc = requests.get(api_url + bozulan_doviz)
sonuc_json =  json.loads(sonuc.text)

#print(sonuc_json['conversion_rates'][alinan_doviz])

print('1 {0} = {1} {2}'.format(bozulan_doviz, sonuc_json['conversion_rates'][alinan_doviz],alinan_doviz))
print('{0} {1} = {2} {3}'.format(miktar,bozulan_doviz, miktar * sonuc_json['conversion_rates'][alinan_doviz],alinan_doviz))