# ECE198X: GANSynth-based Bumbong Bamboo Instrument Synthesis as SoundFont

THESIS Topic: GANSynth-based Bumbong Bamboo Instrument Synthesis as SoundFont
Solo Thesis Topic by Ryle Emmanuel Raagas (DSP)
Advisers: Crisron Lucas, Carl Tolentino, Jose Marie Mendoza

## METHODOLOGY
1. Audio Data Collection
2. Data Prepocessing (Spectrograms and VAE-GAN)
3. GANSynth Audio Synthesis
4. Evaluations (FAD, 2IFC, etc).

## Prerequisites and other requirements
- Windows 10/11 version 22H2 and later
- CPU with AVX2 (e.g. Intel Core or AMD Ryzen series)
- GPU - NVIDIA Graphics Card (Supports CUDA 11.x and later)
- WSL Install of Ubuntu 18.x (VAE-GAN) and Ubuntu 20.x (Magenta/GANSynth)
- Others: Secondary Storage with NTFS format only for FAD (has issues on exFAT)

## GENERAL INSTALLATION
- Enable WSL feature of Windows 10/11 via https://learn.microsoft.com/en-us/windows/wsl/install. Make sure Virtualization is enabled on BIOS.
- Install Ubuntu 18.04.x and Ubuntu 20.04.x WSL using Microsoft Store
- Make sure to update NVIDIA Drivers to latest version.
- INSTALL [CUDA](https://docs.nvidia.com/cuda/wsl-user-guide/index.html) and [CUDNN](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html) on both Ubuntu WSLs.

## 1 PREPROCESS VAE-GAN (UBUNTU 18.04.x)
- Use Python 3.8 only. Different version may cause install errors.
- Uses only the voice_conversion part of the VAE-GAN repository (split into CQT and MEL)
- See respective folders (VAE-GAN CQT and VAE-GAN MEL for instructions)
- VAE-GAN is originally made to convert/inverse MEL.
- Make sure to update Ubuntu first!
```bash
sudo apt update
sudo apt upgrade
sudo apt install python3-pip
sudo apt install ffmpeg
```
Note: FFMPEG is required on FAD which is also used on VAE-GAN.

## 2 GANSYNTH (UBUNTU 20.04.x)
- Follow the instructions for installing Magenta for [GANSynth](https://github.com/magenta/magenta/tree/main/magenta/models/gansynth).
- For simplicity, use the MINICONDA track and see the 2 GANSynth Folder. See below:

**IMPORTANT!** Update Ubuntu & install dependencies
```bash
sudo apt update
sudo apt upgrade
sudo apt install python3-pip
sudo apt-get install build-essential libasound2-dev libjack-dev portaudio19-dev ffmpeg
```

## 3 EVALUATION: FAD (UBUNTU 18.04.x)
- Use **Python 3.7** (you may switch the Python version on the Ubuntu 18 setup on #1)
- No need to use virtualenv or conda.
- Reference Code is also from [VAE-GAN](https://github.com/RussellSB/tt-vae-gan/tree/e530888af4841cba78a77cda08f8b9dd33dfbd0b/fad/frechet_audio_distance)

## FINAL PRODUCT (SoundFont)
- TO BE UPDATED