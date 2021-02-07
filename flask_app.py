import json
import requests
import pandas as pd
from flask import Flask, session, render_template, request, redirect, url_for

URL = "https://www.alphavantage.co/query?"
PARAMS = {}

app = Flask(__name__)
app.secret_key = "super secret key"

def generate_list_dict_from_df(file_name):
    if file_name != "nasdaq.csv":
        return False
    else:
        stock_df = pd.read_csv(file_name)
        if check_df_cols(stock_df):
            stock_df_symbol_name = stock_df[["Symbol", "Name"]]
        else:
            return False
        list_dic_symbol_name = stock_df_symbol_name.to_dict('records')
        return list_dic_symbol_name

def check_df_cols(df):
    if "Symbol" in df.columns and "Name" in df.columns:
        return True

def make_request(function_name, data_key):
    if function_name == "SYMBOL_SEARCH":
        PARAMS["keywords"] = PARAMS["symbol"]
        del PARAMS["symbol"]
    PARAMS["function"] = function_name
    content = requests.get(URL, PARAMS).json()
    data = content[data_key]
    return data

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user_key = request.form["api-key"]
        if user_key:
            session["user_api_key"] = user_key
            PARAMS["apikey"] = user_key
            return redirect(url_for("user"))
        else:
            mssg = "Please enter your API key."
            return render_template("login.html", mssg = mssg)
    else:
        return render_template("login.html")

@app.route("/user", methods=["POST", "GET"])
def user():
    if request.method == "POST":
        symbol_name = request.form["company"]
        symbol_name_list = symbol_name.split("          ")
        symbol = symbol_name_list[0]
        session["symbol"] = symbol
        return redirect(url_for("symbol"))
    else:
        if "user_api_key" in session:
            user = session["user_api_key"]
            file_name = "nasdaq.csv"
            list_dic_symbol_name = generate_list_dict_from_df(file_name)
            return render_template("user.html", list_symbol_name = list_dic_symbol_name)
        else:
            return redirect(url_for("login"))

@app.route("/symbol", methods=["POST", "GET"])
def symbol():
    if request.method == "POST":
        symbol = session["symbol"]
        PARAMS["symbol"] = symbol
        button_value = request.form['submit_button']

        if button_value == "Additional Details":
            function_name = "SYMBOL_SEARCH"
            data_key = "bestMatches"
            file_name = "details.html"

        elif button_value == "Historical Prices Daily":
            function_name = "TIME_SERIES_DAILY"
            data_key = "Time Series (Daily)"
            file_name = "timeframe.html"

        elif button_value == "Historical Prices Weekly":
            function_name = "TIME_SERIES_WEEKLY"
            data_key = "Weekly Time Series"
            file_name = "timeframe.html"

        elif button_value == "Current Quote":
            function_name = "GLOBAL_QUOTE"
            data_key = "Global Quote"
            file_name = "quote.html"

        else:                                       # if button_value == "Indicator":
            return redirect(url_for("indicator"))

        data = make_request(function_name, data_key)

        if function_name == "SYMBOL_SEARCH":
            for match_data in data:
                if match_data["1. symbol"] == symbol:
                    data = match_data

        return render_template(file_name, data = data)
    else:
        return render_template("symbol.html")

@app.route("/indicator", methods=["POST", "GET"])
def indicator():
    if request.method == "POST":
        symbol = session["symbol"]
        PARAMS["symbol"] = symbol
        PARAMS["interval"] = "monthly"
        PARAMS["time_period"] = "200"
        PARAMS["series_type"] = "high"
        button_value = request.form['submit_button']
        function_name = button_value
        data_key = "Technical Analysis: " + function_name
        file_name = "function.html"
        data = make_request(function_name, data_key)
        return render_template(file_name, data = data, function = function_name)
    else:
        return render_template("indicator.html")

@app.route("/logout", methods=["GET"])
def logout():
    session.pop("user_api_key", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)


