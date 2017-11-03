from collections import namedtuple

def main():
    n = int(input())
    fields =input().split()
    total = 0
    
    for i in range(n):
        students = namedtuple('student', fields)
        field1, field2, field3, field4 = input().split()
        student = students(field1, field2, field3, field4)
        total += int(student.MARKS)
    print("{0:.2f}".format(total/n))    
        

if __name__ == "__main__":
    main()
