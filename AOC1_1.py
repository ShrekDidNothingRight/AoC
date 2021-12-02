file = open(r"C:\Users\alt\desktop\aoc\data.txt")

#compare = lines.toint[+1]

#print("the original list is: " + str(file.readlines()))

sub_data = list(map(int, file.readlines()))
count = 0
for i in range(len(sub_data)):
    if sub_data[i] > sub_data[i - 1]:
        count = count + 1
print(count)
