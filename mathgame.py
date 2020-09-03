import time
import random
max_addition = 50
max_multiply = 9
n = 10
print ("Welcome to Math game")
print (" Here you can check your math skills\n by answering "+str(n)+" math questions")
score = 0
t = time.perf_counter()
for i in range(n):
    a = 0
    b = 0
    c = 0
    operation = random.choice(["+","-","*","/"])
    if operation == "+":
        a = random.randint(1, max_addition)
        b = random.randint(1, max_addition)
        c = a + b
    if operation == "-":
        c = random.randint(1, max_addition)
        b = random.randint(1, max_addition)
        a = b + c
    if operation == "*":
        a = random.randint(1, max_multiply)
        b = random.randint(1, max_multiply)
        c = a * b
    if operation == "/":
        b = random.randint(2, max_multiply)
        c = random.randint(2, max_multiply)
        a = b * c
    question = str(a)+" "+operation+" "+str(b)+" = "
    raw_answer = input(question)
    while not raw_answer.isdigit():
        raw_answer = input("  try number for "+question)
    answer = int(raw_answer)
    if answer == c:
        score = score + 1
        print(" correct")
    else:
        print("  no, it's "+str(c))
t2 = time.perf_counter()
print("Your score = "+str(score)+" ("+str(round(100*score/n,1))+" %)")
print("  time = "+str(t2-t))
print("  TpQ  = "+str((t2-t)/n))
