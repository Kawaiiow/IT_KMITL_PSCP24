"""iphone"""

def out(price):
    """int"""
    if price:
        print(price)
    else:
        print("Not Available")

def main():
    """iphone"""
    model = str(input())
    storage = input()
    price = 0

    if model in ("iPhone 13 mini", "iPhone 13") and storage in ("128 GB", "256 GB", "512 GB"):
        if storage == "128 GB":
            price = 25900
        elif storage == "256 GB":
            price = 29900
        elif storage == "512 GB":
            price = 37900
        if model == "iPhone 13":
            price += 4000
    elif model in ("iPhone 13 Pro", "iPhone 13 Pro Max") and storage in ("128 GB", "256 GB", \
        "512 GB", "1 TB"):
        if storage == "128 GB":
            price = 38900
        elif storage == "256 GB":
            price = 42900
        elif storage == "512 GB":
            price = 50900
        elif storage == "1 TB":
            price = 58900
        if model == "iPhone 13 Pro Max":
            price += 4000
    out(price)
main()
