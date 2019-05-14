import numpy as np
import pickle as pk
import utilserv as ut
import os
import re

def trainingSet():
    data_set = [
        [1,787,24.2,17.7,8.0,5.4,11.7,8.4,1.8,4.0,5.6,2.8,1.3,5.9,3.1],
        [2,737,23.6,14.9,11.6,6.5,7.7,6.3,11.3,3.1,3.5,3.1,3.5,2.7,1.9],
        [3,754,23.2,11.7,10.9,8.4,10.0,9.1,6.4,4.8,3.3,3.9,4.4,2.4,1.4],
        [4,621,24.6,10.8,11.8,11.7,8.2,8.2,4.0,6.2,4.2,5.1,2.5,1.2,1.4],
        [5,693,22.8,8.8,12.8,21.4,7.9,5.9,3.1,5.9,3.3,4.6,2.0,0.3,0.8]
    ]

    data_list = []
    for i in range(0,len(data_set)):
        for j in range(2, len(data_set[i])):
            data_set[i][j] = data_set[i][j]/10

    for k in range(0,len(data_set)):
        for i in range(0, data_set[k][1]):
            data = []
            data.append(data_set[k][0])
            for j in range(2, len(data_set[k])):
                ans_good = int(data_set[k][1]*data_set[k][j]/100)
                ans_bad = data_set[k][1] - ans_good
                target = np.random.hypergeometric(ngood = ans_good, nbad = ans_bad, nsample = 13, size = None)
                data.append(target)
            data_list.append(data)

    f = open('data_list.tdat', 'wb')
    pk.dump(data_list, f)
    f.close()

def kvalue_check():
    f = open('data_list.tdat', 'rb')
    data_list = pk.load(f)
    a = ut.elbow(data_list)
    print(a)

def testisFile():
    if os.path.isfile('./checkpoint'):
        print("yes")