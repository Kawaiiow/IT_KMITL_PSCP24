"""CIA want to know your location"""
import re

def main():
    """void"""
    msg = str(input()).lower()
    mac_pattern_a = r"^([a-f0-9]{2}\-){5}([a-f0-9]{2})$"
    mac_pattern_b = r"^([a-f0-9]{2}\:){5}([a-f0-9]{2})$"
    mac_pattern_c = r"^([a-fA-F0-9]{4}\.){2}([a-f0-9]{4})$"

    if re.search(mac_pattern_a, msg):
        print("VALID 1")
    elif re.search(mac_pattern_b, msg):
        print("VALID 2")
    elif re.search(mac_pattern_c, msg):
        print("VALID 3")
    else:
        print("ERROR")
main()
