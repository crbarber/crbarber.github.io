#!/usr/bin/python
import cgi, cgitb, sys
cgitb.enable()
f = open('logins.txt', 'r')
inputs = cgi.FieldStorage()
name = inputs['username'].value
password = inputs['password'].value
login = name+':'+password
logins = f.read()
user = ''
target = ''
for i in range(0, len(logins)):
    if login is logins[i]:
        user = name
f.close()
if user != '':
    t = open('targets.txt', 'r')
    targets = t.read()
    t.close()
    for i in range(0, len(targets)):
        line = targets[i]
        potname = line.split(':')
        if name is potname[0]:
            target = potname[1]
    
    print '''Content type: text/html
<html>
  <head>
  </head>
  <body style="                       background-image: url(&quot;Spoon_mod2.png&quot;);">
    <h1 style="color: white" align="center"> Welcome %s, your target: </h1>
    <meta content="text/html; charset=windows-1252" http-equiv="content-type">
    <p style="color:white" align="Center">Your target is: %s, go forth and spoon
      them. </p>
    <p style="color:white" align="Center"> number of people playing: %s</p>
    <p style="color:white" align="Center"> number of people elimenated: %s</p>
    
  </body>
</html>'''%(user, target, len(logins), 0)

else:
    print '''Content type: text/html
<html>
  <head>
  </head>
  <body style=" background-image: url(&quot;Spoon_mod2.png&quot;);">
    <h1 style="color: white" align="center"> Error: invalid login </h1>    
  </body>
</html>'''
