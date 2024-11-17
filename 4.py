def ab(a,b):
    text_a = 'A'
    text_b = 'B'
    mix = []
    count_a = 0
    count_b = 0

    while a > 0 or b >0:
        if count_a == 2 and b >0:
            mix.append(text_b)
            b -= 1
            count_b = 1
            count_a = 0
        elif count_b == 2 and a >0:
            mix.append(text_a)
            a -= 1
            count_a = 1
            count_b = 0
        elif a > b:
            mix.append(text_a)
            a -= 1
            count_a +=1
            count_b = 0
        else:
            mix.append(text_b)
            b -= 1
            count_b += 1
            count_a = 0
    print("".join(mix))


ab(7,5)
