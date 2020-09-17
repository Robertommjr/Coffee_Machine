min_hours = int(input())
max_hours = int(input())
sleeps_hours = int(input())

if min_hours > sleeps_hours:
    resp = "Deficiency"
else:
    if max_hours < sleeps_hours:
        resp = "Excess"
    else:
        resp = "Normal"

print(resp)
