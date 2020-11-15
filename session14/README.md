# Webserver



# HTTP Server

```console
>mkdir http
>cd http
>python3 -m http.server
```


```html
<!DOCTYPE html>
<html>
<head>
<title>Hallo Welt!</title>
</head>

<body>
<h1>Willkommen</h1>
<p>Dies ist meine eigene Webseite</p><br/> 

</body>
</html>
```


```console
>mkdir cgi-bin
```

```html
<!DOCTYPE html>
<html>
<head>
<title>Hallo Welt!</title>
</head>

<body>
<h1>Willkommen</h1>
<p>Dies ist meine eigene Webseite</p><br/> 

<form method="get" action="cgi-bin/myscript.py"> Hallo Dein Name? <br/>
<p>Name: <input type="text" name="name" maxlength="40" size="30" /></p>
<p><input type="submit" value="Login" /></p>
</form>

</body>
</html>
```



```python
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
```

```console
>python3 -m http.server --cgi
```


# Flask

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello World'

app.run()
```

```console
>python3 firstflsksrv.py
```


```python
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

app.run()
```

```console
>python3 flsksrv.py
```
