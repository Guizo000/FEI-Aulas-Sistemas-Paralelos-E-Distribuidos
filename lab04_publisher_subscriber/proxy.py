import zmq

context = zmq.Context()

pub = context.socket(zmq.XPUB)
pub.bind("tcp://*:5556")
pub.bind("tcp://*:5557")
pub.bind("tcp://*:5558")

sub = context.socket(zmq.XSUB)
sub.bind("tcp://*:5555")
sub.bind("tcp://*:5554")

zmq.proxy(pub, sub)
pub.close()
sub.close()
context.close()
