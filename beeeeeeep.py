import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal import spectrogram

output_name = "C"

def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            try:
                # Convert each line to an integer
                data.append(int(line.strip()))
            except ValueError:
                continue  # Skip blank lines or lines that can't be converted
    return np.array(data)

def plot_spectrogram(data, sampling_rate):
    # Compute the spectrogram
    f, t, Sxx = spectrogram(data, fs=sampling_rate)
    
    low_pass_threshold_hz = 800
    low_pass_threshold = low_pass_threshold_hz // 35
    f, Sxx = f[:low_pass_threshold], Sxx[:low_pass_threshold]

    # breakpoint()

    # Plot the spectrogram
    plt.figure(figsize=(10, 6))
    plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='gouraud')
    plt.title('Spectrogram')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [s]')
    plt.colorbar(label='dB')
    plt.savefig(f"{output_name}_spectrogram.png")

    return t, Sxx

def plot_dft(data, sampling_rate):
    # Perform Discrete Fourier Transform (DFT)
    N = len(data)
    dft_data = fft(data)
    freqs = np.fft.fftfreq(N, 1/sampling_rate)

    # Only keep the positive frequencies
    positive_freqs = freqs[1:N // 2]
    positive_magnitude = np.abs(dft_data[1:N // 2])

    # Plot DFT result
    plt.figure(figsize=(10, 6))
    plt.plot(positive_freqs, positive_magnitude)
    plt.title('DFT Frequency Magnitude Response')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Amplitude')
    plt.yticks(np.arange(0, 2e6, 0.5e6))
    plt.grid()
    plt.savefig(f"{output_name}_dft.png")



def plot_cumulative_amplitude(t, Sxx):
    # Calculate the cumulative amplitude by summing across frequencies
    cumulative_amplitude = np.sum(Sxx, axis=0)
    
    # Plot the cumulative amplitude
    plt.figure(figsize=(10, 6))
    plt.plot(t, cumulative_amplitude)
    plt.title('Cumulative Amplitude Over Time')
    plt.xlabel('Time [s]')
    plt.ylabel('Cumulative Amplitude')
    plt.grid(True)
    plt.savefig(f"{output_name}_cumulative_amplitude.png")

# Main function to run the analysis
if __name__ == "__main__":
    # Read the data from the file
    data = read_data(f'{output_name}.txt')

    # Assuming a sampling rate (adjust as needed)
    sampling_rate = 8900  # In Hz (or sample rate per second)

    # Plot the DFT
    plot_dft(data, sampling_rate)

    # Plot the Spectrogram and get time and Sxx
    t, Sxx = plot_spectrogram(data, sampling_rate)

    # Plot the Cumulative Amplitude
    plot_cumulative_amplitude(t, Sxx)