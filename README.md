## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info

This is a program that converts an amount of money of one currency to another currency using the website 'https://www.xe.com/currencyconverter/'

You must execute it in the console and you must specify the amount of money, the currency to convert and the resulting currency.
It will show a notification with the conversion.

E. G. 200 dollar yen -> 'Convert 200 US Dollars to Japanese Yens'

## Technologies

To execute the code you will need the following packages:

- Selenium 3.141.0

```
$ pip install selenium
```
Selenium is used in this program to go to the URL and scrape the information.

- Argparse 1.4.0

```
$ pip install argparser
```
Argparser is used to parse the information you want to scrape.

- Plyer 2.0.0

```
$ pip install plyer
```
Plyer is used to show the notification.


## Setup

To execute this program go to your console and type one of the following lines:
```
$ python main.py -m amount -t currency_to_convert -c resulting_currency
$ python main.py --money amount --type currency_to_convert --convert resulting_currency
```
