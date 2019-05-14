from sklearn.cluster import KMeans
import numpy as np

def elbow(X) -> int:
    sse = []
    for i in range(1, 11):
        km = KMeans(n_clusters=i, init='k-means++', random_state=0)
        km.fit(X)
        sse.append(km.inertia_)
    max = 0
    #K의 갯수로 추정되는.. 숫자.
    maxpoint = 0
    
    for i in range(2, len(sse)-2):
        ySub = sse[i] - sse[i+1]
        ySub2 = sse[i+1] - sse[i+2]
        if max < abs(ySub - ySub2):
            max = abs(ySub - ySub2)
            maxpoint = i+1
    #plt.plot(range(1, 11), sse, marker='o')
    #plt.xlabel('Quantity of Clusters')
    #plt.ylabel('SSE')
    #plt.show()
    return maxpoint
