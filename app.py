import gradio as gr
from transformers import VisionEncoderDecoderModel,ViTImageProcessor,RobertaTokenizerFast
from PIL import Image
def image_captioner(inp):
    model = VisionEncoderDecoderModel.from_pretrained('ViT_Roberta_Image_Captioning')
    image_processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224-in21k')
    tokenizer = RobertaTokenizerFast.from_pretrained('Byte_tokenizer')
    cap = tokenizer.decode(model.generate(image_processor(images = inp, return_tensors="pt").pixel_values)[0])
    return f'{cap.replace("<s>","").replace("</s>","")}'

app = gr.Interface(fn=image_captioner, inputs="image", outputs="label")
app.launch(share=True)