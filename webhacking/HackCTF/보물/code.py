import requests

url = "http://ctf.j0n9hyun.xyz:2025/?page="

default = 1

while True:
    a = requests.get(url + str(default))
    print(default)
    if "HackCTF" in a.text:
        print(a.text)
        break
    default += 1
