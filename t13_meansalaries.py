# calculate mean salary

salaries_to_employees = {1000: 20, 1100: 8, 1200: 10, 2100: 7, 2500: 5}

total_employees = sum(salaries_to_employees.values())
total_salaries = sum(salaries_to_employees)

print("Total number of employees:", total_employees)
print("Total salary paid:", total_salaries)

print("Mean weekly salary:", total_salaries / total_employees)
