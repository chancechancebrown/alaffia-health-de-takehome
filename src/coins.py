import requests
from flask import Flask, request, jsonify
from multiprocessing import Value
import csv
import json
import logging


counter = Value("i", 0)
app = Flask(__name__)
app.config["DEBUG"] = False
logging.basicConfig(level=logging.INFO)


@app.route("/")
def counter_func():
    """Function index returns global counter associated with process"""
    with counter.get_lock():
        counter.value += 1
    return counter.value


def query_coingecko(coin):
    """Function query_coingecko takes a coin name and returns the set of unique markets that coin appears on
    Inputs:
        coin(string): Coin name
    Outputs:
        coin_dict(dict): Dict contain key-value pair of {coin:[markets]}"""
    markets = []
    coin = coin.lower()  ## CG API takes only lowercase names for crypto
    response = requests.get(f"https://api.coingecko.com/api/v3/coins/{coin}/tickers")
    if response.status_code == 200:
        response = response.json()
        for item in response["tickers"]:
            markets.append(item.get("market").get("identifier"))
        return {coin: list(set(markets))}
    else:
        return {}


@app.route("/", methods=["POST", "GET"])
def coin_app():
    count = counter_func()
    post_data = request.get_data()
    coins = []
    if request.content_type == "text/csv":
        post_data = post_data.decode("utf-8")
        coins = post_data.split("\n")
        coins.remove("coins")
        app.logger.info("CSV: " + str(coins))
    if request.content_type == "application/json":
        coins = json.loads(post_data)["coins"]
        app.logger.info("JSON: " + str(coins))

    try:
        coin_markets = json.load(open("data/coin_markets.json"))
    except:
        coin_markets = {}
    coin_template = {}

    for coin in coins:
        try:
            coin_data = query_coingecko(coin)
            coin_template[coin] = {
                "id": coin,
                "exchanges": coin_data[coin],
                "task_run": count,
            }
        except KeyError:
            coin_template = {}
        coin_markets.update(coin_template)
    with open("data/coin_markets.json", "w") as outfile:
        json.dump(coin_markets, outfile)
    return ""


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3333)
