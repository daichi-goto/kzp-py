def prob_check(prob):
    x = 0
    int_prob = int(prob)
    
    while True:
        if prob != int_prob:
            prob *= 10
            int_prob = int(prob)
            x += 1
        else:
            break
    
    return int_prob , x
