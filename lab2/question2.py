'''
2. WAP which accepts marks of four subjects and display total marks, percentage and grade.
 Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail
'''
math = int(input(f'enter the marks: '))
sci = int(input(f'enter the marks: '))
eng = int(input(f'enter the marks: '))
com = int(input(f'enter the marks : '))
total_attempt_marks = math + sci + eng + com
total_marks = 400
percentage = (total_attempt_marks / total_marks) * 100
print(f'The percentage is {percentage}')
if percentage > 70:
    print(f'contrats!! you got distinction')
elif percentage > 60 <=69:
    print(f'you got first divison.')
elif percentage >= 40:
    print(f'you passed')
elif percentage < 40 :
    print(f'you fail')


