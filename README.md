# Snippets API

API to create snippets with TTL. Snippet's TTL can be customized upon snippet creation. 
A snippet's TTL increases by 30 seconds every time a snippet is retrieved or liked.  


## Features: 
* TTL snippets - A snippet TTL is set by the `expires_in` POST request body field. If snippet is still alive and accessed before its expiration, 30 seconds are added to its TTL

* `/like` endpoint - PUT request to `/like` with snippet name increases snippet expiration by 30 seconds


## Languages and Libraries: 
Flask, Python 3.8.2

Why? Little boiler plate, easy to get started and to read, non-opionated backend framework


## Setup and Run locally:

* Set up virtualenv and initialize virtualenv. [Help doing so.](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
* Install all packages in requirements.txt:

    `pip install -r requirements.txt`
    
* In the root directory, run:
    `python3 main.py`
    
    Server will be found at: `http://0.0.0.0:8080/`




## Organization:
```
Snippets-API
      main.py [Flask server and routes]   
      controllers/
          create_snippet.py
          get_snippet.py
          process_payload.py
          update_snippet.py
      models/
          db.py [Using global object as db for now]
          schema.py
          snippets.py
      tests/
      README.md
```




## Run server on repl.it:

Server and routes are located in main.py 
* Click "Start" or "Restart" button on repl.it
* Make requests to `https://Snippets-API.briceidamariscal.repl.co/snippets` as stated below


### Endpoints:

POST:

```
URL:
https://Snippets-API.briceidamariscal.repl.co/snippets

POST Request Body:

{
	"name": "h",
	"expires_in": 2,
	 "snippet": "hel"
	
}

Types:
name = string
expires_in = integer
snippet = string


Response Payload:

{
  "expires_at": "2020-05-18T20:31:23.233361",
  "name": "h",
  "snippet": "hel",
  "likes" : 0,
  "url": "https://Snippets-API.briceidamariscal.repl.co/snippets/h"
}

Types:
expires_at = isoformat string
name = string
snippet = string
url = string
likes = integer

```

GET:

```
URL:
https://Snippets-API.briceidamariscal.repl.co/snippets/<snippet-name>


Response Payload:

{
  "expires_at": "2020-05-18T20:31:23.233361",
  "name": <snippet-name>,
  "likes": 0,
  "snippet": "hel",
  "url": "https://Snippets-API.briceidamariscal.repl.co/snippets/<snippet-name>"
}


Types:
expires_at = isoformat string
name = string
snippet = string
url = string
likes = integer


Errors:

400 - snippet name was not passed in
404 - snippet name does not exist in cache because it wasn't created or has expired

```


PUT:

Increment number of likes and add 30 seconds to TTL
```
URL:
https://Snippets-API.briceidamariscal.repl.co/snippets/like

PUT Request Body:

{
	"name": "h",	
}

Types:
name = string

Response Payload:

{
  "expires_at": "2020-05-18T20:31:23.233361",
  "name": "h",
  "likes": 1,
  "snippet": "hel",
  "url": "https://Snippets-API.briceidamariscal.repl.co/snippets/h"
}


Types:
expires_at = isoformat string
name = string
snippet = string
url = string
likes = integer


```


Example:

```
- Make POST:

curl --location --request POST 'https://Snippets-API.briceidamariscal.repl.co/snippets' \
--header 'Content-Type: application/json' \
--data-raw '{
	
	"name": "hello",
	"expires_in": 30,
	 "snippet": "hello there test"
	
}'



POST Request Response:
{
  "expires_at": "2020-05-18T20:40:28.951011",
  "name": "hello",
  "snippet": "hello there test",
  "likes": 0,
  "url": "https://Snippets-API.briceidamariscal.repl.co/snippets/hello"
}

- Make GET:

curl --location --request GET 'https://Snippets-API.briceidamariscal.repl.co/snippets/hello'


GET Request Response:
{
  "expires_at": "2020-05-18T20:42:14.726913",
  "name": "hello",
  "snippet": "hello there test",
  "likes": 0,
  "url": "https://Snippets-API.briceidamariscal.repl.co/snippets/hello"
}



- Make PUT:

curl --location --request PUT 'https://Snippets-API.briceidamariscal.repl.co/snippets/like' \
--header 'Content-Type: application/json' \
--data-raw '{
	
	"name": "hello"
}'


PUT Request Response:
{
  "expires_at": "2020-05-18T23:25:00.032235",
  "likes": 1,
  "name": "hello",
  "snippet": "hello there test",
  "url": "https://Snippets-API.briceidamariscal.repl.co/snippets/hello"
}

```

## Tests:
wip
Tested manually using Postman 
