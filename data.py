import generators


class Url:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru/'  # Main Url Yandex Scooter
    CREATE_COURIER = 'api/v1/courier'  # Courier account creation handle
    COURIER_LOGIN = 'api/v1/courier/login'  # Courier login handle
    COURIER_DELETE = 'api/v1/courier/'  # Courier Delete handle
    CREATE_ORDER = 'api/v1/orders'  # Order creation handle
    GET_ORDER_LIST = 'api/v1/orders'  # Get order list handle
    ORDER_CANCEL = 'api/v1/orders/cancel?track='  # Order cancel handle
    TRACK_ORDER = '/api/v1/orders/track?t='  # Track order handle


class DataForOrder:
    order_data = {"firstName": "Ivan",
                  "lastName": "Generalov",
                  "address": "Perovskaya 16b",
                  "metroStation": 2,
                  "phone": "+79166666666",
                  "rentTime": 3,
                  "deliveryDate": "2024-09-13",
                  "comment": "Call me before deliver"
                  }
    scooter_color = [['BLACK'], ['GREY'], (['BLACK'], ['GREY']), ['']]


class DataForRegistration:
    reg_data = [{'password': generators.password_generator(), 'first_name': generators.name_generator()},
                {'login': generators.login_generator(), 'first_name': generators.name_generator()}]


class ResponseBody:
    COURIER_CREATION_SUCCESS = {'ok': True}
    COURIER_NAME_ALREADY_EXIST = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}  #
    COURIER_REGISTRATION_NOT_ENOUGH_DATA = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
    COURIER_ACCOUNT_NOT_FOUND = {'code': 404, 'message': 'Учетная запись не найдена'}
    COURIER_LOGIN_NOT_ENOUGH_DATA = {'code': 400, 'message': 'Недостаточно данных для входа'}


class Flags:
    SUCCESSFUL_ORDER_CREATION = 'track'  # Successful order creation flag
    SUCCESSFUL_GET_ORDER_LIST = 'orders'  # Successful get order list flag
