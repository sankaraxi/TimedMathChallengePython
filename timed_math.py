import random
import time

operators = ["+", "-", "*"]
min_operand = 3
max_operand = 12
total_problems = 10

#generating a random problems
def generate_problem():
    left = random.randint(min_operand,max_operand)
    right = random.randint(min_operand,max_operand)
    operator = random.choice(operators)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr , answer

input("Press Enter to Start!")
print("----------------------")
start_time = time.time() #initiating start time

#obtaining answers for the total number of problems
for i in range(total_problems):
    expr, answer = generate_problem()
    
    print (expr, answer)
    while True:
        guess = input("Problem #" + str(i+1)+" : "+ expr + " = ")
        if guess == str(answer):
            break
end_time = time.time() #obtaing end time
total_time=round(end_time-start_time,2)
print("----------------------")
print("Nice Work! You have completed in ",total_time,"seconds." )


