from tensorflow.contrib.factorization import KMeans
import tensorflow as tf
import numpy as np
import pickle as pk
import utilserv as ut
import os

def keeplearning(new_data):
    #K값 추정을 위해 data_list 파일 불러오기.
    ofile = open('data_list.tdat', 'rb')
    ofile_list = pk.load(ofile)

    #추가된 new_data와 기존의 old file을 합쳐서 저장
    if len(new_data) != 0:
        data_list = new_data + ofile_list
    else:
        data_list = ofile_list
    ofile.close()

    f = open('data_list.tdat', 'wb')
    pk.dump(data_list, f)
    f.close()
    # data_set = [
    #     [1,787,24.2,17.7,8.0,5.4,11.7,8.4,1.8,4.0,5.6,2.8,1.3,5.9,3.1],
    #     [2,737,23.6,14.9,11.6,6.5,7.7,6.3,11.3,3.1,3.5,3.1,3.5,2.7,1.9],
    #     [3,754,23.2,11.7,10.9,8.4,10.0,9.1,6.4,4.8,3.3,3.9,4.4,2.4,1.4],
    #     [4,621,24.6,10.8,11.8,11.7,8.2,8.2,4.0,6.2,4.2,5.1,2.5,1.2,1.4],
    #     [5,693,22.8,8.8,12.8,21.4,7.9,5.9,3.1,5.9,3.3,4.6,2.0,0.3,0.8]
    # ]

    # data_list = []
    # for i in range(0,len(data_set)):
    #     for j in range(2, len(data_set[i])):
    #         data_set[i][j] = data_set[i][j]/10

    # for k in range(0,len(data_set)):
    #     for i in range(0, data_set[k][1]):
    #         data = []
    #         data.append(data_set[k][0])
    #         for j in range(2, len(data_set[k])):
    #             ans_good = int(data_set[k][1]*data_set[k][j]/100)
    #             ans_bad = data_set[k][1] - ans_good
    #             #numpy 초기하분포를 활용해서 통계청 자료 비복원추출
    #             target = np.random.hypergeometric(ngood = ans_good, nbad = ans_bad, nsample = 13, size = None)
    #             data.append(target)
    #         data_list.append(data)

    #파일에 list를 그대로 기록
    # f = open('data_list.tdat', 'wb')
    # pickle.dump(data_list, f)
    # f.close()

    #훈련 전에 일단 기존의 체크포인트 삭제
    if os.path.isfile('./trained_data.ckpt.data-00000-of-00001'):
        os.remove('./trained_data.ckpt.data-00000-of-00001')
    if os.path.isfile('./trained_data.ckpt.index'):
        os.remove('./trained_data.ckpt.index')
    if os.path.isfile('./trained_data.ckpt.meta'):
        os.remove('./trained_data.ckpt.meta')
    if os.path.isfile('./checkpoint'):
        os.remove('./checkpoint')

    #새로운 데이터 훈련
    Data_X = data_list
    k = ut.elbow(data_list)

    #훈련자료 column의 개수
    num_features = 14

    X = tf.placeholder(tf.float32, shape=[None, num_features])

    kmeans = KMeans(inputs = X, num_clusters=k, distance_metric='squared_euclidean', use_mini_batch=True)

    (all_scores, cluster_idx, scores, cluster_centers_initialized, init_op, train_op) = kmeans.training_graph()
    cluster_idx = cluster_idx[0]
    avg_distance = tf.reduce_mean(scores)

    saver = tf.train.Saver()
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)
    sess.run(init_op, feed_dict={X: Data_X})

    #밥맥이기
    for i in range(1, 100):
        _, d, idx = sess.run([train_op, avg_distance, cluster_idx],
                            feed_dict={X: Data_X})

    #훈련된 모델 저장
    saver.save(sess, './trained_data.ckpt')
    print("Trained data save completed.")
    sess.close()
    # print (idx, d)
    # for i in range(0, k):
    #     result = []
    #     for j in range(0, idx.size, 1):
    #         if(idx[j] == i):
    #             result.append(Data_X[j])
    #     print(i, "에 속한 데이터: ", result)
    #     print("\n")

keeplearning([])