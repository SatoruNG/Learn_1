#grades = '[[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]'
#students = "{'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}"
GPA = {}

grades = input().strip('[]').split('], [')
students = sorted(input().strip("{''}").split("', '"))
GPA[students[0]] = sum(list(map(int, grades[0].split(", ")))) / len(grades[0].split(", "))
GPA[students[1]] = sum(list(map(int, grades[1].split(", ")))) / len(grades[1].split(", "))
GPA[students[2]] = sum(list(map(int, grades[2].split(", ")))) / len(grades[2].split(", "))
GPA[students[3]] = sum(list(map(int, grades[3].split(", ")))) / len(grades[3].split(", "))
GPA[students[4]] = sum(list(map(int, grades[4].split(", ")))) / len(grades[4].split(", "))
print(GPA)