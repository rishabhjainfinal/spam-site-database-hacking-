# vote_increaser_on_a_site

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

SO FOR EACH VOTE YOU HAVE TO ADD +1 IN YOUR **authorid**  ALTHOUGH IT ALSO ADD A VOTE WHEN REQUESTED FROM SAME **authorid   ¯\\_(ツ)_/¯ **

and then i make a simple script to fetch current votes 
```bash
def votes(url):
	source = urllib.request.urlopen(url).read()
	soup = bs.BeautifulSoup(source,features="html.parser")
	for i in soup.select('div.blog-item'):
		votes=i.p.strong.text
	return votes

```

you can also use **threading** to get things faster and more excited jsut un-comment all the threading lines code and comment the the increaser call funtion 

