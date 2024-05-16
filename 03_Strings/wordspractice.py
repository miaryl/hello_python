#store words in myString value and print
myString ="This is a string."
print(myString)

#print type of myString
print(type(myString))

#Ex2 store three words each in a value and connect them
firstString = "Enter "
secondString ="Shikari "
thirdStrings = "is the best"
forthString = firstString + secondString + thirdStrings
print(forthString)

#Ex3 I did it before but let's do it again, input strings
band = input("What is your fav band?: ")
print(band, "is the BEST ! !")

#Ex4 Formatting output strings
#make name and genre value and use input() to be able to answer
name = input("What is your name?: ")
genre = input("What is your fav music genre?: ")

#unite all inputs to use format()
print("you like {}, especially {}? {}, you have nice taste of music!".format(genre,band,name))


