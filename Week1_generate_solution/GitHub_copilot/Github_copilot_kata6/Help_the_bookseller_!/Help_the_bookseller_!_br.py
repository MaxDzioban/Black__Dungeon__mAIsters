def stock_list(list_of_art, list_of_cat):
    # Create a dictionary to store the quantity of books for each category
    category_quantity = {cat: 0 for cat in list_of_cat}

    # Iterate over each book in the stock list
    for book in list_of_art:
        # Split the book code and quantity
        code, quantity = book.split()

        # Get the category of the book
        category = code[0]

        # Check if the category is in the list of categories
        if category in list_of_cat:
            # Add the quantity of the book to the corresponding category
            category_quantity[category] += int(quantity)

    # Convert the category quantity dictionary to a list of strings
    result = [f'({cat} : {category_quantity[cat]})' for cat in list_of_cat]

    # Return the result as a string joined by spaces
    return ' '.join(result)