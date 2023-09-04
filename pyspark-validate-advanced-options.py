import sys
from operator import add
import os
from pyspark.sql import SparkSession


if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("ValidateAdvancedOptions")\
        .getOrCreate()
    
    m = {0: [], 1: 
         ["Folder-1/Folder-2/input.txt"], 
         2: ["Folder-1/Folder-2/input.txt", "Folder-1/Folder-2/spark-examples_2.11-2.4.4.jar"], 
         3: ["Folder-1/Folder-2/input.txt", "Folder-1/Folder-2/spark-examples_2.11-2.4.4.jar", "Folder-1/Folder-2/100_doors.py"]}

    print("the map is ", m)

    n = len(sys.argv)
    if n == 1:
        print("missing args")
    elif n == 2:
        print("entered in elif")
        x = int(sys.argv[1])
        print("doing stat for files: ", m[x])

        for f in m[x]:
            p = "/app/mount/" + f
            if os.path.exists(p):
                print("File exists: ", p)
            else:
                print("File doesnt exist: ", p)
    else:
        print("entered else", sys.argv)