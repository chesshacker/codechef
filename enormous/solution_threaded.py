#! /usr/bin/env python3

# This could definitely be improved, but it's pretty clear that the
# overhead of communicating through the queue is going to keep this
# approach from competing with simpler approaches.  Still, it was fun
# to write this little producer/consumer version.

import sys
import queue
import threading
import logging

queue_size = 0
# logging.basicConfig(level=logging.DEBUG)

def get_integers(q):
    while True:
        line = q.get()
        if line == '':
            logging.debug('consumer: received empty line')
            raise StopIteration
        logging.debug('consumer: received line: ' + line[:-1])
        yield int(line)
        q.task_done()

def consume_lines():
    logging.debug('consumer: started')
    count = sum(1 for x in get_integers(q) if x % k == 0)
    print(count)
    logging.debug('consumer: done')

def produce_lines():
    logging.debug('producer: started')
    for line in sys.stdin:
        logging.debug('producer: produced line: ' + line[:-1])
        q.put(line)
    q.put('')
    logging.debug('producer: done')

class Producer():
    def __init__(self):
        pass
    def __call__(self):
        produce_lines()

n, k = map(int,sys.stdin.readline().split())
q = queue.Queue(queue_size)
producer = threading.Thread(target=Producer())
logging.debug('    main: created thread')
producer.daemon = True
producer.start()
logging.debug('    main: started thread')
consume_lines()
logging.debug('    main: done')
