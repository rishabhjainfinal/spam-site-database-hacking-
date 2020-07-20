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
