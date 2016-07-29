# mailer_reverse_shell
A python reverse shell using email subject text as the connecting address<br>
Use this format as the email subject, for example ***10.1.1.1:9965***<br>
The script would check the latest email subject and use the subject text as the reverse shell address<br>
To connect to the machine running this script, simply use nc as following:<br>
***nc -nvlpp port***<br>
Make sure that your firewall doesn't block the connection
