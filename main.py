from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from ukol2 import hvezda
import html

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def ukol():
    return """<h1>Hvězda</h1>
    <form action="/hvezda">
    <input name="symbol">
    <input name="velikost" type="number">
    <button>Nakreslit</button>
</form>
    """

@app.get("/hvezda", response_class=HTMLResponse)
def nakresli(symbol: str, velikost: int):
    obrazek = hvezda(symbol, velikost)
    return f"<pre>{html.escape(obrazek)}</pre>"