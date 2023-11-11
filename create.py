#Камышев Евгений 10 когорта группа mars 11 спринт часть 2
import Sender
import data

#ПОлучение новго заказа
def get_new_order():
    order_body = data.order_body
    response_order = Sender.post_new_order(order_body)
    return response_order.json

#ПОзитивная проверка присваивания трэка (код 200)
def positive_assert_200():
	track_response = Sender.post_new_order(data.order_body)
	track = track_response.json()["track"]
	return Sender.get_order_with_track(track).status_code

#Тест провеки позитивной проверки 200
#
def test_get_order_with_track_code_200():
	assert positive_assert_200() == 200