import os
import csv


class ManagementSuite:
    # this will be used to manage our portfolio, clients, vendors, buyers, bids....

    def __init__(self):
        self.portfolio = {}
        self.vendors = {}
        self.buyers = {}

    def add_property(self, property_dict):
        # set up a mapping to set which subclass will be created..
        type_class_map = {'house': House,
                          'apartment': Apartment}

        # set up a variable to hold the type of Class and look it up using above map,
        # and the 'type' key in the property_dict
        prop_obj = type_class_map[property_dict['type']]

        # add a new instance of the chosen class to the portfolio dict of our Management_Suite object
        self.portfolio[property_dict['id']] = prop_obj(property_dict)

    def list_portfolio(self):
        for k, v in self.portfolio.items():
            print(v.address, "at price", v.reserve)

class Property:
    def __init__(self, attributes):
        # attributes is a dict of all the important info about the property
        self.portfolio_num = attributes['id']
        self.vendor = attributes['vendor']
        self.type = attributes['type']
        self.address = attributes['address']

        self.num_rooms = attributes['num_rooms']
        self.bathrooms = attributes['bathrooms']
        self.size = attributes['size']
        self.parking_spots = attributes['parking_spots']

        self.reserve = attributes['price']
        self.cash_buyer_preferred = attributes['cash_buyer_preferred']
        self.sale_type = attributes['sale_type']

        self.bids = {}

    def sales_pitch(self):
        op_str = "This is a beautiful {type} with a generous {size} square metres" \
                 "including {num_rooms} rooms and {bathrooms} bathrooms. Conveniently " \
                 "located at {address}, the reserve is set at {reserve} euro.".format(**self.__dict__)
        return op_str

    def make_bid(self, buyer_id, amount):
        # first check if it's the highest bid.....
        if amount > self.get_highest_bid:
            print("This is the highest bid!")
        else:
            print("You need to go a bit higher...")
        # add to bid list - insert in list of bids for that buyer
        if self.check_previous_bid(buyer_id):
            self.bids[buyer_id].append(amount)
        else:
            self.bids[buyer_id] = [amount]

    def check_previous_bid(self, buyer_id):
        if buyer_id in self.bids.keys():
            return True
        else:
            return False

    @property
    def get_highest_bid(self):
        all_bids = []
        for bid_lists in self.bids.values():
            all_bids += bid_lists
        return max(all_bids)


class Apartment(Property):
    def __init__(self, attributes):
        super().__init__(attributes)

        self.floor = attributes['level']
        self.has_lift = attributes['has_lift']
        self.has_balcony = attributes['has_balcony']
        self.maintenance_fee = attributes['maintenance_fee']


class House(Property):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.floors = attributes['floors']
        self.garden = attributes['garden_size']
        self.attic_conversion = attributes['attic_conversion']


def main():
    house_12345 = {"id": 12345,
                  'vendor': 273,
                  'type': 'house',
                  'address': '5, Sylvan Avenue, Templeogue',
                  'num_rooms': 7,
                  'bathrooms': 3,
                  'size': 156,
                  'parking_spots': 2,
                  'price': 560000,
                  'cash_buyer_preferred': True,
                  'sale_type': 'Auction',
                  'floors': 2,
                  'garden_size': 130,
                  'attic_conversion': True,
                  }

    apt_23443 = {"id": 23443,
                  'vendor': 543,
                  'type': 'apartment',
                  'address': '34, Elysian Towers, Stillorgan',
                  'num_rooms': 5,
                  'bathrooms': 2,
                  'size': 80,
                  'parking_spots': 0,
                  'price': 230000,
                  'cash_buyer_preferred': False,
                  'sale_type': 'Private Treaty',
                  'level': 3,
                  'has_lift': True,
                  'has_balcony': True,
                  'maintenance_fee': 1200,
                }

    new_properties = [house_12345, apt_23443]

    # setup new management suite..
    micks_auctioneers = ManagementSuite()

    for p in new_properties:
        micks_auctioneers.add_property(p)

    micks_auctioneers.list_portfolio()


if __name__ == '__main__':
    main()
