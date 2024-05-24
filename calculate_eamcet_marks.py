# ask user for his name and store it in a variable "name"
#  ask user for his marks in eamcet and store it in marks
#  now ask user for his marks in ipe for 600
#  now calculate total marks he will get 75% of eamcet+25% of ipe



# ❯ python3 idk.py
# what is your name?
# paddu

# what is your makrs in eamcet47
# what are your ipe marks523
# 43.82291666666667


#  strin -> "" / words
#  int -> numbers


name= input("what is ur name\n")
marks=input("how many marks in eamcet?\n")
ipe_marks=input("what is your ipe marks\n")


avg_inter_marks=int(ipe_marks)/600*25
avg_eamcet_marks=int(marks)/160*75

total_marks = avg_inter_marks+avg_eamcet_marks

print("total marks is",total_marks)





# int() -> converts string in to integer






































