things = []
safe = 0

with open('p1input.txt', 'r') as file:
    for line in file:
        things.append(list(map(int, line.split())))

def is_safe(report):
    increasing = decreasing = True
    valid_diff = True

    for i in range(1, len(report)):
        if report[i] > report[i-1]:
            decreasing = False
        elif report[i] < report[i-1]:
            increasing = False
        else:
            increasing = decreasing = False
        
        if abs(report[i] - report[i - 1]) < 1 or abs(report[i] - report[i - 1]) > 3:
            valid_diff = False
            break  # No need to check further if invalid difference found

    return (increasing or decreasing) and valid_diff

for report in things:
    if is_safe(report):
        safe += 1
    else:
        # Project Dampener garbage (this story is ridiculous)
        for i in range(len(report)):
            modified_report = report[:i] + report[i+1:]
            if is_safe(modified_report):
                safe +=1
                break
            else:
                continue

print("The amount of safe reports is: " + str(safe))