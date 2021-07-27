# Assignment 1: write a programming to opening the file, analyzing and writing the result

# import packages
import pandas as pd
import numpy as np
import os
import statistics


# Task1: write a programming that lets the user type in the name of a file to open it
print("\n*** OPENING FILE ***")

# check the name of file to open it
list_name = np.array(['class1.txt', 'class2.txt', 'class3.txt', 'class4.txt', 'class5.txt', 'class6.txt', 'class7.txt', 'class8.txt'])
# class_name = str(input("Enter the class name: ") + ".txt")            # restore
#
# while class_name not in list_name:
#     print("Invalid name! Please try another name")
#     class_name = str(input("Enter the class name: ")) + ".txt"
# print(f"successful opned {class_name}")

class_name = "class2.txt"               # delete


# Task2: analyze the data contained within the file you just opened to ensure that it is in the correct format
print("\n*** ANALYZING ***")

# Analyzing the data
df_class = pd.read_table(class_name, header=None) # df_class = pd.read_csv(class_name, header=None, delimiter = "\t")
def check_row(x):
    line_single = x[0].split(",")
    is_valid = 1
    if len(line_single) != 26:
        is_valid = -1
        print("Invalid data of line: does not contain exactly 26 values \n", x[0])
    elif "N" not in line_single[0] or len(line_single[0]) != 9 or line_single[0][1:9].isnumeric() == False:
        is_valid = -2
        print("Invalid data of line: N# is invalid \n", x[0])
    return pd.Series({"original":x[0], "student_id": line_single[0], "is_valid": is_valid})

# report the result
df_analyze = df_class.apply(lambda x: check_row(x), axis=1)
line_total = df_class.shape[0]
line_valid = sum(df_analyze["is_valid"] == 1)
line_invalid = sum(df_analyze["is_valid"] != 1)

if line_invalid == 0:
    print("No errors found")

print("\n*** REPORT ***")
print(f"The total of lines in {class_name} is: " + str(line_total))
print("Total valid lines of data: " + str(line_valid))
print("Total invalid lines of data: " + str(line_invalid))


# Task3: write a programme to grade the exams
df_score = df_analyze[df_analyze["is_valid"] == 1]

def grade(x):
    line_single = x[0].split(",")
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    answer_key_split = answer_key.split(",")
    score = 0
    for i in range(len(answer_key_split)):
        if line_single[i+1] == answer_key_split[i]:
            score += 4
        elif line_single[i+1] == "":
            score += 0
        else:
            score += -1
    return pd.Series({"Original":x[0], "Student_ID": line_single[0], "Score": score})

df_result = df_score.apply(lambda x: grade(x), axis=1)

# The average score
score_average = df_result["Score"].mean()
print("The average score is: ", round(score_average, 2) )

# The highest score
score_highest = df_result["Score"].max()
print("The highest score is: ", score_highest)

# The lowest score
score_lowest = df_result["Score"].min()
print("The lowest score is: ", score_lowest)

# The range of scores
score_range = score_highest - score_lowest
print("The range of score is: ", score_range)

# The median value
score_median = df_result["Score"].median()
print("The median value is: ", round(score_median, 2))


# Task 4: Store the result
class_name_movetxt = class_name.replace(".txt", "")
class_name_op = class_name_movetxt + "_grades.txt"

result_list = pd.DataFrame(df_result[["Student_ID", "Score"]])

with open(class_name_op, "w") as opw:
   opw.write(result_list.to_string(header=False, index=False))

open_class = open(class_name_op, "r")
print(open_class.readlines())
open_class.close()
