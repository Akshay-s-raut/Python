import time
import ntplib

#add the difference to time.time()
def get_difference():
    c = ntplib.NTPClient()
    response = c.request('in.pool.ntp.org', version=3)
    # print((response.recv_time - response.orig_time + response.tx_time - response.dest_time)/2,(response.offset + response.dest_time) - time.time())
    # return (response.offset + response.dest_time) - time.time()
    return (response.recv_time - response.orig_time + response.tx_time - response.dest_time)/2
    # return response.tx_time,(response.recv_time - response.orig_time + response.tx_time - response.dest_time)/2

# x = get_difference()
# print(x)
