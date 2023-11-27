import numpy as np
import sounddevice as sd
import tkinter as tk
from scipy.signal import butter, lfilter

# Generating 10 frequency bands between 20 Hz and 20,000 Hz
low_freq = 20
high_freq = 20000
num_bands = 10
log_space = np.logspace(np.log10(low_freq), np.log10(high_freq), num_bands + 1)
frequency_bands = [(int(log_space[i]), int(log_space[i + 1])) for i in range(num_bands)]

# Function to create a bandpass filter
def bandpass_filter(data, lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    y = lfilter(b, a, data)
    return y


def callback(outdata, frames, time, status):
    if status:
        print(status)
    white_noise = np.random.randn(frames)
    filtered_noise = np.zeros_like(white_noise)
    for (low, high), volume in zip(frequency_bands, band_volumes.values()):
        band_noise = bandpass_filter(white_noise, low, high, fs=44100, order=3)
        filtered_noise += band_noise * volume
    outdata[:] = np.tile(filtered_noise.reshape(-1, 1), (1, 8))


# Global variables for band volumes and file to store slider values
band_volumes = {'{}-{} Hz'.format(low, high): 1.0 for low, high in frequency_bands}
slider_values_file = 'slider_values.txt'

# Function to save slider values to a file
def save_slider_values():
    with open(slider_values_file, 'w') as file:
        for band, value in band_volumes.items():
            file.write(f'{band}:{value}\n')

def load_slider_values():
    try:
        with open(slider_values_file, 'r') as file:
            for line in file:
                band, value = line.strip().split(':')
                # Format the band name to match the generated bands
                formatted_band = f"{band} Hz"
                if formatted_band in band_volumes:  # Update only if band is in the current configuration
                    band_volumes[formatted_band] = float(value)
    except FileNotFoundError:
        pass  # File not found, will use default values


# UI slider change handler
def on_slider_change(band, value):
    global band_volumes
    band_volumes[band] = float(value)

# Building the UI with tkinter
def build_ui():
    load_slider_values()  # Load saved values
    window = tk.Tk()
    window.protocol("WM_DELETE_WINDOW", lambda: [save_slider_values(), window.destroy()])  # Save on close
    for band in band_volumes.keys():
        frame = tk.Frame(window)
        frame.pack(side=tk.LEFT)
        tk.Label(frame, text=band).pack()
        slider = tk.Scale(frame, from_=2, to=0, resolution=0.01, orient=tk.VERTICAL, length=300, command=lambda value, b=band: on_slider_change(b, value))
        slider.set(band_volumes[band])  # Set to saved value
        slider.pack()
    return window


# Main function to run the UI and audio stream
def main():
    global stream
    with stream:
        window = build_ui()
        window.mainloop()

# Initialize the audio stream
device_index = 7  # Adjust as needed
stream = sd.OutputStream(callback=callback, channels=8, device=device_index)

# Run the main function
if __name__ == '__main__':
    main()
