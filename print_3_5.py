
def print_number(n):
    result = []
    for i in range(1, n+1):
        if i%15 == 0:
            result.append("ThreeFive")
        elif i%5 == 0:
            result.append("Five")
        elif i%3 == 0:
            result.append("Three")
        else:
            result.append(str(i))

    return " ".join(result)

# Uncomment this line to directly print the numbers.
# print print_number(100)
