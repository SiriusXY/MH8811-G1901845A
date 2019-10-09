def getFileLines(fname) :
    fhandle = open(fname)
    lines = []
    for line in fhandle :
        line = line.rstrip()
        if line :
            lines.append(line)
    fhandle.close()
    return lines

def my_min(n):
    My_test_min=None
 
    for i in n:
        if My_test_min is None:
            My_test_min=i
        elif i<My_test_min:
                My_test_min=i
    return My_test_min

def my_max(n):
    My_test_max=None
    for i in n:
        if My_test_max is None:                
            My_test_max=i
        elif i>My_test_max:
            My_test_max=i
    return My_test_max

def my_average(n):
    i=0
    for j in n:
        i += j
    return i/len(n)

def my_median(n):
    n.sort()
    if len(n)%2 == 0:
        med=(n[int(len(n)/2)-1]+n[int(len(n)/2)])/2
        return med

    else:
        med=n[int(len(n)-1)/2]
        return med

def my_range(n):
    return my_max(n)-my_min(n)

def my_variance(n):
    var=0
    for i in n:
        var = var+(i-my_average(n))**2
    var = var/(len(n)-1)
    return var

My_data=getFileLines('MH8811-04-Data.csv')

for i in range(0,len(My_data)):
    My_data[i]=int(My_data[i])

print('My list is:',My_data)
print('The min is:',my_min(My_data))
print('The max is:',my_max(My_data))
print('The average is:',my_average(My_data))
print('The median is:',my_median(My_data))
print('The range is:',my_range(My_data))
print('The sample variance is:',my_variance(My_data))
