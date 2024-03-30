def jsonToDict (fileName:str, attributes:list) -> dict :
    file = open(fileName,"r")
    ret_dict = {}
    for line in file.readlines():
        line = line.strip()
        if (len(line) >= 3):
            line = line.replace('"','')
            line = line.split(':')
            if (str(line[0]) in attributes):
                ret_dict.update({str(line[0]):str(line[1])})
    file.close()
    return ret_dict