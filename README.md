# Valorant-Object-Detection
Object detection for Valorant with YOLO models

# Table of Contents
1. [Installation & Requirements](#installation--requirements)
   - [Running with TensorRT](#running-with-tensorrt)
   - [Clone the Repo](#clone-the-repo)
2. [Application Setup](#application)
   - [Brave-Portable](#brave-portable)
   - [Chrome or Edge](#chrome-or-edge)
   - [Model Downloads](#model-downloads)
   - [Using the PyTorch Models](#using-the-pytorch-models)
3. [Usage](#usage)
   - [Using the Application](#using-the-application)
   - [Supported File Extensions](#supported-file-extensions)
     - [Image Extensions](#image-extensions)
     - [Video Extensions](#video-extensions)
5. [Settings](#settings)
6. [Training, Tests, and Comparison](#training-tests-and-comparison)

Built using [YOLOv8n and YOLOv8x](https://github.com/ultralytics/ultralytics), simply choose a file in the application window and it will return the image or video with it's predictions shown.

Snippet from [Inference Test](#training-tests-and-comparison)\
![model-in-action](https://github.com/alexromain/Valorant-Object-Detection/assets/73396089/bca829fc-9521-432e-9117-293db21e5f90)

# Installation & Requirements

> [!NOTE]
> Python 3.8 was used for this project.\
> An Nvidia RTX 3070 GPU was used for training.

## Running with [TensorRT](https://developer.nvidia.com/tensorrt)

**TensorRT models can be up to *6x Faster* than PyTorch models on Nvidia GPUs.**

You'll need to have [CUDA](https://developer.nvidia.com/cuda-toolkit) and [cuDNN](https://developer.nvidia.com/cudnn) installed.\
See [CUDA docs](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html) and [cuDNN docs](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html) for help.

**If you are not able to use TensorRT, you can [use the torch models](#using-the-pytorch-models) with a CPU.**

> [!IMPORTANT]
> Everything must be compatible with your Python version and hardware.\
> Check the Nvidia [GPU Compatibility](https://developer.nvidia.com/cuda-gpus) list.\
> **You need to install [PyTorch](https://pytorch.org/get-started/locally/) whether you're using TensorRT or not.**

## Clone the Repo

```bash
git clone https://github.com/alexromain/Valorant-Object-Detection
```
Go to the project directory
```bash 
cd Valorant-Object-Detection
```
Install requirements.txt
```bash
pip install -r requirements.txt
```

After cloning the repository and installing the [requirements](#installation%20&%20requirements) go to the `application/` directory.

# Application

For the application GUI, [Eel](https://github.com/python-eel/Eel) was used with [Brave Portable](https://github.com/portapps/brave-portable), but you can use [Chrome or Edge](#chrome-or-edge).\

## Brave-Portable 

> [!NOTE]
> Alternatively you can just use [Chrome or Edge](#chrome-or-edge)

Install [Brave Portable](https://github.com/portapps/brave-portable) in this directory.
The `application/` folder should look something like this:
```
application/
├── brave/
│   └── brave-portable.exe
├── gui/
├── model/
├── predictions/
├── upload/
├── utils/
├── __init__.py
├── config.py
└── main.py
```

Now navigate to your python `environment\Lib\site-packages\eel\browsers.py`.

Add the following at line 58, just before `elif mode == 'custom':`, it should look like this:
```python
      pass
    elif mode == 'brave':
        for url in start_urls:
            brave_path="brave/brave-portable.exe"
            wbr.register('brave-portable', None, wbr.BackgroundBrowser(brave_path))
            wbr.get('brave-portable').open('--app=' + url)
    elif mode == 'custom':
```

## Chrome or Edge

If using Brave is too much work, you can use chrome or edge to access the GUI.

In [main.py](application/main.py), change:
```python
  if __name__ == '__main__':
      eel.start('main.html', 
                size=(566, 639), 
                mode='brave', #this line to 'chrome' or 'edge'
                cmdline_args=['--app'])
```

## Model Downloads

Due to the filesize of the models, the files are uploaded to google drive.

- [TensorRT models](https://drive.google.com/file/d/1W6MqDa16iCergzbECxWLFKpljVXj98Be/view?usp=drive_link)
- [Torch models](https://drive.google.com/file/d/1K93_K6D4F4GEghfWEQkOaZBcG0p9hRxG/view?usp=drive_link)

Skip this if you are not using TensorRT. [Go here instead](#using-the-pytorch-models)

The TensorRT models need to be placed in the [`application/model/`](application/model) directory.

```
application/
├── model/
    └── bestv8n.engine
    └── bestv8x.engine
    └── bytetrack.yaml
```

If you're interested in the notebooks, the Torch models should be put in the [`Training & Testing/models`](Training%20&%20Testing/models) directory.

## Using the PyTorch Models

If you can't use the TensorRT models, you'll need to change the following lines in [settings.py](application/utils/settings.py)\
On line `29`, `39` and `42`, change the file .extension:

From:
```python
self.model_path = 'model/bestv8n.engine'
```
To:
```python
self.model_path = 'model/bestv8n.pt'
```

Instead of putting the .engine<sup>TensorRT</sup> models here, you'll simply put the `.pt` models.
```
application/model/
├── model/
    └── bestv8n.pt
    └── bestv8x.pt
    └── bytetrack.yaml
```

# Usage

Now to launch the app, type:
```bash
python main.py
```
The GUI should show up!

![Capture](https://github.com/alexromain/Valorant-Object-Detection/assets/73396089/8ee83fbc-2fa0-45b6-9d3a-da40fbdb4146)

#### Using the Application

To give the model an image or video, first check if the image format is [compatible with the model](#supported-file-extensions), YOLO supports a wide range of formats so that shouldn't be an issue.

After that, simply click 'Click Here' to choose a file.

> [!IMPORTANT]
> Files you want the model to take in have to be put in the [`application/upload`](application/upload) folder!\
> For the best results, use **640x640** under [Settings](#settings). These YOLO models were trained on a [dataset](#i-used-this-huggingface-dataset-to-train-the-model) that was 416x416,
but the pre-trained YOLOv8 models are trained on **640x640**, so they perform better at that resolution.

Once the model has completed its process, see the results by clicking `Results Folder`.

## Supported File Extensions

#### Image Extensions:
- BMP (.bmp)
- DNG (.dng)
- JPEG (.jpeg)
- JPG (.jpg)
- MPO (.mpo)
- PNG (.png)
- TIFF (.tif, .tiff)
- WEBP (.webp)
- PFM (.pfm)

#### Video Extensions:
- ASF (.asf)
- AVI (.avi)
- GIF (.gif)
- M4V (.m4v)
- MKV (.mkv)
- MOV (.mov)
- MP4 (.mp4)
- MPEG (.mpeg)
- MPG (.mpg)
- TS (.ts)
- WMV (.wmv)
- WebM (.webm)

## Settings

There are a few settings I've added that you can play around with, by default the (Width,Height) and Frame-rate will use whatever your image or video is set to.

The model will take any resolution thats a multiple of 32, luckily YOLO handles this for us.

- **Width & Height:**\
The suggested Width and Height is **640x640**, this will give you the highest accuracy.\
But you're free to use any resolution, though high resolutions will be computationally expensive.

- **Frame-rate:**\
Adjusting the frame-rate will have a perfomance impact if raised, but it will put your video in slow-motion if lowered.\
I suggest leaving this field Default.

- **Confidence:**\
This is the value you should play around with, depending on the resolution you use the model will have differing results.\
By default it's set at 0.4 (40%), I don't suggest going lower than that. Values range from **(0.01 to 1.0)**.

#### ByteTrack

For Video Inference, the model uses ByteTrack from the [YOLO Repo](https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/trackers/bytetrack.yaml).\
The config I've set can be found [here](application/model/bytetrack.yaml), I haven't adjusted these too much, but feel free to try different values.

# Training, Tests, and Comparison

- **[Model Training can be found here](Training%20&%20Testing/YOLO%20Training.ipynb)**

- **[Inference Tests can be found here](Training%20&%20Testing/Inference%20Testing.ipynb)**

- **[Model comparison can be found here](Model%20Comparison/Model%20Comparison.ipynb)**

### I used this [HuggingFace Dataset](https://huggingface.co/datasets/keremberke/valorant-object-detection) to train the model.
