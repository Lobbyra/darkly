I don't know if this is a flag or a part of one.

From my work on the userTableSQLInjectionFlag, i exported the table named db_default :

| id | username | password |
| --- | --- | --- |
| 1 | root | 3bf1114a986ba87ed28fc1b5884fc2f8 |
| 2 | admin | 3bf1114a986ba87ed28fc1b5884fc2f8 |

These are login and md5 hashed password.
They are the same and the decrypted version is : shadow

There is an official sign-in page in the web site, if i login to this page with admin:shadow or root:shadow, i got a page with a flag : `b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2`
