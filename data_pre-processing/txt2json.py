import xml.etree.ElementTree as ET
import os
import json
def txt2json(txt_path):
    f = open(txt_path, 'r')
    res = []
    for line in f.readlines():
        line = line.strip()
        image_name = line.split(' ')[0]
        seg_name = line.split(' ')[1]
        for item in line.split(' ')[2:]:
            x1, y1, x2, y2, label, confidence = [int(x) for x in item.split(",")]
            res.append({'name':image_name, 'defect_name': str(label), 'bbox':[x1, y1, x2, y2]})
    f.close()
    json_name = txt_path.replace('txt', 'json')
    print ('json_name:',json_name)
    with open(json_name, 'w') as fp:
         json.dump(res, fp, indent=4, separators=(',', ': '))
    print('over!')

if __name__ == '__main__':
    txt_path = '/home/ting/tensorflow/Driving/train_dataset/train.txt'
    txt2json(txt_path)
