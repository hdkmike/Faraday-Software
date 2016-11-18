import time

class ArqTransmitter(object):
    def __init__(self):
        self.ack_time_timeout = 3
        self.ack_time_start = 0
        self.ack_status = False
        self.retry_max = 3
        self.retry_current = 0
        self.data = None

    def update_transmit_data(self, next_data):
        # Update the classes current data to transmit
        self.data = next_data
    def transmit_data(self):
        # Reset ACK retry counter
        self.retry_current = 0

        # Transmit Data
        print "Transmitting DATA", repr(self.data)

        # Set ACK timeout timer
        self.ack_timeout_reset()

    def transmit_data_retry(self):
        # Increment ACK retry counter
        retry_state = self.retry_counter_increment()
        if retry_state:
            # Transmit Data
            print "RETRY - Transmitting DATA", repr(self.data)

            # Set ACK timeout timer
            self.ack_timeout_reset()
            return True
        else:
            return False

    def retry_counter_increment(self):
        if(self.retry_current < self.retry_max):
            self.retry_current += 1
            return True
        else:
            # Retry MAX
            return False

    def ack_timeout_reset(self):
        self.ack_time_start = time.time()
        self.ack_status = False

    def ack_received(self):
        # Update ACK status
        self.ack_status = True

        # Get the next data packet
        pass

    def ack_check(self):
        if (time.time() - self.ack_time_start) < self.ack_time_timeout:
            return False
        else:
            # Retry transmission
            if self.transmit_data_retry():
                pass
            else:
                print "Failed - Max retries!"
