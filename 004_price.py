"""

price = 100
discount = 5
def discounted(price, discount):
    price_with_discount = price - price * discount / 100
    print(price_with_discount)

"""

"""
def get_summ(one, two, delimiter = '&'):

    #print(one, two)
    return(f'{one}{delimiter}{two}')

one = input ('Первый параметр')
two = input ('Второй параметр')
a = get_summ(one, two, delimiter = '&')
print(a)



"""
#ДОДЕЛАТЬ
def format_price(price):
    price = int (price)
    return(f''ЦЕНА: ')

price = input ('ЦЕНА: ЧИСЛО руб.')

a = format_price(price)

print(a)
