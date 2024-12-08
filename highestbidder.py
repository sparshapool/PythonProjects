from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the secret auction program.")
bidder = {}
choice = False


def highest_bidder(bidder):
    max = 0
    winner = " "
    for value in bidder:
        if bidder[value] > max:
            max = bidder[value]
            winner = value
    print(f"The winner is {winner} with a bid of ${max}")


while (not choice):
    name = input("Enter the bidders name: ")
    bid = int(input("Enter the bid amount $"))
    bidder[name] = bid
    choice = input("Are there any other bidders?Type yes or no")
    if (choice == "no"):
        highest_bidder(bidder)
        choice = True
    elif (choice == "yes"):
        choice = False
        clear()
