import os
import av
import cv2
import torch
import easyocr
import numpy as np
import matplotlib.pyplot as plt
from segment_anything import SamAutomaticMaskGenerator, sam_model_registry


def detect_objects_in_video(video_path, output_path):
    """
    Detects objects in the given video and saves the results to the given output path
    """

    # Create the model
    device = "cuda" if torch.cuda.is_available() else "cpu"
    sam = sam_model_registry["vit_h"](checkpoint="sam_vit_h_4b8939.pth")
    sam.to(device=device)
    mask_generator = SamAutomaticMaskGenerator(sam)
    reader = easyocr.Reader(["es"], gpu=torch.cuda.is_available())

    # Open the video file using PyAV
    container = av.open(video_path)

    # Create the output directory
    output_dir = os.path.split(output_path)[0]
    img_dir = os.path.join(output_dir, "IMG")
    os.makedirs(name=img_dir, exist_ok=True)

    # Create the csv file
    with open(output_path, "w") as f:
        f.write("id,object_type,time,coordinates_text\n")

    # Iterate over each frame in the video
    for i, frame in enumerate(container.decode(video=0)):
        time = frame.time
        frame = frame.to_rgb().to_ndarray()

        # Discard frames with a low variance of pixel values
        # or with temporal proximity to the previous frame
        if i % 100 == 0 and frame.var() > 3000:
            segment_frame(frame, mask_generator, os.path.join(img_dir, f'{i:08d}.png'))
            seconds = int(int(time) % 60)
            minutes = int((time // 60) % 60)
            hours = int(time // 3600)
            coordinates = get_coordinates(reader, frame)
            time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            
            # Append to the csv file
            with open(output_path, "a") as f:
                f.write(f"{i},object,{time},\"{coordinates}\"\n")

    # Close the video file
    container.close()

    # Free memory
    del sam
    del mask_generator
    del reader

def segment_frame(frame, mask_generator, savepath, top_n=15):
    """
    Performs inference on the given frame and returns the segmentation masks
    """

    # Generate the masks from SAM
    masks = mask_generator.generate(frame)

    # Sort the masks by confidence
    confidences = list(map(lambda x:x["predicted_iou"], masks))
    masks = list(map(lambda x:x[0], sorted(zip(masks, confidences), key=lambda x:x[1], reverse=True)))

    # Save results
    show_anns(frame, masks[:top_n], savepath)

def show_anns(frame, anns, savepath):
    """
    Creates an image with the given annotations and saves it to the given path
    """

    plt.figure(figsize=(20,20))
    plt.imshow(frame)
    
    if len(anns) == 0:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
    ax = plt.gca()
    ax.set_autoscale_on(False)

    img = np.ones((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1], 4))
    img[:,:,3] = 0
    for ann in sorted_anns:
        m = ann['segmentation']
        color_mask = np.concatenate([np.random.random(3), [0.35]])
        img[m] = color_mask
        
    ax.imshow(img)
    plt.axis('off')
    plt.savefig(savepath, bbox_inches='tight') 

def get_coordinates(reader, frame):
    """
    Returns the coordinates of the given frame
    """
    result = reader.readtext(frame, paragraph=False)
    text = " ".join(map(str, result))

