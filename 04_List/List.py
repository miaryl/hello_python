#make list of ....... fruits!
fruits = ["apple", "banana", "kiwi", "mango"]

#1st, print fruits and print data type of fruits
print(fruits)
print(type(fruits))

#print each fruit of the list fruits
print(fruits[0])
print(fruits[1])
print(fruits[3])

#change kiwi to peach and print it 
fruits[2] = "peach"
print(fruits[2])

#ex2 tuple data type is like a list but you can't change values
favFruits = ("mango", "peach", "lychee")
print(favFruits)
print(favFruits[2])

#ex3 dictionary data type, store favorite bands each person and print it
favBands = {"Mio": "Enter Shikari",
            "adri":"You Me At Six",
             "Yusuke": "Five Finger Death Punch" }
print(favBands)

print(favBands["Mio"])
