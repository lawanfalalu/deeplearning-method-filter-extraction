import csv
def getImageLabel():
    #import matplotlib.pyplot as plt
    #import matplotlib.image as pxd
    #Setting the path to the images directory
    path = 'C:/tomato/train/list.csv'
    file = open(path, newline='')
    reader = csv.reader(file) # reading the lists; imagenames, labels.l
    next(reader) # header of the list in CSV
    data = [list for list in reader]
    '''
    img = "C:/tomato/train/32X32/"+data[200][0]
    '''
    fls = []
    lbs = []
    for i in range(300):
        fls.append("C:/tomato/train/32X32/"+data[i][0])
        lbs.append(data[i][1])
    #RETURNING LIST OF FILES, LABELS    
    return fls,lbs
