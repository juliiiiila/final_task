import requests


class PetstoreUser:
    def get_headers(self):
        headers = {
            'Accept': 'application/json'
        }
        return headers

    def __init__(self):
        self.base_url = 'https://petstore.swagger.io/v2/user'
        self.headers = self.get_headers()

    def create_user(self):
        url = self.base_url
        json = {
            "id": 1,
            "username": "julia_g",
            "firstName": "Julia",
            "lastName": "Gahovich",
            "email": "Ty4kayes@yandex.ru",
            "password": "Ty4kayes",
            "phone": "+375298259568",
            "userStatus": 0
        }
        response = requests.request("POST", url, json=json)
        json_response = response.json()
        print(json_response)
        return json_response

    def user_login(self):
        url = self.base_url + '/login'
        params = {
            "username": "julia_g",
            "password": "Ty4kayes"
        }
        response = requests.request("GET", url, headers=self.headers,
                                    params=params)
        json_response = response.json()
        print(json_response)
        return json_response

    def get_user_data(self, username):
        url = self.base_url + f'/{username}'
        response = requests.request("GET", url, headers=self.headers)
        json_response = response.json()
        print(json_response)
        return json_response

    def user_logout(self):
        url = self.base_url + '/logout'
        response = requests.request("GET", url, headers=self.headers)
        json_response = response.json()
        print(json_response)
        return json_response

    def delete_user(self, username):
        url = self.base_url + f'/{username}'
        response = requests.request("DELETE", url, headers=self.headers)
        json_response = response.json()
        print(json_response)
        return json_response


# usr = PetstoreUser()
# usr.create_user()
# usr.user_login()
# usr.get_user_data('julia_g')
# usr.user_logout()
# usr.delete_user('julia_g')
# usr.get_user_data('julia_g')
