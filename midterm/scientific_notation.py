"""SCIENCETIFIC FORM"""
import re

def parse_formular(n: str):
    """void"""
    if (n[0] == "0" and n[1] == ".") or (n[0] == "-" and n[1] == "0" and n[2] == "."):
        n = n.replace(".", "")
        pw = len(re.search(r"[0]+", n).group())
        n = n.lstrip("0")
        if n[0] != '-':
            n = f"{n[0]}.{n[1:]}".rstrip(".")
        else:
            n = n.lstrip("-").lstrip("0")
            n = f"-{n[0]}.{n[1:]}".rstrip(".")
        print(f"{n} x 10^{-pw}")
    else:
        lead = re.search(r"^[-0-9]+", n).group()
        if n.find(".") == -1:
            pw = len(n) - 1
            if lead[0] != "-":
                lead = f"{lead[0]}.{lead[1:].rstrip("0")}"
            else:
                lead = f"{lead[:2]}.{lead[2:].rstrip("0")}"
                pw -= 1
            lead = lead.rstrip(".")
            print(f"{lead} x 10^{pw}")
        elif n.find(".") != -1: # 26 27
            foll = re.search(r"[0-9]+$", n).group()
            pw = len(n[:n.index(".")]) - 1
            if lead[0] != "-":
                print(f"{lead[0]}.{lead[1:]}{foll} x 10^{pw}")
            else:
                pw -= 1
                print(f"{lead[:2]}.{lead[2:]}{foll} x 10^{pw}")

def r_formula(n):
    """void"""
    base = re.search(r"^\S+", n.replace(".", "")).group()
    pw = int(re.search(r"[-0-9]+$", n.replace(".", "")).group())
    if not re.sub(r"[0. ]", "", n[:n.find(" ")]):
        print("0")
        return
    if not pw:
        buf = n[:n.find(" ")]
        print(buf)
        return
    if pw == 1:
        base = re.search(r"^\S+", n.replace(".", "")).group()
        buf = (f"{base[:2]}.{base[2:]}").lstrip("0").rstrip(".").rstrip("0").rstrip(".")
        print(buf if buf[0] != "." else "0" + buf)
    elif pw > 1:
        base = re.search(r"^\S+", n.replace(".", "")).group()
        buf = (f"{base[:pw + 1]}.{base[pw + 1:]}").lstrip("0").rstrip(".")
        buf += ("0" * (pw - len(base) + 1))
        print(buf if buf[0] != "." else "0" + buf)
    elif pw < 0: # 37 38
        base = re.search(r"^\S+", n.replace(".", "")).group()
        if base[0] != "-":
            print(("0." + ("0" * (abs(pw) - 1)) + base))
        else:
            print("-" + ("0." + ("0" * (abs(pw) - 1)) + base[1:]))

def main():
    """void"""
    msg = input()
    if not re.sub(r"[-0.]", "", msg):
        print("0")
        return
    if re.search(r"x", msg):
        r_formula(msg.strip())
    else:
        parse_formular(msg.strip())
main()
