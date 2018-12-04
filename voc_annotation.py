import xml.etree.ElementTree as ET
import os
from pathlib import Path


sets = ['train']

classes = ["bee"]


def convert_annotation(image_id, list_file, image_set):
    in_file = open('dataset/%s/%s.xml' % (image_set, image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = os.getcwd()

for image_set in sets:
    list_file = open('%s.txt' % image_set, 'w')

    for file in os.listdir('dataset/%s' % image_set):
        if file.endswith(".jpg"):
            image_id = file.replace('.jpg', '')
            if Path('dataset/%s/%s.xml' % (image_set, image_id)).is_file():
                list_file.write('%s/dataset/%s/%s.jpg'%(wd, image_set, image_id))
                convert_annotation(image_id, list_file, image_set)
                list_file.write('\n')

    list_file.close()
