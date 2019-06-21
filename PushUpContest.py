def push_up_total(pushups, days, day_num=1):
     if days < day_num:
        return
     else:
       print("\n\nday = "+ str(day_num))
       print("push ups " + str(pushups))
       push_up_total(pushups*2,days, day_num+1)


starting_num = int(input("how many push ups will you start with? "))
num_of_days = int(input("how many days? "))
push_up_total(starting_num,num_of_days)