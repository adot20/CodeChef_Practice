# Pooja would like to withdraw X US Dollar from an ATM. The cash machine will only accept the transaction if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges). For each successful withdrawal the bank charges 0.50 US Dollar.

# Calculate Pooja's account balance after an attempted transaction.

# Input Format
# Each input contains 2 numbers X and Y.
# X is the amount of cash which Pooja wishes to withdraw. Y is Pooja's initial account balance.

# Output Format
# Output the account balance after the attempted transaction, given as a number with two digits of precision. If there is not enough money in the account to complete the transaction, output the current bank balance.

# X, Y = withdarwal_amount, initial_balance
X, Y = map(float, input().split())
# charge = 0.50 USD per transaction
charge = 0.5
if Y < (X + 0.5) or X % 5 != 0:
    print(Y)
else:
    if X % 5 == 0:
        final_balance = Y - (X + 0.5)
    balance_remain = f"{final_balance:.2f}"
    
    print(balance_remain)