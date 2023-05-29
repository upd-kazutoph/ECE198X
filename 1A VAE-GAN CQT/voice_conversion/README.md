# VAE-GAN (VOICE CONVERSION) for CQT Spectrograms
This portion is a modified and revised version of the original README.md file of VAE-GAN. Additional notes are added related to the Bumbong project. Kindly read first the end notes before proceeding.

##  Voice Conversion Using Speech-to-Speech Neuro-Style Transfer
This repo contains the official implementation of the VAE-GAN from the INTERSPEECH 2020 paper [Voice Conversion Using Speech-to-Speech Neuro-Style Transfer](http://www.interspeech2020.org/uploadfile/pdf/Thu-3-4-11.pdf).

## 0. CODE PREPARATION
Use Python 3.8 only. Make sure the latest NVIDIA drivers esp. CUDA is installed in your system.

Install the requirement libraries on pip. (DO ONCE ONLY)
```bash
pip install -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html
```

## 1. Data Preparation
This structure requires at least **2 speakers** to work. As the Bumbong doesn't have any different speakers, it was simply distributed into 2 separate folders. Using 1 speaker will fail the setup. Make sure to use WAV files only.

Dataset file structure:

```bash
/path/to/database
├── spkr_1
│   ├── sample.wav
├── spkr_2
│   ├── sample.wav
│   ...
└── spkr_N
    ├── sample.wav
    ...
# The directory under each speaker cannot be nested.
```


## 2. Data Preprocessing
The prepared dataset is organised into a train/eval/test split, the audio is preprocessed and spectrograms are computed. 

```bash
python preprocess.py --dataset [path/to/dataset] --test-size [float] --eval-size [float]
```

Modified version (no eval size needed):
```bash
python3 preprocess.py --dataset ../data/BumbongCQT --n_spkrs 2
```

## 3. Training
The VAE-GAN model uses the spectrograms to learn style transfer between two speakers.

```bash
python train.py --model_name [name of the model] --dataset [path/to/dataset]
```
Modified version:
```bash
python3 train.py --model_name BumbongCQT --dataset ../data/BumbongCQT --n_spkrs 2 --n_epochs 51
```
Note: The epoch count ends at 49 when set to 50 so we set it to 51 instead. The duration per epoch on our setup takes about 1-8 minutes. Limiting the CPU cores/thread is recommended when using Python for Windows. Take note that the preprocess.py requires Ubuntu functions to work but train.py and inference.py can work on both windows and Ubuntu.

## 4. Inference
The trained VAE-GAN is used for inference on a specified audio file. The script then uses **Griffin-Lim** to reconstruct/inverse audio from the generated spectrogram. 

```bash
python inference.py --model_name [name of the model] --epoch [epoch number] --trg_id [id of target generator] --wav [path/to/source_audio.wav]
```

Windows Version of command (Powershell):
```bash
python3 inference.py --model_name BumbongCQTX2 --epoch 50 --trg_id 2 --wavdir "C:/DSP19XC/ProlongedData" --img_height 100
```

Ubuntu Version of command (bash):
```bash
python3 inference.py --model_name BumbongCQTX2 --epoch 50 --trg_id 2 --wavdir /mnt/c/DSP19XC/ProlongedData --img_height 100
```

## 5. READY FOR GANSynth
Go to the INFERENCE.PY Output folder and look for the GEN folder. Copy the output contents and prepare it for GANSynth.


Note: 
- The img_height of 100 works on our dataset but it may vary on your dataset.
- Using Griffin Lim on CQT converts back the CQT spectrogram to a WAV file but the audio duration usually decrease. Using a longer duration wav file is recommended. Our dataset uses 4 sec audio as mirrored in NSynth setting for GANSynth. If the audio file is shorter, you may repeat the audio to make it longer.
- Some audio files on our dataset was removed as the train.py part rejects audio files with "bad" CQT output. CQT processing is recommended to be done first before MEL for consistency purposes.
- For more information, kindly check out the [VAE-GAN repository](https://github.com/RussellSB/voice_conversion/tree/2e9ed3facafcd12d51579bfbee6a5991843b8891)!