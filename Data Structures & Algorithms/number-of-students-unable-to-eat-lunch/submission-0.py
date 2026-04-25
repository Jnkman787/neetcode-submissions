class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        while students and sandwiches:
            count += 1
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count = 0
            else:
                if count == len(sandwiches):
                    break
                x = students.pop(0)
                students.append(x)

        return len(students)