# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# RAyeni,11.27.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
input_product = ""  # user input: product name
input_price = 0.0  # user input: product price
strChoice = ""  # Captures the user option selection
strStatus = ""  # Status message returned by function


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        RAyeni,11.27.2020,Modified code to complete assignment 8
    """

    # Constructor
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        RAyeni,11.27.2020,Modified code to complete assignment 8
    """

    @staticmethod
    def read_data_from_file(file_name, list_of_product_objects):
        """ Read data from file and into a list of objects """

        # try except clause to hand FileNotFound errors
        try:
            # clear list parameter
            list_of_product_objects.clear()
            # open file parameter
            file = open(file_name, "r")
            # loop through lines in file
            for line in file:
                # split each line and assign each field to variables
                # item and price
                item, price = line.split(",")
                # use item and price as arguments to create
                # Product object. Append object to list.
                list_of_product_objects.append(Product(item.strip(), float(price.strip())))
            # close file
            file.close()
            return list_of_product_objects
        except FileNotFoundError:
            print("\nFile is not present, skipping the reading process...\n")

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Write data to file """

        # open file
        file = open(file_name, "w")
        # for each object in list do the following...
        for obj in list_of_product_objects:
            # concatenate the object's name and list and write to file
            file.write(obj.product_name + "," + str(obj.product_price) + "\n")
        # after loop ends, close file
        file.close()
        # return confirmation message
        return '\nData saved to ' + file_name + '.'


class ListProcessor:
    """ Contains functions to perform list operations """

    @staticmethod
    def add_object_to_list(item, price, list_of_product_objects):
        """ use item and price parameters to create object
            and add to list
        """

        # The argument creates an object from the Product class, and is appended
        # to the list (list_of_product_objects).
        list_of_product_objects.append(Product(item.strip().capitalize(), price))
        return '\nProduct added.'

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Contains Input and Output Tasks """

    @staticmethod
    def print_menu_options():
        print("""
        Product List Application

        Main Menu:
        1. Print Current Products in List
        2. Add Product to List
        3. Save Product List to File and Exit
        4. Exit Program
        """)
        print()

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def get_current_data_from_list(list_of_objects):
        """ Shows current data in list """

        print("******* Current Products in List: *******")
        for obj in list_of_objects:
            print(obj.product_name + " (" + str(obj.product_price) + ")")
        print("*****************************************")

    # Get product data from user
    @staticmethod
    def input_product_data():
        """ Ask user for product data.
            Returns product and price to main part of script
        """
        i_product = input("Enter Product: ")
        i_price = float(input("Enter Price: "))
        return i_product, i_price

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press [Enter] to continue. ')

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)

while (True):
    # Show user a menu of options
    IO.print_menu_options()
    # Get user's menu option choice
    strChoice = IO.input_menu_choice()

    # Show user current data in the list of product objects
    if strChoice.strip() == '1':
        IO.get_current_data_from_list(lstOfProductObjects)
        IO.input_press_to_continue()
        continue

    # Let user add data to the list of product objects
    elif strChoice.strip() == '2':
        # Call function to input item and price, assign to results to vars
        input_product, input_price = IO.input_product_data()
        # Call function to create product object (item and price) and it to list
        strStatus = ListProcessor.add_object_to_list(input_product, input_price, lstOfProductObjects)
        # Call function to ask user to press enter to continue
        IO.input_press_to_continue(strStatus)
        continue

    # let user save current data to file and exit program
    elif strChoice.strip() == '3':
        # Call function to ask user if they want to save data to file
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            # Call function to save list of product objects to file
            strStatus = FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            IO.input_press_to_continue(strStatus)
            print("Goodbye!")
            break
        else:
            IO.input_press_to_continue("Save Cancelled.")
            continue

    elif strChoice == '4':
        print("\nGoodbye!")
        break

# Main Body of Script  ---------------------------------------------------- #
