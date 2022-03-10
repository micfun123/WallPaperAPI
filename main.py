from fastapi import FastAPI, Request
from fastapi.responses import FileResponse , RedirectResponse
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os
import random

app = FastAPI(
    title = "HotBeverageAPI",
    description="Gets a HotBeverage from the database. \n This what made by Michael twitter = https://twitter.com/Michaelrbparker ",
    version="0.1.0",
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },

)

app.mount("/static", StaticFiles(directory="static"), name="static")


def getRandomFile(path):
  """
  Returns a random filename, chosen among the files of the given path.
  """
  files = os.listdir(path)
  index = random.randrange(0, len(files))
  return files[index]



@app.get("/")
async def home():
  return RedirectResponse("/docs")

@app.get("/wallpaper")
def tea():
    x = "static/wallpapers/{}".format(getRandomFile("static/wallpapers"))
    return FileResponse(x)
    


@app.get('/json/wallpaper')
async def teajson(request: Request) -> JSONResponse:
    img = "wallpapers/{}".format(getRandomFile("static/wallpapers"))
    img_url = request.url_for('static', path=img)
    return {'img_url': img_url}





   
