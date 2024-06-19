import streamlit as st
from transformers import VisionEncoderDecoderModel,ViTImageProcessor,RobertaTokenizerFast
from torchvision import transforms
from PIL import Image
def image_captioner(inp):
    model = VisionEncoderDecoderModel.from_pretrained('ViT_Roberta_Image_Captioning')
    image_processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224-in21k')
    tokenizer = RobertaTokenizerFast.from_pretrained('Byte_tokenizer')
    cap = tokenizer.decode(model.generate(image_processor(images = inp, return_tensors="pt").pixel_values)[0])
    return f'{cap.replace("<s>","").replace("</s>","")}'
import streamlit as st
import streamlit.components.v1 as components

# bootstrap 4 collapse example


st.markdown(
'''
# Hellooooo !! 
### Welcome to my application for generating captions for an image 
'''
)

st.logo(image="https://kaggle.com/static/images/open-in-kaggle.svg",link="https://www.kaggle.com/code/mightywarrior001/anicygan/")

transform = transforms.Compose([
    transforms.PILToTensor()
])
columns = st.columns([0.5,0.5])
with columns[0]:
    with st.container(border=True):
        option = st.selectbox(
            label='\t',
            options =['select an option','camera','file upload']
            )
        input_photo = None
        match option:
            case 'select an option': st.markdown(' I wonder, which method would you like to use to upload images 🤔?')
            case 'camera': 
                st.markdown('#### Say cheeseeeeeeee... ✌️')
                input_photo = st.camera_input(label='\t')
                # st.write(type(input_photo))
            case 'file upload': 
                st.markdown('Please Upload your image in png, jpeg, or jpg format 😊')
                input_photo = st.file_uploader(label='\t', type=['png','jpg','jpeg'])
                # st.write(type(input_photo))
        if input_photo is not None:
            st.session_state.input_photo = Image.open(input_photo).convert('RGB')
            input_photo = transform(st.session_state.input_photo)
            st.write('the image taken as input is, please check how it looks 🥹🥹')
            st.image((input_photo).permute(1,2,0).numpy(),clamp=True)
with columns[1]:
    with st.container(border=True):
        
        if st.button(label='Generate captions'):
            if "input_photo" in st.session_state:
                with st.status(label="loading models...", expanded=True):
                    model = VisionEncoderDecoderModel.from_pretrained('ViT_Roberta_Image_Captioning')
                    image_processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224-in21k')
                    tokenizer = RobertaTokenizerFast.from_pretrained('Byte_tokenizer')
                with st.status(label='Generating Captions...', expanded=True):
                    cap = tokenizer.decode(model.generate(image_processor(images = st.session_state.input_photo, return_tensors="pt").pixel_values)[0])
                    st.markdown('The caption is....😎:')
                    with st.container(border=True):
                        f'#### {cap.replace("<s>","").replace("</s>","")}'
            else:
                st.error(
                '''
                ### Please upload an image
                '''
                )

