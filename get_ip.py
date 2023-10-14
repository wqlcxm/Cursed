import requests

import folium


def get_info_by_ip(ip='127.0.0.1'):
	try:
		response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

		data = {
			'[IP]': response.get('query'),
			'[Int prov]': response.get('isp'),
			'[Org]': response.get('org'),
			'[Country]': response.get('country'),
			'[Region Name ]': response.get('regionName'),
			'[City]': response.get('city'),
			'[ZIP]': response.get('zip'),
			'[Lat]': response.get('lat'),
			'[Lon]': response.get('lon'),
		}

		for k, v in data.items():
			print(f'{k} : {v}')

		area = folium.Map(location=[response.get('lat'), response.get('lon')])
		area.save(f'{response.get("query")}_{response.get("city")}.html')

	except requests.exceptions.ConnectionError:
		print('[!] Please check your connection!')


def main():
	
	try:
		ip = input('Введите IP: ')
		get_info_by_ip(ip=ip)
	except KeyboardInterrupt:
		print('\n[+] Cancellation...')


if __name__ == '__main__':
	main()