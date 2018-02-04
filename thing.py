rand=str(2**16+1)
digits=[0]*10
for chr in randChar:
 digits[int(chr)]+=1
print(digits)
#[1948, 2057, 1972, 1978, 1977, 1984, 1982, 1944, 1984, 1903]