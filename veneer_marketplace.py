class Art:
    """ Class that holds art piece attributes """

    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return '{artist}. "{title}". {year}, {medium}. {owner}, {location}.'.format(artist=self.artist, title=self.title, year=self.year, medium=self.medium, owner=self.owner.name, location=self.owner.location)


class Marketplace:
    """ Class that holds listings for art to be bought and sold """

    def __init__(self):
        self.listings = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, expired_listing):
        if expired_listing in self.listings:
            self.listings.remove(expired_listing)

    def show_listings(self):
        for listing in self.listings:
            print(listing)


class Listing:
    """ Class holds listing attributes"""

    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return '{art_name} ${price}'.format(art_name=self.art.title, price=self.price)


class Client:
    """ Class that holds client information """

    def __init__(self, name, location, is_museum):
        self.name = name
        self.location = location
        self.is_museum = is_museum

    def sell_artwork(self, artwork, price):
        if artwork.owner.name == self.name:
            listing = Listing(artwork, price, self.name)
            veneer.add_listing(listing)

    def buy_artwork(self, artwork):
        if artwork.owner.name != self.name:
            for listing in veneer.listings:
                if artwork == listing.art:
                    art_listing = artwork
                    art_listing.owner = self
                    veneer.remove_listing(listing)


# Create new Veneer marketplace object
veneer = Marketplace()
veneer.show_listings()

# Create first client
edytta = Client('Edytta Halpirt', 'Private Collection', is_museum=False)

# Art class test
girl_with_mandolin = Art(
    'Picasso, Pablo', 'Girl with a Mandolin (Fanny Tellier)', 'oil on canvas', 1910, edytta)
# print(girl_with_mandolin)

# Create second client
moma = Client('The MOMA', 'New York', is_museum=True)

# Edytta sells art test
edytta.sell_artwork(girl_with_mandolin, '$6M (USD)')
# veneer.show_listings()

# MOMA buys art test
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
veneer.show_listings()

# This is a test
