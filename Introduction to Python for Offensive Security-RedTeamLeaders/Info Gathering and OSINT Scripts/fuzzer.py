import httpx

web_target = input("input target: ")


with open("../../scripts/test files/subdomains-top1million-110000.txt") as f:
    for item in f:
        sub = item.strip()
        url = f"https://{web_target}/{sub}"

        try:
            web = httpx.get(url, timeout=10)
            if web.status_code == [200,201,204,403,302]:
                print(f"[+]{url}")
        except:
            pass