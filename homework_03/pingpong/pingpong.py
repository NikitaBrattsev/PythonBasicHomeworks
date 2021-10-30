import requests
from fastapi import FastAPI, Body

app = FastAPI()


@app.get("/ping/")
def read_ping():
    return {"message": "pong"}


@app.post("/checksite/")
def get_url(url: str = Body(...)):
    """
    String like http://site.name should be provided.

    Return http status code.
    """
    try:
        r = requests.head(url, verify=False, timeout=5)
    except requests.exceptions.ConnectionError:
        return {"site": url, "message": "Not found!"}
    except (requests.exceptions.MissingSchema, requests.exceptions.InvalidURL):
        return {"site": url, "message": "Invalid format, should begin from 'http://' or 'https://'"}
    except Exception as err:
        print(err)
        return {"message": "Something goes wrong :("}
    return {"site": url, "status": r.status_code}
