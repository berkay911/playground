#student_names = [ "alice", "bob", "charlie"]
#midterm1_grades = [90, 92, 78]
#midterm2_grades = [92, 79, 95]
#final_grades = [95, 85, 80]

grades_master_list = [
    ["alice", ["mt",[90,92]],95,"A"],
    ["bob",   ["mt",[92,79]],85,"B"],
    ["charlie",["mt",[78,95]],80,"C"]   
]

def convert_master_list_to_dictionary(grades_master_list):
    grades_dict = {}
    for student in grades_master_list:
        grades_dict[student[0]] = {
            "midterms": student[1][1],
            "final": student[2],
            "letter_grade": student[3]
        }
    return grades_dict

def get_second_midterm_grade(student_name, grades_master_list):
    for student in grades_master_list:
        if student[0] == student_name:
            second_midterm =  student[1][1][1]
    return second_midterm

second_midterm_bob = get_second_midterm_grade("bob", grades_master_list)
#print(second_midterm_bob)

grade_dict = convert_master_list_to_dictionary(grades_master_list)
#print(grade_dict)

#print(grade_dict["alice"])
print(grade_dict["alice"]["midterms"])



