class OrderData:
    # Базовый шаблон заказа
    BASE_ORDER = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha"
    }
    
    ORDERS = [
        {**BASE_ORDER, "color": ["BLACK"]},
        {**BASE_ORDER, "color": ["GREY"]},
        {**BASE_ORDER, "color": ["BLACK", "GREY"]},
        BASE_ORDER.copy()
    ]

    
 