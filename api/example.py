from api.request_helper import APIRequestHelper

if __name__ == '__main__':
    helper = APIRequestHelper("http://192.168.1.62:8888/mapservices/oodb")
    print(helper.get_catalog())
    print(len(helper.load_object(
        bbox="34.85542678861543,66.06507873609485,39.760146455994175,67.71469879171593").features))
