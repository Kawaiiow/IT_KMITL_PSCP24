"""vidg"""

def main():
    """void"""
    nick = input()
    na = input()
    ho = input()
    age = float(input())
    sa = float(input())
    de = float(input())

    if na in ("Yes", "True") and ho in ("Yes", "True") and age >= 16 \
        and sa <= 840000 and de <= 500000:
        print(f"Congratulations! {nick} is qualified to receive\
 a digital wallet amount of 10,000 baht, sponsored by all taxpayers in Thailand.")
    else:
        print(f"Unfortunately, {nick} is not qualified.")
main()
