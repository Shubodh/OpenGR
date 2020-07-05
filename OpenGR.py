import os
import copy
import argparse
import open3d as o3d
import numpy as np

def draw_registration_result(source, target, transformation):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    
    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])
    
    source_temp.transform(transformation)
    
    o3d.visualization.draw_geometries([source_temp, target_temp])


if __name__ == "__main__":
    #Argument Parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('--file1', '-f1', type=str, required=True)
    parser.add_argument('--file2', '-f2', type=str, required=True)
    parser.add_argument('--file3', '-f3', type=str, required=True)
    parser.add_argument('--file4', '-f4', type=str, required=True)
    parser.add_argument('--o', '-o', type=float, required=True)
    parser.add_argument('--d', '-d', type=float, required=True)
    parser.add_argument('--t', '-t', type=int, required=True)
    parser.add_argument('--n', '-n', type=int, required=True)
    parser.add_argument('--output', '-m', type=str, required=True)
    args = parser.parse_args()

    #Bash Command
    cmnd = "../bin/Super4PCS -i " + args.file1 + " " + args.file2 + " -o " + str(args.o) + " -d " +  str(args.d) + " -t " + str(args.t) + " -n " + str(args.n) + " -m " + args.output
    print(cmnd)

    #Run OpenGR with inputs
    os.system(cmnd)

    #Source and Target files for plotting
    target = args.file3
    src = args.file4
    # target = (args.file1).split('.')
    # target = target[0] + '.pcd'
    # src = (args.file2).split('.')
    # src = src[0] + '.pcd'
    print('\n',end = "")
    print("Plotting...",'\n')
    print("Source File :",src)
    print("Target File :",target)

    #Read point clouds from .pcd files
    target_down = o3d.io.read_point_cloud(target)
    source_down = o3d.io.read_point_cloud(src)

    #Read matrix
    f = open(args.output,'r')
    lines = f.readlines()
    cnt = 1
    arr = np.zeros([4,4],dtype=float)
    i = 0
    for line in lines:
        j = 0
        cnt += 1
        if(cnt <= 3):
            continue
        tmp = line.split("  ")
        for el in tmp:
            arr[i][j] = float(el)
            j+=1
        i += 1
    
    print('\n',end = "")
    print("Transformation Matrix")
    print('\n',end = "")
    print(arr)

    #Plot...    
    draw_registration_result(source_down,target_down, arr)

