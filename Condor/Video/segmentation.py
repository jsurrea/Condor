import os
import av
import torch
from PIL import Image
from segment_anything import SamAutomaticMaskGenerator, sam_model_registry

def detect_objects_in_video(video_path, output_path):
    """
    """

    # Create the model
    device = "cuda" if torch.cuda.is_available() else "cpu"
    sam = sam_model_registry["vit_h"](checkpoint="sam_vit_h_4b8939.pth")
    sam.to(device=device)
    mask_generator = SamAutomaticMaskGenerator(sam)

    # Open the video file using PyAV
    container = av.open(video_path)

    # Create the output directory
    output_dir = os.path.split(output_path)[0]
    img_dir = os.path.join(output_dir, "IMG")
    os.makedirs(name=img_dir, exist_ok=True)

    # Iterate over each frame in the video
    for i, frame in enumerate(container.decode(video=0)):
        time = frame.time
        frame = frame.to_rgb().to_ndarray()

        # Discard frames with a low variance of pixel values
        # or with temporal proximity to the previous frame
        if i % 100 == 0 and frame.var() > 3000:
            masks = segment_frame(frame, mask_generator)
            masks.save(os.path.join(img_dir, '{i:%08d}.jpg'))

    # Close the video file
    container.close()

def segment_frame(frame, mask_generator):
    """
    
    """

    # Generate the masks from SAM
    masks = mask_generator.generate(frame)

    # Sort the masks by confidence
    confidences = list(map(lambda x:x["predicted_iou"], masks))
    masks = list(map(lambda x:x[0], sorted(zip(masks, confidences), key=lambda x:x[1], reverse=True)))

    # Create PIL from segmentation masks
    masks = show_anns(masks)
    masks = Image.fromarray(masks)

    return masks

def show_anns(anns):
    """
    Creates an image with the segmentation masks
    """
    if len(anns) == 0:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)

    img = np.ones((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1], 4))
    img[:,:,3] = 0
    for ann in sorted_anns:
        m = ann['segmentation']
        color_mask = np.concatenate([np.random.random(3), [0.35]])
        img[m] = color_mask
    
    return img


