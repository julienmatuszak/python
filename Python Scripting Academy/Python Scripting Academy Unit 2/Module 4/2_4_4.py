# [x] open inner_planets.txt in write mode
inner_planets = open('inner_planets.txt', 'w')
# [x] write Mercury,Venus, Earth, Mars on separate lines
inner_planets.write("Mercury\nVenus\nEarth\nMars\n")
# [x] close the file and re-open in read mode
inner_planets.close()
# [x] use .read() to read the entire file contents
inner_planets = open('inner_planets.txt', 'r')
inner_planets = inner_planets.read()
# [x] print the entire file contents and close the file
for a in inner_planets:
    print(inner_planets)

# [x] open outer_planets.txt in write mode 'w+' 
outer_planets = open('outer_planets.txt', 'w+')
# [x] write four outer planets in earth's solar system (Jupiter, Saturn, Uranus, Neptune) on separate lines
outer_planets.write("Jupiter\nSaturn\nUranus\nNeptune\n")
# [x] use .seek() to move the pointer to the start of the file
# [x] use .read() to read the entire file contents
outer_planets.seek(0)
# [x] print the entire file contents and close the file
outer_planets = outer_planets.read()
print(outer_planets)

# [x] open a new file days.txt in write plus read mode 'w+' 
# [x] write week days (Monday - Friday) on separate lines to the file
days = open('days.txt', 'w+')
days.write('Monday\nTuesday\nWednesday\nThursday\nFriday\n')
# [x] use .seek() to move the pointer to the start of the file
# [x] use .read() to read the entire file contents
# [x] print the entire file contents and close the file
days.seek(0)
days_file = days.read()
print(days_file)
# [x] use .seek() to move the pointer to the end of the file
# [x] write the weekend days (Saturday & Sunday)
days.seek(0,2)
days.write('Saturday\nSunday\n')
days.seek(0)
days_file = days.read()
print(days_file)

# [x] complete the task
# Provided Code creates and populates task4_file.txt
task4_file = open('task4_file.txt', 'w+')
task4_file.write("Line1\nLine2\nLine3\n")
task4_file.close()
# [x] code here
i = 4
task4_file = open('task4_file.txt', 'a+')
for item in range(5):
    task4_file.write("Line"+str(i)+"\n")
    i += 1
    task4_file.seek(0)
for item in range(8):
    print(task4_file.readline().strip())
    
# [x] complete the task
# Provided Code creates and populates task5_file.txt
task5_file = open('task5_file.txt', 'w+')
task5_file.write("Line---1\nLine---2\nLine---3\nLine---4\nLine---5\nLine---6\nLine---7\nLine---8\nLine---9\nLine--10\n")
task5_file.seek(0)
print("Before:\n"+ task5_file.read()+"\n")
task5_file.close()

# [x] complete the task
# Provided Code creates and populates task5_file.txt
task5_file = open('task5_file.txt', 'w+')
task5_file.write("Line---1\nLine---2\nLine---3\nLine---4\nLine---5\nLine---6\nLine---7\nLine---8\nLine---9\nLine--10\n")
task5_file.seek(0)
print("Before:\n"+ task5_file.read()+"\n")
task5_file.close()

# [x] code here
count = 1
task5_file = open('task5_file.txt', 'r+')
for item in range(1,5):
    task5_file.write("Line---"+str(count)+"\n")
    task5_file.seek(item*18)
    count += 1
# 2 by 2, the file is totally rewritten in r+ mode where the pointer is set (here it's the same example so it writes the same file)
for item in range(10):
    print(task5_file.readline().strip())
    