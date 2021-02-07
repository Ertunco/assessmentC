# assessment_C

## The Challenge
Simple interface for Alphavantage.co financial data provider API.
```
https://www.alphavantage.co/
```

Build a command line interface or simple flask front-end site that support following features:
    - User provides its own API key that is remembered for the session
    - User can search specific company using and display results that match selection criteria in select list.
        - [symbolsearch](https://www.alphavantage.co/documentation/#symbolsearch)
    - User can select a company and have one of following options for it:
        - display additional details in grid as:
            - symbol, name, type, region, marketOpen, marketClose, timezone, currency, matchScore
        - display historical prices on specific timeframes:
            - intraday as 5m, 15m,.., daily or weekly or monthly (select two)
                - [intraday](https://www.alphavantage.co/documentation/#intraday)
                - [daily](https://www.alphavantage.co/documentation/#daily)
                - [weekly](https://www.alphavantage.co/documentation/#weekly)
                - [monthly](https://www.alphavantage.co/documentation/#monthly)
        - display current quote:
            - [latestprice](https://www.alphavantage.co/documentation/#latestprice)
        - indicator results for it in grid:
            - [technical-indicators](https://www.alphavantage.co/documentation/#technical-indicators)

## Setup
Crete free API key
```
https://www.alphavantage.co/support/#api-key
```

Clone the repository to your local computer
```
git clone https://github.com/Ertunco/assessmentC.git
```

Setup a virtual environment using below command.
```
python -m venv venv
```

Activate the virtual environment using below command.
```
source venv/bin/activate
```

Install the packages using requirements.txt file on the virtual environment.
```
pip install -r requirements.txt
```

## Execution

Run the app using below command.
```
python flask_app.py
```

On the browser, you can click on to enter date input
```
Click Go to Login Page Button
```

## Tests

### unittest
Please run the command below to see the unit tests.
```
python test_data_handler.py
```