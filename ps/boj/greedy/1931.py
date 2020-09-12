from operator import itemgetter
import sys
num_of_task = int(sys.stdin.readline())
result = 0
prev_finish_time = 0
task_set = []
for i in range(0, num_of_task):
    input_array = sys.stdin.readline().split(' ')
    task_set.append((int(input_array[0]), int(input_array[1])))
task_set.sort(key=itemgetter(1, 0))
for i in range(len(task_set)):
    if i == 0:
        result = result + 1
        prev_finish_time = task_set[i][1]
    else:
        if task_set[i][0] >= prev_finish_time:
            result = result + 1
            prev_finish_time = task_set[i][1]
print(result)