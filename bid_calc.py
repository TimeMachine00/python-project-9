from replit import clear


print("welcome to secret auction")
data ={}
z =True
while z:

    name = input("what is your name\n")
    bid =int(input("what is your bid value:\n$"))

    data[name]=bid
    que= input("are there any other bidders, yes or no?\n").lower()


    if que=='yes':
        clear()

    else:
        z=False

    # print(data)
l = 0
high_name=''
for i, j in data.items():
    if j>l:
        l=j
        high_name=i
print(f"the winner is {high_name} with a bid of ${l}")