from tensorflow.contrib.factorization import KMeans
import tensorflow as tf
import numpy as np
import utilserv as ut
import pickle as pk

def groupNumber(req_data):
    f = open('data_list.tdat', 'rb')
    data_list = pk.load(f)
    f.close()
    k = ut.elbow(data_list)
    num_features = 14

    X = tf.placeholder(tf.float32, shape=[None, num_features])

    kmeans = KMeans(inputs = X, num_clusters=k, distance_metric='squared_euclidean', use_mini_batch=True)

    (all_scores, cluster_idx, scores, cluster_centers_initialized, init_op, train_op) = kmeans.training_graph()
    cluster_idx = cluster_idx[0]
    avg_distance = tf.reduce_mean(scores)

    save_file = './trained_data.ckpt'
    saver = tf.train.Saver()

    input_data = []
    input_data.append(req_data)

    with tf.Session() as sess:
        saver.restore(sess, save_file)
        _, d, idx = sess.run([train_op, avg_distance, cluster_idx], feed_dict={X: input_data})
        for i in range(0, k):
            for j in range(0, idx.size, 1):
                if(idx[j] == i):
                    return i
        
        sess.cllose()