import requests


BASE_URL = "http://127.0.0.1:8080/"
ENDPOINT = "api/updates/"


def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    print(r.status_code)
    if r.status_code != 200:
        print("NOT SUCCESSFUL")
    data = r.json()
    for obj in data:
        # print(obj["id"])
        if obj["id"] == 1:
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj["id"]))
            print(r2.json())
    return data


def create_update():
    new_data = {"user": 1, "content": "A new update from requests."}
    r = requests.post(BASE_URL + ENDPOINT, data=new_data)
    print(r.headers)
    # print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text


# print(get_list())
# get_list
print(create_update())
