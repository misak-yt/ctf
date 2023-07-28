from tqdm import tqdm
import requests
import base64

url = "http://mercury.picoctf.net:15614/"

s = requests.Session()
s.get(url)
cookie = s.cookies["auth_name"]
decoded_cookie = base64.b64decode(cookie)
raw_cookie = base64.b64decode(decoded_cookie)


def solve():
    for position_idx in tqdm(range(0, len(raw_cookie))):
        for bit_idx in range(0, 8):
            bitflip_guess = (
                raw_cookie[0:position_idx]
                + ((raw_cookie[position_idx] ^
                   (1 << bit_idx)).to_bytes(1, "big"))
                + raw_cookie[position_idx + 1:]
            )

            guess = base64.b64encode(base64.b64encode(bitflip_guess)).decode()
            r = requests.get(url, cookies={"auth_name": guess})
            if "picoCTF{" in r.text:
                print(f"Admin bit found in byte {position_idx} bit {bit_idx}.")
                print("Flag: " + r.text.split("<code>")[1].split("</code>")[0])
                return
        
if __name__ == '__main__':
    solve()