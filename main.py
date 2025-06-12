import streamlit as st
import random

st.set_page_config(page_title="📰 가짜 뉴스 메이커", page_icon="🗞️", layout="centered")

st.title("🗞️ 가짜 뉴스 메이커")
st.write("콤마(,)로 키워드 3개 이상 입력하면 웃긴 가짜 뉴스 헤드라인을 만들어 드립니다!")

# 뉴스 헤드라인 템플릿 (키워드 3개 사용)
HEADLINE_TEMPLATES = [
    "⚡ 충격! {0}가 {1}에서 {2}를 발견했다?!",
    "🔍 전문가들, {0}와 {1}의 관계에 {2}가 결정적 역할을 했다고 밝혀",
    "👑 대통령, {0} 사건에 대해 {1}를 지시했다! 국민들 {2} 반응 폭발",
    "🔥 최근 {0} 관련 {1} 소식에 {2}가 난리났다!",
    "🎉 세계 최초로 {0}가 {1}와 함께 {2}에 도전한다!",
    "🚨 속보: {0}와 {1}의 충격적인 {2} 사건, 진실은 과연?",
    "🤯 {0} 때문에 {1}가 {2} 상태에 빠졌다는데..."
]

def generate_headline(keywords):
    # 키워드가 3개 미만이면 랜덤 중복으로 채우기
    while len(keywords) < 3:
        keywords.append(random.choice(keywords))
    template = random.choice(HEADLINE_TEMPLATES)
    return template.format(keywords[0], keywords[1], keywords[2])

# 키워드 입력란
user_input = st.text_input("키워드를 입력하세요 (콤마로 구분):", placeholder="예: 우주인, 치킨, 대통령")

if st.button("📰 가짜 뉴스 만들기"):
    if not user_input.strip():
        st.warning("키워드를 적어주세요! 😅")
    else:
        keywords = [k.strip() for k in user_input.split(",") if k.strip()]
        headline = generate_headline(keywords)
        st.markdown(f"### {headline}")
        st.balloons()
