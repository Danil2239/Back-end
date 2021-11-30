import requests

def get_method(url):#метод для get запроса
    try:
        response = requests.get(url)#ответ
        response.raise_for_status()#проверка статуса ответа (200,404 и тд.)
    except requests.models.HTTPError as http_err:#если ошибка http (неправильный адрес или сервер недоступен) 
        return f'HTTP error occurred: {http_err}'#то вернуть код и ошибку
    except Exception as err:#какая либо другая ошибка вернуть наименование ошибки (например введена не ссылка а просто число)
        return f'Other error occurred: {err}'
    else:
        return response.json()#если ошибок нет то вернуть ответ от api в формате json

    
def post_method(url, data):
    try:
        response = requests.post(url, json = data, headers = {"Content-Type": "application/json"})
        print(response.json())
        response.raise_for_status()
    except requests.models.HTTPError as http_err:
        return f'HTTP error occurred: {http_err}'
    except Exception as err:
        return f'Other error occurred: {err}'
    else:
        return response.json()

def put_method(url, data):
    try:
        response = requests.put(url, json = data)
        response.raise_for_status()
    except requests.models.HTTPError as http_err:
        return f'HTTP error occurred: {http_err}'
    except Exception as err:
        return f'Other error occurred: {err}'
    else:
        return response.json()

def delete_method(url):
    try:
        response = requests.delete(url)
        response.raise_for_status()
    except requests.models.HTTPError as http_err:
        return f'HTTP error occurred: {http_err}'
    except Exception as err:
        return f'Other error occurred: {err}'
    else:
        return response.json()




