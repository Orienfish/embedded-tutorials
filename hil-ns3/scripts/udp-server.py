#!/usr/bin/python3
import socket
import time
import subprocess
import numpy as np
from lr import LinearRegression
from ina219_pi_seelab import ina219_pi_seelab

UDP_IP = "10.1.1.5"
UDP_PORT = 4000

sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

pm = ina219_pi_seelab()
temp_cmd = "bash ./get_temp.sh"

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    (host, port) = addr
    print("received message:", data, host, port)

    # get the message type
    info = data.strip().split(',')
    if info[0] == "data":
        try:
            # run linear regression 
            input_size = int(info[1]) # Bytes
            output_size = int(info[2]) # Bytes
            # times = int(info[3]) # Run how many times

            st_time = time.time()
            lr = LinearRegression(input_size >> 2, output_size >> 2)
            a = np.random.normal(size=(1, input_size >> 2))
            # for i in range(times):
            lr.run(a)
            run_time = time.time() - st_time
            run_time = round(run_time, 12) # total is 14 Bytes
            # send back execution time and dummy data
            dummy_data = 'x' * output_size # Bytes
            msg = ",".join(["data", str(run_time), dummy_data])
            sock.sendto(msg, (host, UDP_PORT))
            print("runtime: ", run_time)
        except Exception as e:
            print(e)
    elif info[0] == "power":
        pwr = pm.read_power()
        pwr = pwr / 1000.0 # convert from mW to W
        msg = ",".join(["power", str(pwr)])
        sock.sendto(msg, (host, UDP_PORT))
        print("power(W): ", pwr)
    elif info[0] == "temp":
        proc = subprocess.Popen(temp_cmd.split(), 
            stdout=subprocess.PIPE)
        res = proc.stdout.read().decode('utf-8').strip()
        msg = ",".join(["temp", str(res)])
        sock.sendto(msg, (host, UDP_PORT))
        print("temp: ", str(res))

