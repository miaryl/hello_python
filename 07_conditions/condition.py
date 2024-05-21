# use input() to get infomation from the user
userReply = input("do you need to ship a package? (enter YES or NO) ")

#print response depends on the answer from input
if userReply == "yes" :
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")

# make more complicated!
userReply = input("Which item do you want to buy? (Enter stamps, envelope, or copy)")

if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copeis." .format(copies))
else:
    print("Thank you!")