# student_scores = {
#     'Harry': 88, 
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}


# for keys in student_scores:
#     if 91 <= student_scores[keys] <= 100:
#         student_scores[keys] = "Outstanding"
#     elif 81 <= student_scores[keys] <= 90:
#         student_scores[keys] = "Exceeds Expectations"
#     elif 71 <= student_scores[keys] <= 80:
#         student_scores[keys] = "Acceptable"
#     elif student_scores[keys] <= 70:
#         student_scores[keys] = "Fail"
#     else:
#         student_scores[keys] = "Not a number"
        
# student_grades = student_scores
# print(student_grades)
print("Welcome to python silent Auction House!!\nBidders input your name and your bid....\nAs usual the highest bidder wins...let the bidding begin...")
def clear_terminal():
    print("\n" * 50)
details = {}
bidding = True

name = input("What's your name? ").capitalize()
bid = int(input("What's your bid? "))
details.update({name: bid})


def bid_process(boolean):
    while boolean :
        auctioner_choice = input("Anyone else bidding (yes/no) ? ").lower()
        if auctioner_choice == 'yes':
            clear_terminal()
            name = input("What's your name? ").capitalize()
            bid = int(input("What's your bid? "))
            details.update({name: bid})
        elif auctioner_choice == 'no':
            boolean = False

bid_process(bidding)

highest_bid, highest_bidder = details[max(details, key= details.get)], max(details, key= details.get)
print(f"With ${highest_bid}, {highest_bidder} wins this bid\n")