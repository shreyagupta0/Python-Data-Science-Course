num = 12345
rev = 0

while num > 0:
    rem = num % 10
    num = num // 10
    rev = rev * 10 + rem
    print ( rem , num)

    print (" your total sum is >>> " , rev)