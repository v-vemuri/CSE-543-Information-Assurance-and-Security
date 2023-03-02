Name: Vaishnavi Vemuri
ID number: 1226770885

LEVEL 01

Secret: Your First Blood
MD5 hash of the secret: cd3d9cadf1ef30f7dc5802e823116310

Description:
I connected to vpn and in the burp suite and I turned on the intercept. Opened the browser from burp suite and entered the level01 URL.
From the target response in burp suite, I went through the verify function and was able to find the secret - Your First Blood

LEVEL 02

Secret: allyourbasebelongtous
MD5 hash of the secret: 41e33f8c6719f97e1ac00d745e6a25c5

Description:
 
Started with giving the URL with the secret of level 01. The secret has been converted by using MD5 generator and then give the MD5 with the level02 URL. I looked at the burp and saw that the list of users was being fetched from /cgi-bin/users.php. I didn’t see any users in burp. Then, I tried running fetch command from the chrome console and realized that the referer was important.

I then tried to filter the payload with command line injection
curl --referer http://pwnthemall.cse543.rev.fish:8082/users.html 'http://pwnthemall.cse543.rev.fish:8082/cgi-bin/users.php?filter=;ls'

Then I used the filter to get the secret user
curl --referer http://pwnthemall.cse543.rev.fish:8082/users.html 'http://pwnthemall.cse543.rev.fish:8082/cgi-bin/users.php?filter=;cat%20secretuser.txt'

Then I received secret as allyourbasebelongtous

LEVEL 03

Secret: Hack the planet!
MD5 hash of the secret: ba49a4555854299152eb44d2619bc5bf

Description:
 
Started with giving the URL with the secret of level 02. The secret has been converted by using MD5 generator and then give the MD5 with the level03 URL. I opened the browser from Burp and opened the URL. I then saw that not passing ID when given Mike’s details gives us an ID. I then gave the ID and not passed any of the details of Mike and received the secret - Hack the planet!

LEVEL 04

Secret: thisissuchasimplesecret
MD5 hash of the secret: 9b87ecb29600dd01b9e32d2cd268a9a4

Description:

Started with giving the URL with the secret of level 03. The secret has been converted by using MD5 generator and then give the MD5 with the level04 URL. I figured out that there was a JavaScript injection vulnerability. I got the name of the file using the vulnerability from level02. Then, when I enter filename=sess_91c7e1e10744d69fd8fe35ecfc&readmode=yes, I got the username as mike and secret password as thisissuchasimplesecret

LEVEL 05

Secret: wel0vesecurity
MD5 hash of the secret: fdf1f06b0422dc2746c7daff964c5307

Description:

Started with giving the URL with the secret of level 04. The secret has been converted by using MD5 generator and then give the MD5 with the level05 URL. After many attempts, I figured out that the answer would be in the error messages. I then passed some good filenames such as store and receive and then, I was able to read the python scripts, the password was terriblechoice. Then I used the password in administrator mode to get all the passwords and usernames from all IDs and the got mike's password, wel0vesecurity

LEVEL 06

Secret: SuperMegaSecretNoGuessing
MD5 hash of the secret: c84f270fa1ae043894c2d758bb17da2e

Description:

Started with giving the URL with the secret of level 05. The secret has been converted by using MD5 generator and then give the MD5 with the level06 URL. I looked at the user agent field in HTTP request header. When I tried to change the field, it was trying to read files by appending .php to the field. I then checked files under /tmp/ and found x.php. passing /tmp/x and it revealed the secret, SuperMegaSecretNoGuessing
