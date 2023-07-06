There is one cookie that is created by firstly browsing the website.

It's name I_am_admin admin and contain something that look like a md5 hash.

After decrypting the hash, i found `false` string.

So i tried to replace the cookie value by the md5 hashing of the string `true` that is `b326b5062b2f0e69046810717534cb09`

After a page refresh, the site display a js alter with this message :

Good job! Flag : df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3

Soo we got the flag !
