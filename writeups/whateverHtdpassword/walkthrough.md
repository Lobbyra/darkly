In the robots.txt file, there is a path named /whatever.

This path return an index page with only one entry : htdpassword.

This file is downloadable and contains this text : `root:437394baff5aa33daa618be47b75cb49`

This is a login password combinaison. The password is md5 hashed that can be decrypted.
The result of the decryption is : `qwerty123@`

With a dirbuster named `dirb`, i found a hidden path /admin. You can find the log of the program in /global/ressources/dirb_log.txt. The wordlist is the default one from the binary.

This page is a login/password form, I tried thoses logins a got a page that give a flag :
`d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff`
