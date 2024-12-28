print("""\

███╗   ███╗ █████╗ ████████╗██╗  ██╗███████╗     ██████╗ ██╗   ██╗██╗███████╗
████╗ ████║██╔══██╗╚══██╔══╝██║  ██║██╔════╝    ██╔═══██╗██║   ██║██║╚══███╔╝
██╔████╔██║███████║   ██║   ███████║███████╗    ██║   ██║██║   ██║██║  ███╔╝ 
██║╚██╔╝██║██╔══██║   ██║   ██╔══██║╚════██║    ██║▄▄ ██║██║   ██║██║ ███╔╝  
██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║███████║    ╚██████╔╝╚██████╔╝██║███████╗
╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝
                                                                             
""")

import random

print("Welcome to the Maths quiz!")
print("You can select a difficulty mode from difficult to easy. Your job is to try to answer the questions correctly. Good luck!")

no_ques = int(input("Enter the number of questions you want to play: "))
if not isinstance(no_ques, int):
    print("Enter a valid number!")

    
max_num = int(input("Enter the highest number you want to practice with: "))
if not isinstance(max_num, int):
    print("Enter a valid number!")



difficulty_level = input("Press D for difficult, M for medium, and E for easy: ").lower()

score = 0

def difficult_question():
    num1, num2, num3, num4, num5, num6, num7, num8, num9 = (
        random.randint(1, max_num + 1),
        random.randint(1, max_num + 1),
        random.randint(1, max_num + 1),
        random.randint(1, max_num + 1),
        random.randint(1, max_num + 1),
        random.randint(1, max_num + 1),
        random.randint(1, max_num + 1),
        random.randint(1, max_num + 1),
        random.randint(1, max_num + 1),
    )

    def a_():
        global score
        a_calc = (num1 * num2) / 2
        u_a_ans = float(input(f"({num1} * {num2}) / 2: "))
        if a_calc == u_a_ans:
            print("Congrats you entered the right answer! ")
            score += 1
        else:
            print(f"Wrong answer! The correct answer is: ({num1} * {num2}) / 2 = {a_calc}")

    def b_():
        global score
        b_calc = (num4 * num6) * num3
        u_b_ans = float(input(f"({num4} * {num6}) * {num3}: "))
        if b_calc == u_b_ans:
            print("Congrats you entered the right answer! ")
            score += 1
        else:
            print(f"Wrong answer! The correct answer is: ({num4} * {num6}) * {num3} = {b_calc}")

    def c_():
        global score
        c_calc = (num8 * num7) / 2
        u_c_ans = float(input(f"({num8} * {num7}) / 2: "))
        if c_calc == u_c_ans:
            print("Congrats you entered the right answer! ")
            score += 1
        else:
            print(f"Wrong answer! The correct answer is: ({num8} * {num7}) / 2 = {c_calc}")

    def f_():
        global score
        f_calc = (num1 * num1) / 2
        u_f_ans = float(input(f"({num1} * {num1}) / 2: "))
        if f_calc == u_f_ans:
            print("Congrats you entered the right answer! ")
            score += 1
        else:
            print(f"Wrong answer! The correct answer is: ({num1} * {num1}) / 2 = {f_calc}")

    question_types = [a_, b_, c_, f_]
    random.shuffle(question_types)

    for question in question_types[:no_ques]:
        question()

