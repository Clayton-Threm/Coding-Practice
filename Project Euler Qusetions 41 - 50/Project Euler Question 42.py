#Project Euler Question 42
#Coded triangle numbers


names_file = open(r"C:\Users\Clayton\Documents\Python Other Files\p042_words.txt")
content = names_file.read()
content = content.replace("\"", "")
content = content.split(",")
content.sort()

def triangle_number(x):
    if x == 1:
        return True
    else:
        n = 1
        while True:
            n += 1
            trin = int((n + 1) * n / 2)
            if trin > x:
                return False
            elif trin == x:
                return True

triangle_words = set()
for word in content:
    word_score = sum([(ord(letter.lower()) - 96) for letter in word])
    if triangle_number(word_score) is True:
        triangle_words.add(word)

print (len(triangle_words))

names_file.close()