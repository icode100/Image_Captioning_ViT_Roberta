## Image Caption Generator with ViT and Roberta

This is a repository for an image caption generator model built using Vision Transformer (ViT) and Roberta. The model is trained on the [flickr10k](https://www.kaggle.com/datasets/icode100/flickr-10k) dataset which derived from the [Flickr](https://www.kaggle.com/datasets/hsankesara/flickr-image-dataset) dataset consisting of 31k images. RobertaMLM and Byte_tokenizer is removed from this github repository for space constraints. 

View on kaggle:
<table align="left">
  <td>
    <a href="https://www.kaggle.com/icode100/image-captioning" target="_parent"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Colab"/></a>
  </td>
</table>

## Contents
- [Models](#models)
- [Features](#features)
- [Dependancies](#dependencies)
- [Usage](#usage)
- [Trainig](#training)



---
**ROUGE2 SCORES**

| Metric | Score |
|---|---|
| Precision | 0.114700 |
| Recall | 0.124500 |
| F1-Score | 0.114100 |

---

### Models

* [RobertaMLM](https://www.kaggle.com/models/icode100/robertamlm) the Roberta model fine-tuned on Masked Lnaguage modeling
* [ViT_Roberta_Image_Captioning](https://www.kaggle.com/models/icode100/vit_roberta_image_captioning) made using VitEncoderDecoder where ViT acts as image encoder and RobertaMLM being the language based decoder
* [The Byte pair tokenizer](https://www.kaggle.com/models/icode100/byte_tokenizer) 

### Features

* Generates captions for images based on visual content and learned language patterns.
* Leverages the power of ViT for efficient image encoding and Roberta for robust text generation.

### Dependencies

This project requires the following libraries:

* Transformers
* torch
* Pillow (PIL Fork)


### Usage

* This is the [application](https://huggingface.co/spaces/icode100/Image_Captioning) where you can upload image from local file system and the captions will be generated
* For using model in kaggle :
  * visit the [kaggle page](https://www.kaggle.com/models/icode100/vit_roberta_image_captioning) and click create notebook.
  * Add both the datasets provided in the description.
  * The datasets are dependent as flickr10k is derived from Flickr and hence uses the image folder privided in Flickr.
  

### Training

To clone and create your own model:
> `git install lfs`

> `git clone https://huggingface.co/spaces/icode100/Image_Captioning/tree/main`


