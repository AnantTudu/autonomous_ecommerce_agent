import requests


def convert_to_inr(amount: float, currency: str) -> float:

    if currency.upper() == "INR":
        return amount

    url = f"https://open.er-api.com/v6/latest/{currency.upper()}"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    rate = data["rates"]["INR"]

    converted_amount = amount * rate

    return converted_amount


if __name__ == "__main__":

    usd_amount = convert_to_inr(800, "USD")
    print(f"$800 = ₹{usd_amount:,.2f}")

    inr_amount = convert_to_inr(70000, "INR")
    print(f"₹70,000 = ₹{inr_amount:,.2f}")