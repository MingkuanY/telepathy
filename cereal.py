import serial
import time
import datetime
from scipy.fft import fft
from scipy.signal import spectrogram
import numpy as np
import matplotlib.pyplot as plt

second = 8900

def plot_spectrogram(data, sampling_rate):
    data = np.array(data)
    print(len(data))
    # Compute the spectrogram
    f, t, Sxx = spectrogram(data, fs=sampling_rate)
    
    low_pass_threshold_hz = 800
    low_pass_threshold = low_pass_threshold_hz // 35
    f, Sxx = f[1:low_pass_threshold], Sxx[1:low_pass_threshold]

    return Sxx

def plot_cumulative_amplitude(Sxx):
    # Calculate the cumulative amplitude by summing across frequencies
    cumulative_amplitude = np.sum(Sxx, axis=0)
    binary = np.where(cumulative_amplitude > 7000, cumulative_amplitude, 0)

        # Plot the cumulative amplitude
    # plt.figure(figsize=(10, 6))
    # plt.plot(cumulative_amplitude)
    # plt.title('Cumulative Amplitude Over Time')
    # plt.xlabel('Time [s]')
    # plt.ylabel('Cumulative Amplitude')
    # plt.grid(True)
    # plt.savefig(f"cumulative_amplitude_thing.png")


    return binary

def find_clustered_ones(binary_array):
    # Find the difference between consecutive elements
    diff = np.diff(binary_array)
    
    # Identify where there is a transition from 0 to 1 (start of a cluster)
    clustered_indices = np.where(diff == 1)[0] + 1  # Add 1 to get the actual index after np.diff
    # If the array starts with 1, include the first index (0)
    if binary_array[0] == 1:
        clustered_indices = np.insert(clustered_indices, 0, 0)
    
    print(clustered_indices)
    return [(e,binary_array[e]) for e in clustered_indices]
    #return clustered_indices

def morse_like_encoding(indices, dash_threshold=4400, new_char_threshold=8900*2):
    morse_code = []
    current_char = []

    for i in range(len(indices) - 1):
        # Get the difference between current and next index
        diff = indices[i + 1] - indices[i]

        # Check if the difference falls within the dash threshold
        if diff <= dash_threshold:
            if not current_char or current_char[-1] != '-':
                current_char.append('-')  # Add a dash if previous symbol was not a dash
                i+=1
        else:
            if not current_char or current_char[-1] != '.':
                current_char.append('.')  # Add a dot if previous symbol was not a dot
        
        # Check if the difference exceeds the new character threshold
        if diff > new_char_threshold:
            morse_code.append(''.join(current_char))  # Append current character to morse code
            current_char = []  # Start a new character

    # Append the final character to the morse code if there's anything left
    if current_char:
        morse_code.append(''.join(current_char))

    return morse_code


# Configure the serial port
ser = serial.Serial('/dev/cu.usbserial-0001', 500000, timeout=1)  # Added timeout
ser.reset_input_buffer()  # Clear any existing buffer

# Open a file to write the data
filename = f"serial_data_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
data_list = []

with open(filename, 'wb') as file:  # Changed to binary mode
    start_time = time.time()
    
    counter = 0
    #while time.time() - start_time < 6:  # Run for 10 seconds
    while True:
        # Read all available bytes
        data = ser.read(ser.in_waiting or 1)
        
        if data:
            #timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3].encode()
            #file.write(data + b"\n")
            #print(f"{timestamp.decode()}: {data}")  # Optional: print to console
            for i in data.decode("utf-8").split("\n"):
                if i.strip():
                    data_list.append(int(i.strip()))
                    counter+=1
                    if len(data_list) > 89000 == 0:
                        del data_list[0]
        
        if counter > 8900:
            counter = 0
            morse_ouput = morse_like_encoding(find_clustered_ones(plot_cumulative_amplitude(plot_spectrogram(data_list, 8900))),
                                dash_threshold=8900/2,new_char_threshold=8900*2)
            print(morse_ouput)


    ser.close()

print(f"Data collection complete. Saved to {filename}")