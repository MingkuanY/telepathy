import serial
import time
import datetime

# Configure the serial port
ser = serial.Serial('/dev/cu.usbserial-0001', 500000, timeout=1)  # Added timeout
ser.reset_input_buffer()  # Clear any existing buffer

# Open a file to write the data
filename = f"serial_data_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
with open(filename, 'wb') as file:  # Changed to binary mode
    start_time = time.time()
    
    while time.time() - start_time < 6:  # Run for 10 seconds
        # Read all available bytes
        data = ser.read(ser.in_waiting or 1)
        
        if data:
            #timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3].encode()
            file.write(data + b"\n")
            #print(f"{timestamp.decode()}: {data}")  # Optional: print to console

    ser.close()

print(f"Data collection complete. Saved to {filename}")