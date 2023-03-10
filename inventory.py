# ========The beginning of the class==========
class Shoe:
    # Method that initialise the Shoe object values
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # this method returns the cost of the shoes
    def get_cost(self):
        return self.cost

    # this method returns the quantity of the shoes
    def get_quantity(self):
        return self.quantity

    def update_quantity(self, amount):
        self.quantity += amount


    # this method returns a string representation of class
    def __str__(self):
        return f"Country: {self.country}\n" \
               f"Code: {self.code}\n" \
               f"Product: {self.product}\n" \
               f"Cost: {self.cost}\n" \
               f"Quantity: {self.quantity}\n"


# =============Shoe list===========
shoe_list = []


# ==========Functions outside the class==============

# this function will open the file inventory.txt and read the data from this file.
# It will create a shoe object and add this to the shoe list.
def read_shoes_data():
    file = None
    try:
        file = open("inventory.txt", "r")

        # skip first line
        next(file)

        for line in file:
            parts = line.split(",")
            try:
                country = parts[0]
                code = parts[1]
                product = parts[2]
                cost = int(parts[3])
                quantity = int(parts[4])

                shoe = Shoe(country, code, product, cost, quantity)

                shoe_list.append(shoe)

            # Error handling using the try-except
            except ValueError:
                print("Line did not contain valid data")
    except FileNotFoundError:
        print("The file inventory.txt that you trying to open does not exist")
    finally:
        if file is not None:
            file.close()

# function that ask the user for the data about a shoe and create a shoe object and add to the shoe list
def capture_shoes():
    country = input("Please enter the country where the shoes are from")
    code = input("Please enter the code of the shoe")
    product = input("Please enter the name of the product")

    # error handling using the 'try' and 'except' inside the While loop
    while True:
        try:
            cost = int(input("Please enter the cost of the product"))
            break
        except ValueError:
            print("Enter valid cost as a number!")

    while True:
        try:
            quantity = int(input("Please enter the quantity of the product"))
            break
        except ValueError:
            print("Enter valid quantity as a number!")

    shoe = Shoe(country, code, product, cost, quantity)

    shoe_list.append(shoe)

# this function will go through the shoe list and print all the shoes
def view_all():
    for shoe in shoe_list:
        print(shoe)

# this function will find the shoe object with the lowest stock quantity, which are the shoes that need to be re-stocked
def re_stock():
    lowest_stock_shoe = shoe_list[0]

    for i in range(1, len(shoe_list)):
        shoe = shoe_list[i]
        if shoe.quantity < lowest_stock_shoe.quantity:
            lowest_stock_shoe = shoe

    print(f"The lowest stock shoe is:\n{lowest_stock_shoe}")

    # error handling using the 'try' and 'except' inside the While loop
    while True:
        try:
            quantity = int(input("Enter the quantity to update or '-1' to cancel"))
            if quantity != -1:
                lowest_stock_shoe.update_quantity(quantity)
            break
        except ValueError:
            print("Invalid entry, please enter quantity as a number")

# function that will search for a shoe from the shoe list by using the shoe code and return the shoe object
def seach_shoe():
    shoe_code = input("Enter a shoe code")

    for shoe in shoe_list:
        if shoe.code == shoe_code:
            return shoe

    print(f"Shoe not found for shoe code {shoe_code}")

# function that will calculate the total value for each item.
def value_per_item():

   for shoe in shoe_list:
       value = shoe.cost * shoe.quantity
       print(f"Code: {shoe.code}\n"
             f"Product: {shoe.product}\n"
             f"Total value: {value}\n")

# function that will determine the product with the highest quantity
def highest_qty():
    highest_stock_shoe = shoe_list[0]
    for i in range(1, len(shoe_list)):
        shoe = shoe_list[i]
        if shoe.quantity > highest_stock_shoe.quantity:
            highest_stock_shoe = shoe
    print(f"This following shoe {highest_stock_shoe} is for sale!")


# ==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

while True:
    menu = input('''Select one of the following Options below:
        
        rsd - read shoe data
        cs - capture shoe
        va - view all
        rs - re-stock
        ss - search shoe
        vpi - value per item
        hq - highest quantity
        e - Exit
        : ''').lower()

    if menu == "rsd":
        read_shoes_data()

    elif menu == "cs":
        capture_shoes()

    elif menu == "va":
        view_all()

    elif menu == "rs":
        re_stock()

    elif menu == "ss":
        shoe = seach_shoe()
        print(shoe)

    elif menu == "vpi":
        value_per_item()

    elif menu == "hq":
        highest_qty()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
