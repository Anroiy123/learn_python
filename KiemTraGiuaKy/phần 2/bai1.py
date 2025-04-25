import os
from typing import Union, List

# Định nghĩa các class
class Person:
    def __init__(self, name: str, yob: int):
        self.name = name
        self.yob = yob

    def describe(self):
        pass

class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self.grade = grade
    
    def describe(self):
        return f"Student - Name: {self.name:<10}, YOB: {self.yob:<4}, Grade: {self.grade:<10}"

class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self.subject = subject
    
    def describe(self):
        return f"Teacher - Name: {self.name:<10}, YOB: {self.yob:<4}, Subject: {self.subject:<10}"

class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self.specialist = specialist
    
    def describe(self):
        return f"Doctor  - Name: {self.name:<10}, YOB: {self.yob:<4}, Specialist: {self.specialist:<10}"

class Ward:
    def __init__(self, name: str):
        self.name = name
        self.people: List[Person] = []
        # Thêm dữ liệu mẫu khi khởi tạo
        self._initialize_sample_data()
    
    def _initialize_sample_data(self):
        self.add_person(Student('Hùng', 2003, '12A3'))
        self.add_person(Teacher('Hải', 1998, 'Toán'))
        self.add_person(Doctor('Hợp', 2000, 'Răng-hàm-mặt'))
        self.add_person(Doctor('Long', 1995, 'Thú y'))
        self.add_person(Student('Đức', 2004, '12A6'))
        self.add_person(Teacher('Hào', 1996, 'Lý'))
    
    def add_person(self, person: Person) -> None:
        self.people.append(person)
    
    def describe(self) -> None:
        print(f"Ward: {self.name}")
        for person in self.people:
            print(person.describe())
    
    def count_doctors(self) -> int:
        return sum(isinstance(person, Doctor) for person in self.people)
    
    def sort_by_age(self) -> None:
        self.people.sort(key=lambda x: x.yob, reverse=True)
    
    def average_teacher_yob(self) -> float:
        teachers = [p for p in self.people if isinstance(p, Teacher)]
        return sum(t.yob for t in teachers) / len(teachers) if teachers else 0.0

def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def get_person_input() -> Union[Person, None]:
    try:
        name = input("Nhập tên: ").strip()
        yob = int(input("Nhập năm sinh: "))
        role = input("Nhập vai trò (Student/Teacher/Doctor): ").strip().lower()
        
        if role == 'student':
            grade = input("Nhập lớp: ").strip()
            return Student(name, yob, grade)
        elif role == 'teacher':
            subject = input("Nhập môn học: ").strip()
            return Teacher(name, yob, subject)
        elif role == 'doctor':
            specialist = input("Nhập chuyên khoa: ").strip()
            return Doctor(name, yob, specialist)
        else:
            print("Vai trò không hợp lệ!")
            return None
    except ValueError:
        print("Năm sinh phải là số nguyên!")
        return None

def display_menu() -> None:
    print("\n=== QUẢN LÝ WARD ===")
    print("1. Thêm người")
    print("2. In danh sách người")
    print("3. Đếm số bác sĩ")
    print("4. Sắp xếp theo năm sinh")
    print("5. Tính năm sinh trung bình của giáo viên")
    print("6. Thoát")

def main():
    ward = Ward("Ward 1")
    
    while True:
        clear_screen()
        display_menu()
        
        choice = input("\nNhập lựa chọn (1-6): ").strip()
        print("-" * 40)
        
        try:
            if choice == '1':
                person = get_person_input()
                if person:
                    ward.add_person(person)
                    print("Đã thêm người thành công!")
            
            elif choice == '2':
                ward.describe()
            
            elif choice == '3':
                print(f"Số lượng bác sĩ: {ward.count_doctors()}")
            
            elif choice == '4':
                ward.sort_by_age()
                print("Đã sắp xếp danh sách theo năm sinh!")
            
            elif choice == '5':
                avg_yob = ward.average_teacher_yob()
                print(f"Năm sinh trung bình của giáo viên: {avg_yob:.2f}")
            
            elif choice == '6':
                print("Đã thoát chương trình!")
                break
            
            else:
                print("Lựa chọn không hợp lệ!")
                
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")
        
        input("\nNhấn Enter để tiếp tục...")

if __name__ == "__main__":
    main()