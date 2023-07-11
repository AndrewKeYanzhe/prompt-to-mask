from transformers import CLIPSegProcessor, CLIPSegForImageSegmentation
# import gradio as gr
from PIL import Image
import torch
import matplotlib.pyplot as plt
import cv2

from matplotlib import image as mpimg
import numpy as np


processor = CLIPSegProcessor.from_pretrained("CIDAS/clipseg-rd64-refined")
model = CLIPSegForImageSegmentation.from_pretrained("CIDAS/clipseg-rd64-refined")

def process_image(image, prompt):
  
  inputs = processor(text=prompt, images=image, padding="max_length", return_tensors="pt")
  
  # predict
  with torch.no_grad():
    outputs = model(**inputs)
    preds = outputs.logits
  
  filename = r"C:\Users\kyanzhe\Downloads\prompt-to-mask-main\mask.png"
  plt.imsave(filename, torch.sigmoid(preds))
  # cv2.imshow("mask", torch.sigmoid(preds))
  # mask = torch.sigmoid(preds)
  # mask.show()
  mask_img = mpimg.imread(filename)


  plt.imshow(image)
  plt.imshow(mask_img, cmap='jet', alpha=0.5)
  # plt.imshow(mask_img)
  plt.show()
  
  # # img2 = cv2.imread(filename)
  # # gray_image = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

  # # (thresh, bw_image) = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
  
  # # # fix color format
  # # cv2.cvtColor(bw_image, cv2.COLOR_BGR2RGB)
  
  # # return Image.fromarray(bw_image)

  # return Image.open("mask.png").convert("RGB")
  return True
  
title = "Interactive demo: zero-shot image segmentation with CLIPSeg"
description = "Demo for using CLIPSeg, a CLIP-based model for zero- and one-shot image segmentation. To use it, simply upload an image and add a text to mask (identify in the image), or use one of the examples below and click 'submit'. Results will show up in a few seconds."
article = "<p style='text-align: center'><a href='https://arxiv.org/abs/2112.10003'>CLIPSeg: Image Segmentation Using Text and Image Prompts</a> | <a href='https://huggingface.co/docs/transformers/main/en/model_doc/clipseg'>HuggingFace docs</a></p>"

examples = [[r"C:\Users\kyanzhe\Downloads\download (3).jfif", "wood"]]
   
# interface = gr.Interface(fn=process_image, 
#                      inputs=[gr.Image(type="pil"), gr.Textbox(label="Please describe what you want to identify")],
#                      outputs=gr.Image(type="pil"),
#                      title=title,
#                      description=description,
#                      article=article,
#                      examples=examples)
                     
# interface.launch(debug=True)

process_image( Image.open(r"C:\Users\kyanzhe\Downloads\download (3).jfif").convert('RGB'),"man in blue shirt")