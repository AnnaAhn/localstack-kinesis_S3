import sys
import time
import subprocess
import threading
import queue
import boto3
import json

class Producer:
    
    def __init__(self, config, filename):

        self.client = boto3.client('kinesis', endpoint_url=config["endpoint"])
        self.line_queue = queue.Queue(100)

        send_thread = threading.Thread(target = self.send_)
        send_thread.start()

        self.poll_file(filename)

    def poll_file(self,filename):
        f = subprocess.Popen(['tail','-F',filename],\
                stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        try:
            while True:
                line = f.stdout.readline()
                self.line_queue.put(line.rstrip())
        except KeyboardInterrupt:
            if f:
                f.terminate()
        
    def send_(self):
        while True:
            cnt_queue = self.line_queue.qsize()
            for i in range(0, cnt_queue):
                self.put_record(self.line_queue.get())
            time.sleep(1)


    def put_record(self, data):
        response = self.client.put_record(
            StreamName='KinesisTest',
            Data=data,
            PartitionKey='temp'
        )

        print(response)


if __name__ == '__main__':

    conf_file =  sys.argv[1]
    with open(conf_file) as fin:
        conf = json.load(fin)
        prod  = Producer(conf, sys.argv[2])
