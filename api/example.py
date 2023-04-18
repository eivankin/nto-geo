from api.request_helper import APIRequestHelper

if __name__ == '__main__':
    helper = APIRequestHelper("http://192.168.1.62:8888/mapservices/oodb")
    print(helper.get_catalog())
    print(helper.load_object(ids="1"))
