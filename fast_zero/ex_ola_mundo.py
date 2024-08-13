from fastapi import FastAPI
from fastapi.responses import HTMLResponse

html = FastAPI()


@html.get(
    '/olamundo',
    response_class=HTMLResponse,
)
def retorne_ola_mundo():
    return """
    <html>
        <head>
            <title>nosso primeiro olá mundo</title>
        </head>
        <body>
            <h1>Olá Mundo!</h1>
        </body>
    </html> """
