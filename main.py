# https://github.com/asalnorouzzade/Practice-40-IP-Address-Validation.git
import re
ip = input().strip()
n = r"([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])"
pattern = rf"^{n}\.{n}\.{n}\.{n}$"

if re.fullmatch(pattern, ip):
    print("Valid IP")
    
else:
    print("Invalid IP")
