"""как по мне лучше всего обмениватся словорями так легче ,есть тип марок и их виды"""

my_marks =[{"Cats": ("terrible", "good", "good", "crazy", "beautiful")},
           {"Cars": ("koenigsegg", "porsh", "bugatti", "ferrari", "kia")},
           {"Elephants": ("sick", "big", "small", "hungry")}]
her_marks = [{"Yacht": ("big", "mini", "toy")}, {"Dog": ("puppy",)}, {"Helicopter": ("hunter", "wood", "military")}]

print("It is your marks:", my_marks)
print("It is her marks:", her_marks)

human_answer = input("Do you need her marks?  y/n\n")

if human_answer == "y":
    want_he = int(input("What do you want in her marks?\nPlease number "))
    if want_he <= 3 and want_he >= 1:
        give_she = int(input("What do you give her?\nPlease number "))
        if give_she <= 3 and give_she >= 1:
            her_marks.append(my_marks[give_she - 1])
            my_marks.append(her_marks[want_he-1])
            my_marks.pop(give_she-1)
            her_marks.pop(want_he-1)
            print(my_marks)
            print(her_marks)
        else:
            print("go to school")
    else:
        print("go home")
else:
    print("go having lunch")