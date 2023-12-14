There is a page to vote for a member.

The form send a "sujet" and a "valeur".

With cURL, i tried a big value as valeur and the response contains a flag :

curl --location 'http://172.16.91.134/index.php?page=survey' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'sujet=5' \
--data-urlencode 'valeur=2222222'

```
<h2 style="margin-top:50px;"> The flag is 03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa</h2>
```
