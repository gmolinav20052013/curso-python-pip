import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
def get_list():
      return '''
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    '''

@app.get('/listas')
def get_list():
    return [1,2,3,]

@app.get('/contacts')
def get_contactos():
    return {'name': 'Platzi'}

def run():
    store.get_categories()
    
if __name__ == '__main__':
    run()    