#Project Euler Question 48
#Self powers

result = 0
for x in range(1,(1000 + 1)):
    result += (x**x)

print (int(str(result)[-10::]))