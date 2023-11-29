# Valorant-Object-Detection
Object detection for Valorant with YOLO models

Built using YOLOv8n and YOLOv8x, simply choose a file in the application window and it will return the image or video with it's predictions drawn.

![test_enemy6520608217](https://github.com/alexromain/Valorant-Object-Detection/assets/73396089/badadeb1-2b93-4589-9d11-3c79d6868c9f)

# Installation & Requirements

## Running with [TensorRT](https://developer.nvidia.com/tensorrt)

You'll need to have [CUDA](https://developer.nvidia.com/cuda-toolkit) and [cuDNN](https://developer.nvidia.com/cudnn) installed, see [CUDA docs](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html) and [cuDNN docs](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html) for help.\
Also confirm that you have a compatible [Nvidia GPU](https://developer.nvidia.com/cuda-gpus).

If you are not able to use TensorRT, you can [use the torch models](#using-the-pytorch-models) with a CPU.

### You need to install [PyTorch](https://pytorch.org/get-started/locally/) whether you're using TensorRT or not.

## Application

For the application, [Eel](https://github.com/python-eel/Eel) was used with [Brave Portable](https://github.com/portapps/brave-portable), but you can use chrome or edge. See [Chrome or Edge](#chrome-or-edge)

## Cloning the repo

Clone the repo
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

# Usage

After cloning the repository and installing the requirements go to the `application/` directory.

## Brave-Portable

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
├── main.py
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

If using Brave is too much work, you can use another web browser such as chrome or edge.

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

The models need to be placed in the [`application/model`](application/model) directory.\
If you're interested in the notebooks, the Torch models should be put in the [`Training & Testing/models`](Training%20&%20Testing/models) directory.

## Using the PyTorch Models

If you can't use the TensorRT models, you'll need to change the following lines in [settings.py](application/utils/settings.py)\
On line `29`, `39` and `42`, change the extension:

From:
```python
self.model_path = 'model/bestv8n.engine'
```
To:
```python
self.model_path = 'model/bestv8n.pt'
```

Now to launch the app, type:
```bash
python main.py
```
The GUI should show up!

## Testing

- [Inference Tests can be found here](Training%20&%20Testing/Inference%20Testing.ipynb).

- [Model comparison can be found here](Model%20Comparison/Model%20Comparison.ipynb)

### I used this [HuggingFace Dataset](https://huggingface.co/datasets/keremberke/valorant-object-detection) to train the model.
