# [ 기본코드 ]
# marks = [90, 25, 67, 45, 80]
#
# number = 0
# for mark in marks:
#     number += 1
#     if mark >= 60:
#         print("%d 번 학생: 합격" % number)
#     else:
#         print("%d 번 학생: 불합격" % number)

# [ 합격 점검 코드1 ]
# marks = [90, 25, 67, 45, 80]
#
# number = 0
# for mark in marks:
#     number += 1
#     if mark < 60: continue
#     print("%d 번 학생: 합격" % number)

# [ 합격 점검 코드2 ]
marks = [90, 25, 67, 45, 80]

for number in range(len(marks)):
    if marks[number] < 60: continue
    print("%d 번 학생: 합격" % (number+1))