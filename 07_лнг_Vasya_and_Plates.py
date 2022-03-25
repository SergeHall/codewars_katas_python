def count_clean(bowls, plates, dishes):
    wash = 0
    for i in dishes:
        if i == 1:
            if bowls > 0:
                bowls -= 1
            else:
                wash += 1

        if i == 2:
            if plates > 0:
                plates -= 1
                continue
            if plates <= 0 and bowls > 0:
                bowls -= 1
            else:
                wash += 1
    return wash