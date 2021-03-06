import os
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
import json
import numpy as np
import shutil
import pandas as pd
defect_name2label = {
    'red': 1, 'green': 2, 'yellow': 3, 'red_left': 4, 'red_right': 5,'yellow_left': 6, 
    'yellow_right': 7, 'green_left': 8, 'green_right': 9, 'red_forward': 10,'green_forward': 11,
    'yellow_forward': 12, 'horizon_red': 13, 'horizon_green': 14, 'horizon_yellow': 15,
    'off': 16, 'traffic_sign': 17, 'car': 18, 'motor': 19, 'bike': 20,
    'bus': 21, 'truck': 22, 'suv':23, 'express': 24, 'person': 25
}

class Fabric2COCO:
    def __init__(self,mode="train"):
        self.images = []
        self.annotations = []
        self.categories = []
        self.img_id = 0
        self.ann_id = 0
        self.mode =mode
        if not os.path.exists("./coco/images/{}".format(self.mode)):
            os.makedirs("./coco/images/{}".format(self.mode))

    def to_coco(self, anno_file,img_dir):
        self._init_categories()
        anno_result= pd.read_json(open(anno_file,"r"))
        name_list=anno_result["name"].unique()
        for img_name in name_list:
            img_anno = anno_result[anno_result["name"] == img_name]
            bboxs = img_anno["bbox"].tolist()
            defect_names = img_anno["defect_name"].tolist()
            assert img_anno["name"].unique()[0] == img_name

            img_path=os.path.join(img_dir,img_name)
            img =cv2.imread(img_path)
            h,w,c=img.shape
            #h,w=1000,2446
            self.images.append(self._image(img_path,h, w))

            self._cp_img(img_path)

            for bbox, defect_name in zip(bboxs, defect_names):
                print ('before_name:',defect_name)
                #label= defect_name2label[defect_name]
                label= defect_name
                if label == 1 or label == 2 or label == 3 or label == 4 or label == 5 or label == 6 or label == 7 or label == 8 or label == 9 or label == 10 or label == 11 or label == 12 or label == 13 or label == 14 or label == 15 or label == 16:
                  label = 1
                if label == 17:
                  label = 2
                if label == 18:
                  label = 3
                if label == 19:
                  label = 4
                if label == 20:
                  label = 5
                if label == 21:
                  label = 6
                if label == 22:
                  label = 7
                if label == 23:
                  label = 8
                if label == 24:
                  label = 9
                if label == 25:
                  label = 10
                print ('after_name:',label)
                annotation = self._annotation(label, bbox)
                self.annotations.append(annotation)
                self.ann_id += 1
            self.img_id += 1
        instance = {}
        instance['info'] = 'fabric defect'
        instance['license'] = ['none']
        instance['images'] = self.images
        instance['annotations'] = self.annotations
        instance['categories'] = self.categories
        return instance

    def _init_categories(self):
        for v in range(1,26):
            #print('v:',v)
            category = {}
            category['id'] = v
            category['name'] = str(v)
            category['supercategory'] = 'defect_name'
            self.categories.append(category)
        #for k, v in defect_name2label.items():
        #     category = {}
        #     category['id'] = v
        #     category['name'] = k
        #     category['supercategory'] = 'defect_name'
        #     self.categories.append(category)

    def _image(self, path,h,w):
        image = {}
        image['height'] = h
        image['width'] = w
        image['id'] = self.img_id
        image['file_name'] = os.path.basename(path)
        return image

    def _annotation(self,label,bbox):
        area=(bbox[2]-bbox[0])*(bbox[3]-bbox[1])
        points=[[bbox[0],bbox[1]],[bbox[2],bbox[1]],[bbox[2],bbox[3]],[bbox[0],bbox[3]]]
        annotation = {}
        annotation['id'] = self.ann_id
        annotation['image_id'] = self.img_id
        annotation['category_id'] = label
        annotation['segmentation'] = [np.asarray(points).flatten().tolist()]
        annotation['bbox'] = self._get_box(points)
        annotation['iscrowd'] = 0
        annotation['area'] = area
        return annotation

    def _cp_img(self, img_path):
        shutil.copy(img_path, os.path.join("coco/images/{}".format(self.mode), os.path.basename(img_path)))

    def _get_box(self, points):
        min_x = min_y = np.inf
        max_x = max_y = 0
        for x, y in points:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        '''coco,[x,y,w,h]'''
        return [min_x, min_y, max_x - min_x, max_y - min_y]

    def save_coco_json(self, instance, save_path):
        import json
        with open(save_path, 'w') as fp:
            json.dump(instance, fp, indent=1, separators=(',', ': '))

img_dir = "/home/ting/tensorflow/Driving/train_dataset/train_image"
anno_dir="/home/ting/tensorflow/Driving/train_dataset/train.json"
fabric2coco = Fabric2COCO()
train_instance = fabric2coco.to_coco(anno_dir,img_dir)
if not os.path.exists("coco/annotations/"):
    os.makedirs("coco/annotations/")
fabric2coco.save_coco_json(train_instance, "coco/annotations/"+'0630_instances_{}.json'.format("train"))


