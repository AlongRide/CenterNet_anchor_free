
f = open("/home/ting/tensorflow/Driving/train_dataset/train.txt","r")
lines = f.readlines()
for line in lines:
    line
    txt = line[0:6]
    #print(txt)
    f='/home/ting/tensorflow/Driving/txt_train/' +txt+'.txt'
    file = open(f, 'w')
    print('file name:',f)
    print('line:',line)
    line=line[22:]
    print('line[22:]',line)
    for db in line.split():
        print('db[5]',db)
        file.write(db[:-2])
        file.write('\n')
