import json
from pathlib import Path

import numpy as np


CLASS_NAMES = ["vehicle", "pedestrian", "truck"]


def load_scene(scene_path):
    scene_path = Path(scene_path) #convert to Path object if not already
    with scene_path.open("r") as f: #read to jsono object 
        scene = json.load(f) #converts into dictionary
    return scene


def class_to_one_hot(class_name): #coneverts class name to one hot vector
    one_hot = np.zeros(len(CLASS_NAMES), dtype=np.float32) #intialize 0.0
    class_index = CLASS_NAMES.index(class_name) #wherever it is present, get the index
    one_hot[class_index] = 1.0 #set index to 1.0 instead of 0.0
    return one_hot 


def encode_object(obj):
    class_vec = class_to_one_hot(obj["class"]) #call previous function to get one hot vector for class
    box = np.array(obj["box"], dtype=np.float32) #convert box to numpy array
    # box = [x, y, z, dx, dy, dz, heading]
    size = box[3:6] #extract size from box 3= dx 4= dy 5 = dz
    heading = np.array([box[6]], dtype=np.float32)
    encoded = np.concatenate([class_vec, size, heading]) #combines everything into one array
    return encoded


def encode_scene(scene): 
    encoded_objects = []
    for obj in scene["objects"]:
        encoded = encode_object(obj)
        encoded_objects.append(encoded)
    return np.stack(encoded_objects, axis=0) #returns all of the endocded objects as a single numpy array