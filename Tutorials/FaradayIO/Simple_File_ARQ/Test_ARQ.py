import arq
import time

tx_arq_object = arq.ArqTransmitter()

data = "- This is a test -"

tx_arq_object.update_transmit_data(data)

tx_arq_object.transmit_data()

while(True):
    tx_arq_object.ack_check()
    print tx_arq_object.retry_current, tx_arq_object.retry_max
    time.sleep(0.25)