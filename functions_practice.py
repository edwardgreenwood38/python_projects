def hello():
    print("Hello")

def pack(a, b, c):
    return [a, b, c]

def eat_lunch(foodItems):
    # check if no food passed in
    if len(foodItems) == 0:
        print("My lunchbox is empty!")
    else:
        # print out each item passed in
        for i in range(len(foodItems)):
            if i == 0:
                print(f"First I eat {foodItems[0]}")
            else:
                print(f"Next I eat {foodItems[i]}")

hello()
print(pack(1,3,6))
eat_lunch(["apple", "banana", "carrot"])
