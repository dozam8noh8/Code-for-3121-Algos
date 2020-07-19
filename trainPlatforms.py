arr = [100, 103, 106, 108, 121, 161, 191]
dep = [104, 110, 150, 130, 122, 109, 103]

both = []
for time in arr:
    both.append((time, True))

for time in dep: # Departures considered false.
    both.append((time, False))

ordered = sorted(both)
counter = 0
max = 0
for (time, arrival) in ordered:
    print("Time is " + str(time) + " arrival is " + str(arrival))
    if arrival:
        counter += 1
    else:
        counter -= 1
    if counter > max:
        max = counter
#print(both)


print(max)