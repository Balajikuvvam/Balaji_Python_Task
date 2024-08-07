import time
import math
file_path = r"C:\Users\balaj\OneDrive\Desktop\MY Documents\myTet 3.stl"

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print("process started")
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Time for execution",end_time-start_time)
        print("Ended process")
        return result
    return wrapper

@timing_decorator
def calculate_stl_surface_area(*args,**kwargs):
    
    vertices = []
    stl_file = open(file_path,'r')
    lines = stl_file.readlines()
    for line in lines:
        line = line.split()
        if line[0] == "vertex":
            vertices.append([float(line[1]), float(line[2]), float(line[3])])

    total_area = 0
    for j in range(0, len(vertices), 3):
        x1, y1, z1 = vertices[j]
        x2, y2, z2 = vertices[j+1]
        x3, y3, z3 = vertices[j+2]

        a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
        b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2 + (z3 - z2)**2)
        c = math.sqrt((x1 - x3)**2 + (y1 - y3)**2 + (z1 - z3)**2)

        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))

        total_area += area
    print("Total area:", total_area)

    return total_area

calculate_stl_surface_area(file_path)






