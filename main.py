import streamlit as st
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

st.title("🎨 네 이상형 그려주는 앱")

prompt = st.text_input("이상형을 설명해 주세요:", "긴 금발 머리, 푸른 눈, 밝은 미소")

if st.button("그려줘!"):
    if not prompt.strip():
        st.warning("이상형을 입력해 주세요!")
    else:
        with st.spinner("그리는 중... 조금만 기다려 주세요!"):
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="512x512"
            )
            image_url = response['data'][0]['url']
            st.image(image_url, caption="당신의 이상형", use_column_width=True)
