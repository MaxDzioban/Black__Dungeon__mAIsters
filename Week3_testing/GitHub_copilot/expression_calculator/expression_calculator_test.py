def calculate_expression(string_na_input)->int:
    """
    Calculate string in mathisian way
    >>> calculate_expression("Скільки буде 8 відняти 3?")
    5
    >>> calculate_expression("Скільки буде 7 відняти 3?")
    4
    >>> calculate_expression('Скільки буде 10 розділити на 2?')
    5
    """
    falsh="Неправильний вираз!"
    if not isinstance(string_na_input, str):
        return falsh
    if "?" not in string_na_input:
        return falsh
    word_list= string_na_input.split(" ")
    if word_list[0] == "Скільки" and word_list[1] == "буде":
        word_list.remove('Скільки')
        word_list.remove('буде')
        if "на" in word_list:
            word_list.remove('на')
        new_list = []
        for item in word_list:
            if '?' in item:
                new_item = item.rstrip('?')  # Видаляємо запитання з кінця рядка
                new_list.append(new_item)
            else:
                new_list.append(item)
        if len(new_list)%2 == 0:
            return falsh
        if len(new_list)==1:
            return int(new_list[0])
        if len(new_list)==3:
            elem_1 = int(new_list[0])
            elem_2 = int(new_list[2])
            if new_list[1] == "відняти" or new_list[1] == "мінус":
                return elem_1-elem_2
            if new_list[1] == "додати" or new_list[1] == "плюс":
                return elem_1+elem_2
            if new_list[1] == "поділити" or new_list[1] == "розділити":
                if elem_2 == 0:
                    return falsh
                return(int(elem_1/elem_2))
            if new_list[1] == "помножити":
                return elem_1*elem_2

    else:
        return falsh
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
