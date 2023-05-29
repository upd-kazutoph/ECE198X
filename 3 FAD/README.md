# 3 EVALUATION: FAD (UBUNTU X)
- Use **Python 3.7** (you may switch the Python version on the Ubuntu 18 setup on #1 or VAE-GAN)
- No need to use virtualenv or conda.
- Reference Code is also from [VAE-GAN](https://github.com/RussellSB/tt-vae-gan/tree/e530888af4841cba78a77cda08f8b9dd33dfbd0b/fad/frechet_audio_distance)
- See notes below for full details.

## STEP 1: Install dependencies and VGGISH Checkpoint
```bash
python -m pip install -r requirements_fad.txt
```
Download the [VGGish checkpoint file](https://storage.googleapis.com/audioset/vggish_model.ckpt) and save it in the DATA folder.

## STEP 2: MAKE A LIST OF FILE PATHs PER FOLDER
```bash
ls --color=never dataset_ref/audio/*  > dataset_ref/reference.cvs
ls --color=never dataset_raw/audio/*  > dataset_raw/bumbongdataset.CVS
ls --color=never dataset_CQT/audio/*  > dataset_CQT/gansynth_cqt.CVS
ls --color=never dataset_MEL/audio/*  > dataset_MEL/gansynth_mel.CVS
```
dataset_raw is the Bumbong dataset. dataset_ref is a custom dataset with "clean" audio files. This project used files from **MagnaTagATune** dataset which was used [FAD by Kilgour et al.](https://arxiv.org/abs/1812.08466). Large dataset requires a bigger RAM so make sure to trim down the reference dataset to the highest possible based on your PC setup specifications.

## STEP 3: CREATE STAT EMBEDDINGS!
```bash
mkdir -p stats_raw
python create_embeddings_main.py --input_files dataset_ref/reference.cvs --stats stats_ref/reference_stats
python create_embeddings_main.py --input_files dataset_raw/bumbongdataset.cvs --stats stats_input/raw_audio
python create_embeddings_main.py --input_files dataset_CQT/gansynth_cqt.CVS --stats stats_input/gansynth_cqt
python create_embeddings_main.py --input_files dataset_MEL/gansynth_mel.CVS --stats stats_input/gansynth_mel
```

## STEP 3: COMPUTE THE FRECHET AUDIO DISTANCE (FAD)
```bash
python compute_fad.py --background_stats stats_ref/reference_stats --test_stats stats_input/raw_audio
python compute_fad.py --background_stats stats/background_stats --test_stats stats/test1_stats
python compute_fad.py --background_stats stats/background_stats --test_stats stats_input/gansynth_cqt
python compute_fad.py --background_stats stats/background_stats --test_stats stats_input/gansynth_mel
```

NOTE: 
- The python file headers were modified to use the code locally and not from any libraries. 
- Make sure to download the vggish checkpoint file and store it in data folder.
- If your reference dataset is on MP3 format, you may use the **mp3towav_conv.py** by editing the PATH variable. This will convert all the mp3 files to WAV files and store it in the same folder. Make sure to segregate files afterwards.