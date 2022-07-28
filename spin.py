import sys, threading, time

class SpinnerThread(threading.Thread):
    def __init__(self):
        super().__init__(target=self._spin)
        self._stopevent = threading.Event()

    def stop(self):
        self._stopevent.set()

    def _spin(self):
        while not self._stopevent.is_set():
            for t in '|/-\\':
                sys.stdout.write('Processing...' + t)
                sys.stdout.flush()
                time.sleep(0.1)
                sys.stdout.write('\r')