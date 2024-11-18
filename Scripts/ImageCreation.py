import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def csv_to_heatmap(csv_file, output_image_file):
    # Load CSV data into a pandas DataFrame
    data = pd.read_csv(csv_file, header = None)
    
    # Create a heatmap using seaborn
    plt.figure(figsize=(8, 8)) #10 In x 8 In
    sns.heatmap(data, cmap="coolwarm", annot=True, fmt=".2f", cbar=False) 

    plt.axis("off")
    # Save the heatmap as an image file
    plt.savefig(output_image_file,bbox_inches="tight", pad_inches=0)
    plt.close()

def csv_to_pixelated_image(csv_file, output_image_file):
    # Load CSV data into a pandas DataFrame
    data = pd.read_csv(csv_file, header=None)  # Use header=None if there's no header row in the CSV

    # Convert DataFrame to a NumPy array for easy plotting
    pixel_data = data.to_numpy()
    
    # Plot the pixel data
    plt.imshow(pixel_data, cmap="tab10", interpolation="none")
    plt.axis("off")  # Turn off axis for a cleaner image

    # Save the pixelated image
    plt.savefig(output_image_file, bbox_inches="tight", pad_inches=0)
    plt.close()

#Example usage
csv_to_pixelated_image("./Data/Region.csv", "GrabberRegionTab10.png")
#csv_to_heatmap("USBImage.csv", "CoolWarmHeatMap.jpg")