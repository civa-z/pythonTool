import tensorflow as tf
import numpy as np

graph=tf.Graph()
with graph.as_default():
    x1 = tf.placeholder(tf.float32, shape=[128, 128])
    x2 = tf.placeholder(tf.float32, shape=[1, 128])

    D3rnn_cell = tf.nn.rnn_cell.BasicRNNCell(num_units=128, input_size=None, activation=tf.nn.tanh)

    with tf.variable_scope("x1"):
        outputsi1, states1 = tf.nn.rnn(D3rnn_cell, [x1], dtype=tf.float32)

    with tf.variable_scope("x1", reuse=True):
        outputsi2, states2 = tf.nn.rnn(D3rnn_cell, [x2], dtype=tf.float32)

with tf.Session(graph=graph) as session:
   tf.initialize_all_variables().run(); 
    
