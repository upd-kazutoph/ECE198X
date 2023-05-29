import librosa
from params import *
from utils import amp_to_db, normalize
from scipy.io import wavfile
import matplotlib.pyplot as plt

signal = wavfile.read('../../wavenet_vocoder/egs/gaussian/data/cqt_testpair1_2/eval/prolonged_bass_electronic_000-042-050.wav')

## Audio
sample_rate = 16000
# Number of spectrogram frames in a partial utterance
partials_n_frames = 160     # 1600 ms
# Number of spectrogram frames at inference
inference_n_frames = 80     #  800 ms

## Mel-filterbank
n_fft = 2048
num_mels = 128
num_samples = 128 # input spect shape num_mels * num_samples
hop_length = int(0.0125*sample_rate)                    # 12.5ms - in line with Tacotron 2 paper
win_length = int(0.05*sample_rate)                   # 50ms - same reason as above

orig = librosa.feature.chroma_stft(signal, sample_rate, hop_length, win_length, n_fft)
orig = amp_to_db(orig)
orig = normalize(orig)

fig, ax = plt.subplots(nrows=1, ncols=1, sharey=True)

ax[0].imshow(signal, interpolation="None", aspect='auto')
ax[0].set(title='Input')
ax[0].set_ylabel('CQT')
ax[0].axes.xaxis.set_ticks([])

    
ax[0].invert_yaxis()
plt.tight_layout()
plt.savefig('/testing', format='png')
plt.close()