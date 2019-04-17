import tensorflow as tf
from sklearn.cluster import KMeans
import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs

num_features = 6

#난수 데이터 생성
data_quantity = 1000
data_list = []
input_list = [
    #연령, 인원, 문학, 장르소설, 취미오락여행건강, 철학사상종교, 자기계발, 경제경영, 가정육아요리, 정치사회시사, 예술문화, 역사,지리
    [20, 789, 28.5, 15.6, 9.4, 7.6, 12.0, 6.0, 2.8, 3.8, 4.4, 3.6],
    [30, 718, 24.9, 13.3, 12.2, 7.0, 9.6, 6.1, 9.0, 3.7, 3.8, 2.7],
    [40, 744, 25.5, 13.5, 12.7, 7.3, 8.4, 9.1, 6.8, 3.6, 3.1, 3.8],
    [50, 595, 30.6, 11.2, 12.4, 12.5, 7.4, 6.4, 5.1, 3.5, 3.3, 2.7],
    [60, 421, 25.4, 7.0, 10.8, 20.8, 5.7, 6.1, 3.0, 5.9, 4.1, 6.3]
]
for i in range(0, data_quantity):
    data = []
    data.append(random.randint(2, 6)*10)
    data.append(random.randint(1, 5))
    data.append(random.randint(1, 5))
    data.append(random.randint(1, 5))
    data.append(random.randint(1, 5))
    data.append(random.randint(1, 5))
    data.append(random.randint(1, 5))
    data.append(random.randint(1, 5))
    data.append(random.randint(1, 5))
    data.append(random.randint(1, 5))
    data.append(random.randint(1, 5))
    data_list.append(data)

    
X = data_list
def elbow(X):
    sse = []
    for i in range(1, 11):
        km = KMeans(n_clusters=i, init='k-means++', random_state=0)
        km.fit(X)
        sse.append(km.inertia_)
        print(km.fit(X))
    
        
    plt.plot(range(1, 11), sse, marker='o')
    plt.xlabel('Quantity of Clusters')
    plt.ylabel('SSE')
    plt.show()
    
elbow(X)