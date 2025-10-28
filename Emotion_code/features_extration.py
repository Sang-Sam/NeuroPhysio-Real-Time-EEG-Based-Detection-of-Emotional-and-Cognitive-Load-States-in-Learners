import numpy as np
import pandas as pd
from scipy.stats import kurtosis, skew
from scipy.signal import welch
import pywt
import antropy as ant
from mne_features.univariate import compute_hjorth_mobility, compute_hjorth_complexity

# EEG frequency bands
bands = {
    "Delta": (0.5, 4),
    "Theta": (4, 8),
    "Alpha": (8, 12),
    "Beta": (12, 30),
    "Gamma": (30, 50),
}

# Band power calculation
def bandpower(data, sf, band):
    low, high = band
    freqs, psd = welch(data, sf, nperseg=sf*2)
    band_power = np.trapz(psd[(freqs >= low) & (freqs <= high)], dx=np.diff(freqs).mean())
    return band_power / np.trapz(psd, dx=np.diff(freqs).mean())

# Wavelet energy
def wavelet_energy(data, wavelet='db4'):
    coeffs = pywt.wavedec(data, wavelet, level=4)
    energy = [np.sum(np.abs(c)**2) for c in coeffs]
    return energy

# Main feature extractor for one segment
def extract_features(segment, fs=256, num_channels=19):
    segment = segment.reshape(num_channels, -1)
    features = {}

    for ch in range(segment.shape[0]):
        data = np.array(segment[ch], dtype=np.float64)

        # Hjorth
        features[f'Ch{ch}_Hjorth_Mobility'] = compute_hjorth_mobility(data)
        features[f'Ch{ch}_Hjorth_Complexity'] = compute_hjorth_complexity(data)

        # Stats
        features[f'Ch{ch}_Mean'] = np.mean(data)
        features[f'Ch{ch}_Std'] = np.std(data)
        features[f'Ch{ch}_Kurtosis'] = kurtosis(data)
        features[f'Ch{ch}_Skewness'] = skew(data)

        # Differences
        first_diff = np.diff(data)
        second_diff = np.diff(first_diff)
        features[f'Ch{ch}_First_Diff_Mean'] = np.mean(first_diff)
        features[f'Ch{ch}_Second_Diff_Mean'] = np.mean(second_diff)

        # Power
        freqs, psd = welch(data, fs, nperseg=fs*2)
        max_power_idx = np.argmax(psd)
        features[f'Ch{ch}_Max_Power'] = psd[max_power_idx]
        features[f'Ch{ch}_Max_Power_Freq'] = freqs[max_power_idx]

        # Band Power
        for band, range_ in bands.items():
            features[f'Ch{ch}_RBP_{band}'] = bandpower(data, fs, range_)

        # Fractal Dimensions
        features[f'Ch{ch}_Higuchi_FD'] = ant.higuchi_fd(data)
        features[f'Ch{ch}_Petrosian_FD'] = ant.petrosian_fd(data)

        # Wavelet Energy
        wavelet_feats = wavelet_energy(data)
        for i, val in enumerate(wavelet_feats):
            features[f'Ch{ch}_Wavelet_Energy_{i}'] = val

    return features

# Function to process a single preprocessed CSV file
def process_segments(input_csv, output_csv, num_channels=19):
    df = pd.read_csv(input_csv)
    features_list = []

    for i, row in df.iterrows():
        segment = row.values.astype(np.float64)
        features = extract_features(segment, num_channels=num_channels)
        features_list.append(features)

    features_df = pd.DataFrame(features_list)
    features_df.to_csv(output_csv, index=False)
    print(f"✅ Extracted features saved to: {output_csv}")

# Example run
process_segments("processed_segments.csv", "features.csv")
