def nintenyier(price):
    len(str(price))
    str_price = str(price)

    if int(str_price[-2:]) >= 49:
        str_new_price = str_price[:-2] + "99"
    else:
        str_new_price = str_price[0:len(str_price)-3] + str(int(str_price[-3]) - 1) + "99"
    return (str_new_price)


def nearest_ending_in_99(N):
    # Find the closest multiple of 100 that is less than or equal to N
    closest_multiple_of_100 = (N // 100) * 100
    #print(closest_multiple_of_100)
    # Calculate the two possible numbers that end in 99
    num1 = closest_multiple_of_100 - 1
    num2 = closest_multiple_of_100 + 99
    #print(num1)
    #print(num2)
    # Determine which one is closer to N
    if closest_multiple_of_100 == 0:
        return num2
    elif abs(N - num1) < abs(N - num2):
        return num1
    elif abs(N - num2) < abs(N - num1):
        return num2
    else:
        # If both are equally close, return the bigger one
        return max(num1, num2)
for i in [10, 249, 10000]:
    print(nearest_ending_in_99(i))
#print(nintenyier(1234))