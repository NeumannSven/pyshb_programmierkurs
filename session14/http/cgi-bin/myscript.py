#!/usr/bin/env python3

import cgi
form = cgi.FieldStorage()
name = form.getvalue("name", "Unbekannter")

response = f"""Content-type: text/html

<html>
<head><title>Login-Seite</title></head>
<body>
    <h2>Moin Moin,</h2><br>
    <h2>{name}.</h2><br>
    <h2>Herzlich Willkommen</h2>
</body>
</html>"""

print(response)
