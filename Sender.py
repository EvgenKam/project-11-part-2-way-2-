#Камышев Евгений 10 когорта группа mars 11 спринт часть 2
import configuration
import requests
import data
#Создание заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body,
                         headers=data.headers)
#Получение трэка после создания заказа
def get_order_with_track(track):
	return requests.get(configuration.URL_SERVICE + configuration.TRACK_PATH + str(track),
	                    headers = data.headers)
