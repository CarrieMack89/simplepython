import requests


def get_random_quote():
    response = requests.get("https://api.quotable.io/random", timeout=10)
    if response.status_code == 200:
        data = response.json()
        return '"{}" - {}'.format(data["content"],
                                  data["author"])

    else:
        return "could not retrieve a quote at this time"


def main():
    print("Random Inspirational quote generator")
    while True:
        choice = input(
            "Press 'Enter' to get a new quote or 'Q' to quit: ").strip().lower()
        print(f"Your Choice: {choice}")
        if choice == 'Q':
            print("quitting....")
            break
        quote = get_random_quote()
        print("\n" + quote + "\n")


if __name__ == "__main__":
    main()
