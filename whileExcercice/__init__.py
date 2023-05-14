def readGrades():
    grade = 0;
    for index in range(1, 6):
        grade += float(input(f"nota {index } "))

    average = grade / 5

    print(f"media aritmetica {average}")

def multiplicationTable(table: int):
    index = 0;

    while index <= 10:
        print(f"{table} X {index} = {table*index}")
        index+= 1

multiplicationTable(3)
readGrades()
