import sys
import time
import subprocess
import threading
import queue
import boto3


class Producer:
    
    def __init__(self, config, filename):

        self.client = boto3.client('kinesis', endpoint_url='http://localhost:4566')
        self.line_queue = queue.Queue(100)

        send_thread = threading.Thread(target = self.send_)
        send_thread.start()

        self.poll_file(filename)

    def poll_file(self,filename):
        f = subprocess.Popen(['tail','-F',filename],\
                stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        while True:
            line = f.stdout.readline()
            self.line_queue.put(line.rstrip())
        
        
    def send_(self):
        while True:
            cnt_queue = self.line_queue.qsize()
            for i in range(0, cnt_queue):
                self.put_record(self.line_queue.get())
            print("---")
            time.sleep(60)


    def put_record(self, data):
        response = self.client.put_record(
            StreamName='KinesisTest',
            Data=data,
            PartitionKey='temp'
        )

        print(response)


if __name__ == '__main__':

    conf =  None
    prod  = Producer(conf, sys.argv[1])
