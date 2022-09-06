#returns the century of a given year using floor division

def century(year):
    return (year + 99) // 100

c_answer = century(2022)
print(c_answer)