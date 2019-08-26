import os
from glob import glob
import shutil
import cv2
import math

def transform_file(image_file, target_dir):
    image = cv2.imread(image_file)
    image_file_name = os.path.basename(image_file)
    
    try:
        #image = cv2.resize(image, resize_shape)
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        new_file = os.path.join(target_dir, image_file_name)
        cv2.imwrite(new_file, image)
        #shutil.copy(image_file, new_face_dir)
    except:
        print('error resizing image, will not save it'.format())

def copy_and_transform_files(files, training_dir, validate_dir, train_segment_size):
    files_count = len(files)
    training_count = math.ceil(files_count * train_segment_size)
    training_files = files[:training_count]
    validate_files = files[training_count:]

    for image_file in training_files:
        transform_file(image_file, training_dir)
        
    for image_file in validate_files:
        transform_file(image_file, validate_dir)
        


if __name__ == '__main__':
    parent_dir = './raw/'
    new_dir = './raw-grouped'
    resize_shape = (150,150)
    train_segment_size = 0.9

    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    train_dir = os.path.join(new_dir, 'train')
    validate_dir = os.path.join(new_dir, 'validate')

    if not os.path.exists(train_dir):
        os.makedirs(train_dir)

    if not os.path.exists(validate_dir):
        os.makedirs(validate_dir)
    

    # Loop over all the directories of each person
    for class_dir in glob(os.path.join(parent_dir, "*")):
        face_dir = os.path.join(class_dir, '')
        class_name = os.path.basename(class_dir)

        new_training_face_dir = os.path.join(train_dir, class_name)
        new_validate_face_dir = os.path.join(validate_dir, class_name)

        # make a new training class directory
        if not os.path.exists(new_training_face_dir):
            os.makedirs(new_training_face_dir)
        
        # mae a new validate class directory
        if not os.path.exists(new_validate_face_dir):
            os.makedirs(new_validate_face_dir)
        
        files = glob(os.path.join(face_dir, '*.jpg'))
        
        #print(files, new_training_face_dir, new_validate_face_dir, train_segment_size)
        copy_and_transform_files(files, new_training_face_dir, new_validate_face_dir, train_segment_size)

        
