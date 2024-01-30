import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json()
    print('*******' * 10)
    print(categories)
    print('*******' * 10)
    for category in categories:
        print(category)
        print('*******' * 10)
    
    
    