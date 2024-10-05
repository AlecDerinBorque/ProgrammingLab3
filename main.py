



def greet_user(name):
    print(f"Hello, {name}!")

def print_details(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

def calculate_sum(*args):
    print("The sum is:",sum(args))

def calculate_area(length: int, width: int, unit: str = "meters"):
    print(f"The area is {length * width} square {unit}.")


def add_numbers(a: int, b: int):
    return a + b





def info_header(name, panther_id, section, semester, assignment):
    print("=" * 77)
    print(f" PROGRAMMER: {name}")
    print(f" PANTHER ID: {panther_id}")
    print()
    print(f" CLASS: COP2047")
    print(f" SECTION: {section}")
    print(f" SEMESTER: {semester}")
    print()
    print(f" ASSIGNMENT: {assignment}")
    print()
    print(f" CERTIFICATION: I understand FIU's academic policies, and I certify that this work is my")
    print(f"                own and that none of it is the work of any other person")
    print("=" * 77)


def header_caller(step_number: int):
    print("\n\n")
    print("=" * 20)
    print(f"Step: {step_number}")
    print("=" * 20)


def main() -> None:
    header_caller(2)
    info_header("Alec Borque", 6280315, "U04 1248", "Fall 2024", "Lab 3")

    header_caller(3)
    greet_user("Einstein")
    greet_user("Newton")

    header_caller(4)
    print_details("Alice", 30, "New York")
    print_details(name="Bob", city="Los Angeles", age = 30)

    header_caller(5)
    calculate_sum(1,2,3,)
    calculate_sum(4,5,6,7,8)

    header_caller(6)
    calculate_area(5,10)
    calculate_area(5,10, unit="feet")

    header_caller(7)
    results = add_numbers(a=2,b=3)
    print(f"Results = {results}")




if __name__ == "__main__":
    main()


