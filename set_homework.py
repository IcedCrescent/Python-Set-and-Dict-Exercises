height_input = input('Enter the heights separeted by white space: ')
splitted = height_input.split(' ') # [str, str, str,...]
distinct_height = set()
for i in splitted:
    distinct_height.add(int(i))
count = 0
sum_of_heights = 0
for i in distinct_height:
    count += 1
    sum_of_heights += i
average = sum_of_heights / count
# average = sum_of_heights / len(distinct_height)
print(f'The average of all the plants with distinct heights: {average}')