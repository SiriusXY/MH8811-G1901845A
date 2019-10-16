import json

def serialize(l):
    data_type=type(l)
    if data_type is list:
        
        res="list|"

        for i in l:
            res=res + str(i)
            res=res + ";"
            res=res + str(type(i))
            res=res + "|"

        return res[:-1]
    
    elif data_type is dict:
        
        res="dict|"

        for i in l:
            res=res + str(i)
            res=res + ":"
            res=res + str(l[i])
            res=res + ";"
            res=res + str(type(l[i]))
            res=res + "|"
            
        return res[:-1]

def deserialize(s):
    string_1 = s.split("|")
    type_1 = string_1[0]
    string_2 = string_1[1:]

    if type_1 == "list":
        output=list()
        for i in string_2:
            string_3=i.split(";")
            element_type=string_3[1]
            element=string_3[0]
            if element_type == "<class 'int'>":
                output.append(int(element))
            elif element_type == "<class 'float'>":
                output.append(float(element))
            else:
                output.append(element)
        return(output)

    elif type_1 == "dict":
        output=dict()
        for i in string_2:
            string_3=i.split(":")
            key=string_3[0]
            string_4=string_3[1].split(";")
            value=string_4[0]
            value_type=string_4[1]
            if value_type == "<class 'int'>":
                output[key]=int(value)
            elif value_type == "<class 'float'>":
                output[key]=float(value)
            else:
                output[key]=value
        return(output)

def compare(item1, item2):
    if type(item1) != type(item2):
        return False
    else:
        if isinstance(item1, list):
            if item1 == item2:
                return True
            else:
                return False
        elif isinstance(item1, dict):
            if len(item1) != len(item2):
                return False

            for i in item1:
                if i not in item2:
                    return False
                elif item1[i] != item2[i]:
                    return False

            return True

set_file = input('Input the name of the file you want to read:')

try:
    file1=open(set_file)
    file_read=json.load(file1)
    file1.close()
except:
    print('Typing error occurs or no such file exists!')
    exit()

serialize1=serialize(file_read)

file2_name=input('Please input the name of the file you want to store the data:')
file2=open(file2_name,'w')
file2.write(serialize1)
file2.close()

file3=open(file2_name)
serialize2=file3.read()
file3.close()

deserialize1=deserialize(serialize2)
if compare(file_read,deserialize1):
    print('The original data structure remains the same.')
else:
    print('It is a fail trial!')