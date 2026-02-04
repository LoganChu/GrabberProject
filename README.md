# GrabberProject

## Overview

This project leverages **ARTIQ** (Advanced Real-Time Infrastructure for Quantum physics) to improve trapped ion measurement efficiency at the Duke Quantum Center. The primary goal is to reduce measurement times by 30% through faster data transmission speeds via the Camera Link Frame Grabber.

## Project Goals

- **Optimize Data Transmission**: Increase data transmission speeds through the Camera Link Frame Grabber
- **Reduce Measurement Times**: Shorten trapped ion measurement times by ~30%
- **Identify and Localize Ions**: Automatically detect regions of interest (ROIs) where ions are located
- **Visualize Camera Data**: Generate clear visualizations of Camera Link output for measurement and orientation

## Technologies & Libraries

- **ARTIQ**: Advanced Real-Time Infrastructure for Quantum physics control and measurement
- **NumPy**: Numerical computing and array operations
- **Pandas**: Data analysis and manipulation
- **Matplotlib**: Data visualization and plotting
- **OpenCV (cv2)**: Computer vision for image processing and bounding box detection
- **SciPy & scikit-image**: Scientific computing and image processing algorithms
- **Seaborn**: Statistical data visualization
- **tifffile**: TIFF image reading and writing

## Project Structure

```
GrabberProject/
├── ROI.py                    # Main ion region of interest detection module
├── Data/                     # Data files and measurements
│   ├── GrabberData.csv
│   ├── Region.csv
│   └── USBImage.csv
├── Scripts/                  # Processing and utility scripts
│   ├── BoundingBox.py        # Draw bounding boxes around detected regions
│   ├── FlipImage.py          # Image flipping utilities
│   ├── ImageCreation.py      # Convert CSV data to heatmaps and visualizations
│   └── ToTextFile.py         # Convert image data to text format
├── Outputs/                  # Output results and processed images
├── Region/                   # Region data and processed regions
├── IntImageAndor/            # Andor camera image data
├── img-ion-9/                # Ion imaging data set 1
├── img-ion-10/               # Ion imaging data set 2
├── 6-ion-chain/              # 6-ion chain experimental data
└── ColorMaps/                # Color map resources
```

## Key Features

### 1. Region of Interest (ROI) Detection (`ROI.py`)
- Automatically detects ion positions in camera images
- Uses Gaussian blur for image smoothing
- Implements peak detection to locate local maxima (ion positions)
- Generates bounding boxes around detected ions
- Configurable parameters: number of ions, Manhattan distance threshold

### 2. Bounding Box Generation (`BoundingBox.py`)
- Identifies and draws bounding boxes around regions of interest
- Uses binary thresholding to segment regions
- Filters by region size to avoid noise
- Outputs annotated images with detected regions

### 3. Data Visualization (`ImageCreation.py`)
- Converts CSV data to heatmaps for visual analysis
- Generates pixelated images from tabular data
- Supports multiple color mapping schemes
- Useful for analyzing Camera Link data

## Usage

### Detecting Ions in Images
```python
from ROI import roi

# Detect ions in a TIFF image
roi(image="path/to/image.tif", ion_number=6, Manhattan_distance=5)
```

### Drawing Bounding Boxes
```python
from Scripts.BoundingBox import draw_bb

# Generate bounding box visualization
draw_bb("./Region/GrabberRegionGray.png")
```

### Creating Heatmap Visualizations
```python
from Scripts.ImageCreation import csv_to_heatmap, csv_to_pixelated_image

# Convert CSV to heatmap
csv_to_heatmap("Data/Region.csv", "Outputs/heatmap.png")

# Convert CSV to pixelated image
csv_to_pixelated_image("Data/Region.csv", "Outputs/pixelated.png")
```

## Data Files

- **GrabberData.csv**: Main sensor/measurement data
- **Region.csv**: Region-specific measurements
- **USBImage.csv**: USB camera image data
- **Metadata files**: Display settings and imaging parameters for each ion set

## Output

Processed images and analysis results are saved to the `Outputs/` directory, including:
- Detected ion positions and bounding boxes
- Heatmap visualizations
- Processed camera images

