import requests
import feedparser
from pprint import pprint


# Region Codes

NORTH_OF_RIVER = 25
SOUTH_OF_RIVER = 26 
EAST_HILLS = 27
ALBANY = 15 
AUGUSTA_MARGARET_RIVER = 28  
BRIDGETOWN_GREENBUSHES = 30 
BOULDER = 1  
BROOME = 2 
BUNBURY = 16 
BUSSELTON_TOWNSITE = 3 
BUSSELTON_SHIRE = 29 
CAPEL = 19 
CARNARVON = 4 
CATABY = 33 
COLLIE = 5
COOLGARDIE = 34 
CUNDERDIN = 35
DONNYBROOK_BALINGUP = 31  
DALWALLINU = 36 
DAMPIER = 6 
DARDANUP = 20 
DENMARK = 37 
DERBY = 38 
DONGARA = 39 
ESPERANCE = 7 
EXMOUTH = 40 
FITZROY_CROSSING = 41 
GERALDTON = 17 
GREENOUGH = 21 
HARVEY = 22 
JURIEN = 42 
KALGOORLIE = 8 
KAMBALDA = 43 
KARRATHA = 9
KELLERBERRIN = 44 
KOJONUP = 45 
KUNUNURRA = 10 
MANDURAH = 18 
MANJIMUP = 32 
MECKERING = 58 
MEEKATHARRA = 46 
MOORA = 47 
MT_BARKER = 48 
MURRAY = 23 
NARROGIN = 11 
NEWMAN = 49 
NORSEMAN = 50 
NORTHAM = 12 
PORT_HEDLAND = 13 
RAVENSTHORPE = 51 
REGANS_FORD = 57 
SOUTH_HEDLAND = 14 
TAMMIN = 53 
WAROONA = 24 
WILLIAMS = 54 
WUBIN = 55 
WUNDOWIE = 59 
YORK = 56 

# Days

TODAY = 'today'
TOMORROW = 'tomorrow'
YESTERDAY = 'yesterday'



# Fuel Types

UNLEADED_PETROL = 1
PREMIUM_UNLEADED = 2 
DIESEL = 4 
LPG = 5 
RON_98 = 6 
E85 = 10 
BRAND_DIESEL = 11



def fuel_day(which_fuel, which_region, which_day):

    if which_day == 'today':
        response = requests.get('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product={}&Region={}&Day=today'.format(which_fuel, which_region))
    else:
        response = requests.get('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product={}&Region={}&Day=tomorrow'.format(which_fuel, which_region))

    feed = feedparser.parse(response.content)
    # print(which_fuel, which_day, which_region)
    # pprint(feed, indent=4)

# Create a list of dictionaries
    fuel_output = []

    for entry in feed["entries"]:
        new_dict = {}
        new_dict["Price"] = entry["price"]
        new_dict["Brand"] = entry["brand"]
        new_dict["Address"] = entry["address"]
        new_dict["Location"] = entry["location"]
        new_dict["Day"] = which_day
        fuel_output.append(new_dict)
    return fuel_output
    # fuel_output.append(entry["price"])

# Sorting by price
def by_price(item):
    return item['Price']

def  fuel_table_data():

    fuel_today = fuel_day(UNLEADED_PETROL, NORTH_OF_RIVER, TODAY)
    fuel_tomorrow = fuel_day(UNLEADED_PETROL, NORTH_OF_RIVER, TOMORROW)
    all_fuel = fuel_today+fuel_tomorrow
    sorted_fuel_output = sorted(all_fuel, key=by_price)
    return sorted_fuel_output


# Test print of fuel dictionaries
# print(1, fuel_today, TODAY)
# print(fuel_tomorrow)

fuel_output = fuel_table_data()






# Printing output of sorted_fuel_output
# pprint(sorted_fuel_output, indent =4)

""" Empty string fuel_data_row_string is created, a for loop iterates over fuel_data which contains the list 
of dictionaries and adds the value for keys price, brand, address and day into a row which is contained in a string"""


def create_fuel_table():

    fuel_data_row_string = ""

    for value in fuel_output:
        fuel_data_row_string += """
            <tr>
                <td>{Price} </td><td>{Brand} </td><td>{Address} </td><td>{Location} </td><td>{Day}</td>
            </tr>
        """.format(**value)
    return fuel_data_row_string

# create_fuel_table()

# Printing output of fuel_data_row_string
# print(fuel_data_row_string)

# Formats the html data
fuel_html = "<html><title>Fuel Report</title><body><tbody><table>" + create_fuel_table() + "</table></tbody></body></html>"

# Printing output of fuel_html
# print(fuel_html)

# Opens and creates a file named fuel_report.html with write access.
fuel_file = open('fuel_report.html', 'w')

# Writes the the data from fuel_data_html into the fuel_report.html file.
fuel_file.write(fuel_html)

# Closes fuel_report.html.
fuel_file.close()

print("Run succesfully!")
# Get all regions as variables so they can be used by the function def fuel_day(which_day, which_fuel) Add the Region, Fuel type (needs to be added to function to be used) and day. Use a settings.py file (CONSTANCE?)

# Use Itertools to get all combinations of URLs

# Read up on list comprehension

# Read up on Python Context Manager
