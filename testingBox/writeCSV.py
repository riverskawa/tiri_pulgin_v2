
import csv


def writeTxt(self):
    # version 2
    with open('students.csv', 'w', newline='') as student_file:
        writer = csv.writer(student_file)
        writer.writerow(["frame", "displacement"])
        for i in range(0,50):
            for j in range(0,10):
                writer.writerow([i, j])

