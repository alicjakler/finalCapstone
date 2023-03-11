Capstone Project- OOP

This project is to teach me how to use the OOP principles and apply them to a real-world problem.
The real-world problem example is based on a Nike warehouse store where other store managers are able to use this program to manage stock eg. stock quantity, search the product by code, and calculate the total stock value.


This program plays an important role in managing the warehouse and performing stock-taking.

In this following project, we have a menu that allows us to pick an option and check many things for us such as the country of the product, product name, cost, quantity, and value of the product.



Select one of the following Options below:
        
        rsd - read shoe data
        cs - capture shoe
        va - view all
        rs - re-stock
        ss - search shoe
        vpi - value per item
        hq - highest quantity
        e - Exit

Instructions:

- rsd - this option will open the file inventory.txt and read the data from this file. The inventory.txt file must be in the format of shoe data on separate lines. Shoe data must be comma separated. 

Example output:

        Country,Code,Product,Cost,Quantity
        South Africa,SKU44386,Air Max 90,2300,20

- cs - this option will allow a user to add data about a shoe
- va - this option will display all the stock of the shoes

Example output:

        Country: Australia
        Code: SKU71827
        Product: Zoom Hyperfuse
        Cost: 1400
        Quantity: 15

        Country: France
        Code: SKU20394
        Product: Eric Koston 1
        Cost: 2322
        Quantity: 17




- rs - this option will show the lowest stock quantity of shoes that need to be re-stocked. It will ask the user if they want to add this quantity of shoes and then update it.
- ss - this option allows you to search for the shoe by entering a shoe code
- vpi - this option will calculate the total value for each item which is cost times quantity for each shoe

Example output:

        Enter a shoe codeSKU20394
        Country: France
        Code: SKU20394
        Product: Eric Koston 1
        Cost: 2322
        Quantity: 17


- hq - this option allows you to determine the product with the highest quantity and display that is for sale
- e - this option allows to exit the menu


