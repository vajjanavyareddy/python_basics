def result(marks):
    if marks>= 40 and marks<=50:
        return "Grade C"
    elif marks >50 and marks<=70:
        return "Grade B"
    elif marks>70 and marks <=80:
        return "Grade A"
    elif marks>80 and marks<=100:
        return "Distension"
    else:
        return "Fail"
m1 = int(input("ENter sub1 marks: "))
m2 = int(input("ENter sub2 marks: "))
m3 = int(input("ENter sub3 marks: "))
avg = (m1+m2+m3)//3
print("Average marks ",avg)
print("Student got ",result(avg))
