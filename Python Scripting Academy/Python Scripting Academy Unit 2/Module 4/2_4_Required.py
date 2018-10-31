# [x] create The Weather
# [x] copy and paste in edX assignment page
# import world temp as mean_temp
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt
# open the file into variable mean on append+ mode
mean = open('mean_temp.txt', 'a+')
# Write a new line for Rio de Janeiro
mean.write("Rio de Janeiro,Brazil,30.0,18.0\n")
# use .seek() to move the pointer to the beginning of the file
mean.seek(0)
# read the first line of text into a variable called: headings + get read of the "\n" just in case (although it could be left gere actually)
headings = mean.readline().strip()
#convert headings to a list using .split(',') which splits on each comma
headings_list = headings.split(',')
# assign remaining lines to a city_temp variable
city_temp = mean.readlines()
# remove the newline character at the end of each line
count = 0
for a in city_temp:
    city_temp[count] = a[:-1]
    count += 1
# convert the city_temp to a list using .split(',') for each .readline() in the loop
city_lines = []
for a in range(0,len(city_temp)):
        city_lines += city_temp[a].split(',')
# print each city & the highest monthly average temperature
for a in range(0,len(city_temp)):
    print(headings_list[0].capitalize()+" of "+city_lines[4*a],headings_list[2],"is",city_lines[4*a+2],"Celsius")
# close file
mean.close()