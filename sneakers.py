class ShoeContainer:
    """The class `ShoeContainer` initializes an empty list `shoe_closet` to store
    shoes.
    """
    def __init__(self):
        self.shoe_closet = []
    
    def show_items(self):
        return self.shoe_closet

    def add_shoe(self, shoe):
        self.shoe_closet.append(shoe)
        return self.shoe_closet


class Footwear:

    def __init__(self, colour, brand, style):
        self.colour = colour
        self.brand = brand
        self.style = style
    

    def __repr__(self):
        shoe = f"Footwear({self.colour}, {self.brand}, {self.style})"
        return shoe
    

    def __str__(self):

        shoe = ''
        shoe += f"\n{'='*50}\n" # header
        shoe += f"Colour: {self.colour}\n" # item colour
        shoe += f"{'-'*50}\n"
        shoe += f"Brand: {self.brand}\n" # item brand
        shoe += f"{'-'*50}\n"
        shoe += f"Style: {self.style}\n" # item style
        shoe += f"{'='*50}\n" # footer

        return shoe

test_closet = ShoeContainer()
test_shoe = Footwear("Black", "Clarks", "Boot")
second_test_shoe = Footwear("Silver", "Nike", "Running")
print(test_shoe, second_test_shoe)
print(test_closet.show_items())
test_closet.add_shoe(test_shoe)
print(test_closet.show_items())
test_closet.add_shoe(second_test_shoe)
print(test_closet.show_items())