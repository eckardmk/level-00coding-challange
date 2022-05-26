def time_convertor(num):
    number = int(num)

    count_hours = 0

    while number >= 60:
        number -= 60
        count_hours += 1

    minutes = number
    if count_hours > 1:
        handles_plurals_for_hours = "hours"

    if minutes > 1:
        handles_plurals_for_minutes = "minutes"

    time = f"{count_hours} {handles_plurals_for_hours}, {minutes} {handles_plurals_for_minutes}"
    return time


timed = time_convertor(133)
print(timed)
