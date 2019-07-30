import zmq

context = zmq.Context()

recive = context.socket(zmq.PULL)
recive.bind('tcp://127.0.0.1:5557')

sender = context.socket(zmq.PUSH)
sender.connect('tcp://127.0.0.1:5558')

while True:
    data = recive.recv()
    print("开始转发....")
    sender.send(data)