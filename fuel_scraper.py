import requests
import feedparser
from pprint import pprint

north_river = 25
south_river = 26
east_hills = 27


def fuel_day(which_day, which_fuel):

    if which_day == 'today':
        response = requests.get('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Region={}&Day=today'.format(which_fuel))
    else:
        response = requests.get('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Region={}&Day=tomorrow'.format(which_fuel))

    feed = feedparser.parse(response.content)
    # print(which_fuel)
    # pprint(feed, indent=4)

# Create a list of dictionaries
    fuel_output = []

    for entry in feed["entries"]:
        new_dict = {}
        new_dict["Price"] = entry["price"]
        new_dict["Brand"] = entry["brand"]
        new_dict["Address"] = entry["address"]
        new_dict["Day"] = which_day
        fuel_output.append(new_dict)
    return fuel_output
    # fuel_output.append(entry["price"])

fuel_today = fuel_day('today', east_hills)
fuel_tomorrow = fuel_day('tomorrow', east_hills)


# Test print of fuel dictionaries
# print(fuel_today)
# print(fuel_tomorrow)

all_fuel = fuel_today+fuel_tomorrow

# Sorting by price
def by_price(item):
    return item['Price']


sorted_fuel_output = sorted(all_fuel, key=by_price)

# Printing output of sorted_fuel_output
# pprint(sorted_fuel_output, indent =4)

""" Empty string fuel_data_row_string is created, a for loop iterates over fuel_data which contains the list 
of dictionaries and adds the value for keys price, brand, address and day into a row which is contained in a string"""
fuel_data_row_string = ""

for value in sorted_fuel_output:
    fuel_data_row_string += """
        <tr>
            <td>{Price} </td><td>{Brand} </td><td>{Address} </td><td>{Day}</td>
        </tr>
    """.format(**value)

# Printing output of fuel_data_row_string
# print(fuel_data_row_string)

# Formats the html data
fuel_html = "<html><title>Fuel Report</title><body><tbody><table>" + fuel_data_row_string + "</table></tbody></body></html>"

# Printing output of fuel_html
# print(fuel_html)

# Opens and creates a file named fuel_report.html with write access.
fuel_file = open('fuel_report.html', 'w')

# Writes the the data from fuel_data_html into the fuel_report.html file.
fuel_file.write(fuel_html)

# Closes fuel_report.html.
fuel_file.close()


