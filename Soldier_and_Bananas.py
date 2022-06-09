Initial_banana_price = int(input("Enter the first banana's price: "))
Total_money_have = int(input("Enter the total money he has: "))
Tot_no_of_banana_needed = int(input("Enter the total no. of banana that he wanna buy: "))

Amount_need_to_borrow_from_friends = 0
total_money_needed = 0

for i in range(Tot_no_of_banana_needed):
    total_money_needed = total_money_needed + (Initial_banana_price + (i*Initial_banana_price))

print("Total money needed for all these banana: ",total_money_needed)
print("Total money need to borrow from friends: ",abs(total_money_needed-Total_money_have))

