def read_numbers():

    with open('numbers100.txt') as f:
        words = [word.strip() for word in f]

    #print(words)

    for w in words:
        if len(w) != 50:
            print("wrong reading")

    #print("all correct")
    return words

def sum_numbers(num):

    digit_sum = 0
    carry = 0
    total_sum = []
    direct_sum = 0

    # direct addition as python can extend to large integers to verify

    #for w in num:
    #    direct_sum += int(w)

    #print("Ans: ", direct_sum)
    #return direct_sum

    # Addition digit by digit from unit's place
    for j in range(49, -1, -1):

        digit_sum = 0
        digit = 0

        for w in num:
            digit_sum += int(w[j])

        digit_sum += carry

        if digit_sum > 9:
            digit = digit_sum - int(digit_sum / 10) * 10
            carry = int(digit_sum / 10)
            total_sum.append(digit)

        else:
            carry = 0
            total_sum.append(digit_sum)

    while carry > 0:
        digit = carry - int(carry / 10) * 10
        carry = int(carry / 10)
        total_sum.append(digit)

    str1 = ''.join(str(e) for e in total_sum)

    #reversed answer str[begin:end:step]
    print("Result: ", str1[::-1])

numbers = read_numbers()

sum_numbers(numbers)
