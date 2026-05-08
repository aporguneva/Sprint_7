class ResponseMessages:
    #Создание курьера
    CREATE_COURIER_SUCCESS = {"ok": True} # ответ об успешном создании курьера

    ERROR_NOT_ENOUGH_DATA = "Недостаточно данных для создания учетной записи" 
    ERROR_LOGIN_EXISTS= "Этот логин уже используется. Попробуйте другой."
 
    #Логин курьера
    ERROR_ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
    ERROR_LOGIN_NOT_ENOUGH_DATA = "Недостаточно данных для входа"


class ResponseFields:
    COURIER_ID = "id" #ответ логин курьера
    TRACK = "track" #ответ создание заказа
    ORDERS = "orders" #ответ получение списка заказа

