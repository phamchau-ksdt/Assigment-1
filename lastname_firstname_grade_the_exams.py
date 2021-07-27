# Assignment 1: write a programming to opening the file, analyzing and writing the result

# import packages
import os
import statistics


# Task1: write a programming that lets the user type in the name of a file to open it
print("\n*** OPENING FILE ***")

# check the name of file to open it
class_name = str(input("Enter the name of class to grade: ") + ".txt")

while os.path.isfile(class_name) == False:
    try:
        op = open(class_name, "r")
        print(f"Successfully opened {class_name}")
    except:
        print("File name is not found. Please try another name")
        class_name = str(input("Enter the name of class to grade: ") + ".txt")

# other way to check and open the file
"""
path = os.getcwd()
direc = os.listdir(path)

while class_name not in direc:
    print("File name is not found. please try another name")
    class_name = str(input("Enter the name of class to grade: ") + ".txt")
else:
    print(f"Successfully opened {class_name}")
"""

# Task2: analyze the data contained within the file you just opened to ensure that it is in the correct format
print("\n*** ANALYZING ***")

# Analyzing the data
with open(class_name, "r") as op:
    line = op.readlines()
    op.seek(0) # move the mouse pointer to the first line to accomplish the lines_count command
    line_count = sum(1 for line in op)
    count_valid = 0
    count_invalid = 0
    student_id = []
    student_score = []
    result = {}
    for i in range(line_count):
        line_single = line[i].split(",")
        line_single = [item.replace("\n", "") for item in line_single] # xoá ký tự xuống dòng "\n" trong list line_single
        # the second way: line_single = line[i].strip() # delete "\n" at the end on the right side
        # line_single = line_single.split(",")
        # the third way: line_single = line[i].replace("\n", "")
        # line_single = line_single.split(",")
        if len(line_single) != 26:
            count_invalid += 1
            print("Invalid data of line: does not contain exactly 26 values \n" + line[i])
        elif "N" not in line_single[0] or len(line_single[0]) != 9 or line_single[0][1:9].isnumeric() == False:
            count_invalid += 1
            print("Invalid data of line: N# is invalid \n" + line[i])
        else:
            count_valid += 1
            answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
            answer_key = answer_key.split(",")
            score = 0
            for j in range(len(answer_key)):
                if line_single[j + 1] == answer_key[j]:
                    score += 4
                elif line_single[j + 1] == "":
                    score += 0
                else:
                    score -= 1
            student_score.append(score)
            result[line_single[0]] = score

if count_invalid == 0:
    print("No errors found")

# report the result
print("\n*** REPORT ***")
print(f"The total of lines in {class_name} is: " + str(line_count))
print("Total valid lines of data: " + str(count_valid))
print("Total invalid lines of data: " + str(count_invalid))


# Task3: write a programme to grade the exams
print("\n*** GRADING ***")

# The average score
score_average = statistics.mean(student_score)
print("The average score is: ", round(score_average, 2) )

# The highest score
score_highest = max(student_score)
print("The highest score is: ", score_highest)

# The lowest score
score_lowest = min(student_score)
print("The lowest score is: ", score_lowest)

# The range of scores
score_range = score_highest - score_lowest
print("The range of score is: ", score_range)

# The median value
score_median = statistics.median(student_score)
print("The median value is: ", round(score_median, 2))


# Task 4: Store the result
class_name_movetxt = class_name.replace(".txt", "")
class_name_op = class_name_movetxt + "_grades.txt"

with open(class_name_op, "w") as opw:
    for key, value in result.items():
        opw.write(str(key + ", " + str(value) + "\n"))
