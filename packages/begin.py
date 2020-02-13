def prime(num):
    modulo_count = {}
    if num < 1 or type(num) != int:
        return False
    else:
        for number in range(1, num+1, 1):
            modulo_count.setdefault(num%number, 0)
            modulo_count[num%number] +=1
        if modulo_count[0] > 2:
            return False
        else:
            return True