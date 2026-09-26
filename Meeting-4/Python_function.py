# number = [10, 16, 30, 21]
#
# print(max(number))
# print(min(number))
# print("hello".upper())
# print("WELCOME".lower())

# def order_pizza():
#     quantity = 7
#     price = 10
#     total_order = quantity * price
#     print(f"total order $: {total_order}")
#
# order_pizza()

"""
def order_pizza():
    quantity = int(input("How many pizza? :"))
    price = 10
    total_order = quantity * price
    print(f"total order $: {total_order}")

order_pizza()
"""

"""
total = 50
def sum():
    first = 10
    second = 20
    total = first + second
    print(total)
print(total)
sum()
"""
numbers = [2, 3, 4]

def multiply_list(numbers):
    result = 1
    for num in numbers:
        print("-")
        print(num)
        print(result)
        result *= num
        print(result)
    return result

print(multiply_list(numbers))