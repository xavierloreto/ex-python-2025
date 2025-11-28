import requests
import sys

def main():
    bitcoin_url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    try:
        number_of_bitcoins_str = sys.argv[1]
        number_of_bitcoins = float(number_of_bitcoins_str)

        bitcoin_request = requests.get(bitcoin_url)
        bitcoin_data = bitcoin_request.json()

        rate = bitcoin_data["bpi"]["USD"]["rate_float"]

        amount = rate * number_of_bitcoins

        print(f"${amount:,.4f}")

    except IndexError:
        print("Missing command-line argument ")
        sys.exit(1)

    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    except requests.RequestException:
        print("Error1")

    except requests.exceptions.JSONDecodeError:
        print("Error")


main()

