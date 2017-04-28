import pandas
import sys


def read_result(filename, full, foldername):
    if foldername[-1] == "/":
        foldername = foldername[:-1]
    f = open(filename, 'r+')
    grade_dict = {}
    late_dict = {}
    time_dict = {}
    curr_code = 0
    for line in f.readlines():
        # print(line[0])
        line = line[:-1]
        if len(line) < 2:
            continue
        # print(line[:4])
        if line[:len(foldername)] == foldername:
            elems = line[len(foldername)+1:].split("_")
            # print(elems)
            if elems[1] == "late":
                curr_code = elems[2]
                late_dict[curr_code] = 1
            else:
                curr_code = elems[1]
        if line[:3] == "Ran":
            # print("aaaaa")
            elems = line.split(" ")
            # print(elems)
            if elems[1] == "24":
                grade_dict[curr_code] = full
                time_dict[curr_code] = elems[4]

    for key in late_dict.keys():
        grade_dict[key] *= 0.9
        print(key, " : ", grade_dict[key])
    return grade_dict, late_dict, time_dict



def write_grades(filename, grade_dict):
    csv_read = pandas.read_csv(filename)
    for lab, row in csv_read.iterrows():
        # print(row["Student"])
        if row["Student"] == "Points Possible":
            csv_read.loc[lab, "grades"] = 10
            # print("______________")
        curr_id = row["ID"]
        # print(str(curr_id)[:-2])
        curr_id = str(curr_id)[:-2]
        if curr_id not in grade_dict:
            csv_read.loc[lab, "grades"] = 0
            continue
        # print("yes")
        csv_read.loc[lab, "grades"] = (float(grade_dict[curr_id]))
    csv_read.to_csv('upload_grades.csv', index=False)
    # print(csv_read)


arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]

a, b, c = read_result("temp_result", int(float(arg3)), arg1)
# print(a)
# print(b)
# print(c)
print(b)
# write_grades("cs320_grade_base.csv", a)
write_grades(arg2, a)
