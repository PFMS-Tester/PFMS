file = open('ghj.txt', 'w')

students=['akash', 'ranvir', 'vishu', 'arun']
grades=[10, 20, 30, 40]

for i in range(0, 4):
    entry=students[i] + "-" + str(grades[i]) + '\n'
    file.write(entry)

file.close()