def medium_question():
    num1, num2, num3, num4, num5, num6, num7, num8, num9 = (
        random.randint(1, max_num + 1),
        random.randint(1, max_num + 1),
        random.randint(1, max_num + 1),
        random.randint(1, max_num + 1),
        random.randint(1, max_num + 1),
        random.randint(1, max_num + 1),
        random.randint(1, max_num + 1),
        random.randint(1, max_num + 1),
        random.randint(1, max_num + 1),
    )

    def x_():
        global score
        x_calc = (num6 + num4) * 2
        u_x_ans = float(input(f"({num6} + {num4}) * 2: "))
        if x_calc == u_x_ans:
            print("Congrats you entered the right answer! ")
            score += 1
        else:
            print(f"Wrong answer! The correct answer is: ({num6} + {num4}) * 2 = {x_calc}")

    def o_():
        global score
        o_calc = (num5 - num4) * 2
        u_o_ans = float(input(f"({num5} - {num4}) * 2: "))
        if o_calc == u_o_ans:
            print("Congrats you entered the right answer! ")
            score += 1
        else:
            print(f"Wrong answer! The correct answer is: ({num5} - {num4}) * 2 = {o_calc}")

    def g_():
        global score
        g_calc = (num3 + num4) - 2
        u_g_ans = float(input(f"({num3} + {num4}) - 2: "))
        if g_calc == u_g_ans:
            print("Congrats you entered the right answer! ")
            score += 1
        else:
            print(f"Wrong answer! The correct answer is: ({num3} + {num4}) - 2 = {g_calc}")

    def h_():
        global score
        h_calc = (num1 + num2) + (num5 - num9)
        u_h_ans = float(input(f"({num1} + {num2}) + ({num5} - {num9}): "))
        if h_calc == u_h_ans:
            print("Congrats you entered the right answer! ")
            score += 1
        else:
            print(f"Wrong answer! The correct answer is: ({num1} + {num2}) + ({num5} - {num9}) = {h_calc}")

    question_types = [x_, o_, g_, h_]
    random.shuffle(question_types)

    for question in question_types[:no_ques]:
        question()

def easy_question():
    num1, num2, num3, num4, num5, num6, num7, num8, num9 = (
        random.randint(1, max_num + 1),
        random.randint(1, max_num + 1),
        random.randint(1, max_num + 1),
        random.randint(1, max_num + 1),
        random.randint(1, max_num + 1),
        random.randint(1, max_num + 1),
        random.randint(1, max_num + 1),
        random.randint(1, max_num + 1),
        random.randint(1, max_num + 1),
    )

    def i_():
        global score
        i_calc = num5 + num8
        u_i_ans = float(input(f"{num5} + {num8}: "))
        if i_calc == u_i_ans:
            print("Congrats you entered the right answer! ")
            score += 1
        else:
            print(f"Wrong answer! The correct answer is: {num5} + {num8} = {i_calc}")

    def j_():
        global score
        j_calc = num6 + num7 + num8
        u_j_ans = float(input(f"{num6} + {num7} + {num8}: "))
        if j_calc == u_j_ans:
            print("Congrats you entered the right answer! ")
            score += 1
        else:
            print(f"Wrong answer! The correct answer is: {num6} + {num7} + {num8} = {j_calc}")

    def k_():
        global score
        k_calc = num9 - num3
        u_k_ans = float(input(f"{num9} - {num3}: "))
        if k_calc == u_k_ans:
            print("Congrats you entered the right answer! ")
            score += 1
        else:
            print(f"Wrong answer! The correct answer is: {num9} - {num3} = {k_calc}")

    def l_():
        global score
        l_calc = num4 * num1
        u_l_ans = float(input(f"{num4} * {num1}: "))
        if l_calc == u_l_ans:
            print("Congrats you entered the right answer! ")
            score += 1
        else:
            print(f"Wrong answer! The correct answer is: {num4} * {num1} = {l_calc}")

    question_types = [i_, j_, k_, l_]
    random.shuffle(question_types)

    for question in question_types[:no_ques]:
        question()

question_types = []

if difficulty_level == 'd':
    question_types = [difficult_question]
elif difficulty_level == 'm':
    question_types = [medium_question]
elif difficulty_level == 'e':
    question_types = [easy_question]
else:
    print("Invalid difficulty level. Please enter D for difficult, M for medium, or E for easy.")

    
if question_types:
    random.shuffle(question_types)
    
    for question_function in question_types[:no_ques]:
        question_function()

percentage = float(score) / no_ques * 100

if score == no_ques:
    print(f'Congrats! You scored {score} out of {no_ques} ({percentage}%)!')
else:
    print(f'Good try! You scored {score} out of {no_ques} ({percentage}%)!')

input("Press Enter to exit...")