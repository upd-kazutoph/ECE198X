# 2 GANSYNTH (UBUNTU 20.04.x)
- Follow the instructions for installing Magenta for [GANSynth](https://github.com/magenta/magenta/tree/main/magenta/models/gansynth).
- For simplicity, use the MINICONDA track. See below:

Update Ubuntu & install dependencies
```bash
sudo apt update
sudo apt upgrade
sudo apt install python3-pip
sudo apt-get install build-essential libasound2-dev libjack-dev portaudio19-dev ffmpeg
```

Miniconda install
```bash
curl https://raw.githubusercontent.com/tensorflow/magenta/main/magenta/tools/magenta-install.sh > /tmp/magenta-install.sh
bash /tmp/magenta-install.sh
```

The miniconda install may say that it failed in installation. After that, make sure to add the conda PATH to bashrc first. If successful, you may now use "source activate magenta" command line.

Once you enabled the conda environment, install Magenta thru pip. Make sure to install python3-pip and the other dependencies above.

```bash
pip install magenta
```

Get a copy of the GANSynth subset of NSynth to enable local training. Training using the Google Cloud (gs) will take long. Make sure to download the 25GB+ dataset (this project used version 2.3.3). To download the dataset, use the **download_gansubset.py** and **modify TFDS_DATA_DIR** and make sure to have an uninterrupted and fast internet connection. 

The gansubset folder should have a subdirectory of an empty downloads folder and an nsynth folder with tfrecord files inside.

### Use the following commands for GANSynth below:
TRAINING PART
```bash
gansynth_train --hparams='{"tfds_data_dir":"<path/gansubset>", "train_root_dir": "<insert output path here>"}'
```

GENERATION PART (may use repeatedly on one training part)
```bash
gansynth_generate --ckpt_dir="<path from VAE-GAN output gen files>" --output_dir=OUTPUT_FOLDER--midi_file=five2two.mid
```

GANSynth requires a MIDI file to generate an audio file. You may download a midi file or create your own. five2two.mid is a custom midi file which has C2 to A5 notes only. 