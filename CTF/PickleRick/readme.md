placeholder


<pre>
root@ip-10-10-150-158:~# gobuster dir -u http://10.10.117.3 -w /root/Desktop/Tools/wordlists/dirb/common.txt 
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.117.3
[+] Threads:        10
[+] Wordlist:       /root/Desktop/Tools/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2021/04/21 15:19:50 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htaccess (Status: 403)
/.htpasswd (Status: 403)
/assets (Status: 301)
/index.html (Status: 200)
/robots.txt (Status: 200)
/server-status (Status: 403)
===============================================================
2021/04/21 15:19:50 Finished
===============================================================

</pre>
