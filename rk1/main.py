class StudentGroup:
    def __init__(self, id, name, student_count, department_id):
        self.id = id
        self.name = name
        self.student_count = student_count
        self.department_id = department_id


class Department:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class GroupDepartment:
    def __init__(self, group_id, department_id):
        self.group_id = group_id
        self.department_id = department_id


departments = [
    Department(1, "Автоматизация"),
    Department(2, "Информатика"),
    Department(3, "Авиастроение"),
]

groups = [
    StudentGroup(1, "АУ-11", 25, 1),
    StudentGroup(2, "АУ-12", 30, 1),
    StudentGroup(3, "ИУ-11", 28, 2),
    StudentGroup(4, "ИУ-12", 22, 2),
    StudentGroup(5, "АС-11", 26, 3),
]

group_departments = [
    GroupDepartment(1, 1),
    GroupDepartment(2, 1),
    GroupDepartment(3, 2),
    GroupDepartment(4, 2),
    GroupDepartment(5, 3),
    GroupDepartment(1, 2),
    GroupDepartment(3, 3),
]


def main():
    one_to_many = [
        (group.name, group.student_count, department.name)
        for department in departments
        for group in groups
        if group.department_id == department.id
    ]

    many_to_many = [
        (group.name, department.name)
        for department in departments
        for link in group_departments
        for group in groups
        if link.department_id == department.id
        and link.group_id == group.id
    ]

    print("Задание Г1")
    print("Кафедры на букву «А» и их группы:")

    result_1 = {
        department.name: [
            group.name
            for group in groups
            if group.department_id == department.id
        ]
        for department in departments
        if department.name.startswith("А")
    }

    for department_name, group_names in result_1.items():
        print(f"{department_name}: {', '.join(group_names)}")

    print("\nЗадание Г2")
    print("Кафедры по возрастанию максимальной численности группы:")

    result_2 = []

    for department in departments:
        counts = [
            student_count
            for _, student_count, department_name in one_to_many
            if department_name == department.name
        ]
        if counts:
            result_2.append((department.name, max(counts)))

    result_2 = sorted(result_2, key=lambda item: item[1])

    for department_name, max_count in result_2:
        print(f"{department_name}: {max_count}")

    print("\nЗадание Г3")
    print("Связи многие-ко-многим, отсортированные по кафедрам:")

    result_3 = sorted(many_to_many, key=lambda item: item[1])

    for group_name, department_name in result_3:
        print(f"{department_name}: {group_name}")


if __name__ == "__main__":
    main()
