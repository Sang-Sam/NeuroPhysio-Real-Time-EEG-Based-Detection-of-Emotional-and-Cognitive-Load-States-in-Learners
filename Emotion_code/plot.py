import mne
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# EEG channels
eeg_channels = ['Fp1', 'Fp2', 'F7', 'F3', 'Fz', 'F4', 'F8', 'T7', 'C3', 
                'Cz', 'C4', 'T8', 'P7', 'P3', 'Pz', 'P4', 'P8', 'O1', 'O2']

# Bandpass filter function
def butter_bandpass_filter(data, lowcut=0.5, highcut=50, fs=256, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, data, axis=1)

# Plot all conditions in one single figure
def plot_all_topomaps(data, raw_info, condition_timepoints):
    n_conditions = len(condition_timepoints)
    n_timepoints = len(next(iter(condition_timepoints.values())))  # Assumes all conditions have same # of timepoints
    
    fig, axs = plt.subplots(n_conditions, n_timepoints, figsize=(4 * n_timepoints, 4 * n_conditions))

    if n_conditions == 1:
        axs = [axs]  # Ensure iterable if only one condition
    if n_timepoints == 1:
        axs = [[ax] for ax in axs]  # Ensure 2D list if only one timepoint

    for row_idx, (condition, timepoints) in enumerate(condition_timepoints.items()):
        for col_idx, timepoint in enumerate(timepoints):
            time_sample = int(timepoint * raw_info['sfreq'])
            data_at_time = data[:, time_sample]

            ax = axs[row_idx][col_idx]
            mne.viz.plot_topomap(data_at_time, raw_info, axes=ax, show=False, cmap='RdBu_r')
            ax.set_title(f'{condition}', fontsize=10)

    plt.tight_layout()
    plt.show()

# ------------------------- 
# MAIN FUNCTION FOR TESTING
# -------------------------
def process_and_plot_topomap(edf_path):
    fs = 256  # sampling frequency
    raw = mne.io.read_raw_edf(edf_path, preload=True)
    raw.pick_channels(eeg_channels)

    # Assign montage if not already present (using 10-20 system)
    if raw.info.get('ch_names') == eeg_channels:
        montage = mne.channels.make_standard_montage('standard_1020')
        raw.set_montage(montage)

    raw.set_eeg_reference('average', projection=True)
    data_before = raw.get_data() * 1e6  # Convert to µV
    data_after = butter_bandpass_filter(data_before, lowcut=0.5, highcut=50, fs=fs)
    raw.apply_proj()

    # Timepoints per condition
    condition_timepoints = {
        "Relax": [805.0, 806.0, 807.0, 808.0],
        "T1 Learning": [980.0, 981.0, 982.0, 983.0],
        "T2 Learning": [1062.0, 1063.0, 1064.0, 1065.0],
        "T3 Learning": [1520.0, 1521.0, 1522.0, 1523.0],
        "Post test": [2190.0, 2191.0, 2192.0, 2193.0],
    }

    plot_all_topomaps(data_after, raw.info, condition_timepoints)

# Run the function
edf_path = "../FYP/EDF_Files/Prem_Ranjan.edf"
process_and_plot_topomap(edf_path)
