print("enter you marks of all your subjects")
sub1 =int(input("subject 1 "))
sub2 =int(input("subject 2 "))
sub3 =int(input("subject 3 "))
sub4 =int(input("subject 4 "))
sub5 =int(input("subject 5 "))
sub6 =int(input("subject 6 "))
totalvalue =sub1+sub2+sub3+sub4+sub5+sub6
average =totalvalue/6
if (average>80 and average<100):
    print("grade A")
elif (average>60 and average<80):
    print("grade b")
elif (average>40 and average<60):
    print("grade c")
elif (average>30 and average<40):
    print("grade d")
elif (average>0 and average<30):
    print("grade fail")
else:
    print("enter a corect value please")