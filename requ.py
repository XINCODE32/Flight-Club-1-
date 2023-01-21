import requests
API_USERS = "https://api.sheety.co/4a7d01ebea027df987001db75b175032/flights/users"
API_PRICE = "https://api.sheety.co/4a7d01ebea027df987001db75b175032/flights/prices"

class Sheety:
    def post_users(self, first, last, email):
      new_user = {
        "user": {
          "firstName": first,
          "lastName": last,
          "email": email
        }
      }
      response_user = requests.post(url=API_USERS, json=new_user)
      response_user.raise_for_status()
    