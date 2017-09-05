import tensorflow as tf
import numpy as np

a = tf.Variable(5.0, name='a')
b = tf.Variable(6.0, name ='b')
c = tf.mul(a, b, name='c')
d = tf.add(a,b,name = "d")

with tf.Session() as sess:    

    print (type(sess.graph_def))
    print (type(tf.get_default_graph()))
    
    tf.get_default_graph().add_to_collection("b", b)
    for node in sess.graph_def.node:
        print node.name

    sess.run(tf.initialize_all_variables())
    print a.eval() # 5.0
    print b.eval() # 6.0
    print c.eval() # 30.0
    print d.eval()
    print sess.run(tf.get_default_graph().get_tensor_by_name("c:0"))
    for variable in tf.trainable_variables():
        tensor = tf.constant(variable.eval())
        tf.assign(variable, tensor, name="nWeights")
        print "assign variable"
    tf.train.write_graph(sess.graph_def, 'models/', 'graph.pb', as_text=False)

