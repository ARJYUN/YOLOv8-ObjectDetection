# YOLOv8 Object Detection

A simple Python script to perform object detection using YOLOv8 on images.

## Features

- Detect objects in images using YOLOv8
- Works with both local images and image URLs
- Displays and saves detection results
- Lightweight and easy to use

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ARJYUN/YOLOv8-ObjectDetection.git
   cd YOLOv8-ObjectDetection
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the detection on the default sample image:
```bash
python detect.py
```

To use your own image, modify the `detect.py` file and change the image URL or path:

```python
# Change this line in detect.py
results = model('path/to/your/image.jpg')
```

## Output

The script will:
1. Download the YOLOv8 model (if not already downloaded)
2. Process the input image
3. Save the results as `results.jpg`
4. Display the detection results in a window (press any key to close)

## Requirements

- Python 3.7+
- ultralytics
- opencv-python

## Results

![Sample Detection](https://ultralytics.com/images/bus.jpg)
*Sample input image*

![Detection Results](results.jpg)
*Detection results with bounding boxes*
