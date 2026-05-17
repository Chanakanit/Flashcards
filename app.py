import streamlit as st

st.set_page_config(page_title="Flashcards", page_icon="📚")

st.title("📚 Flashcards App")

menu = st.sidebar.selectbox(
    "เลือกเมนู",
    ["หน้าแรก", "ทำแบบทดสอบ", "ตั้งค่าคำถาม"]
)

if menu == "หน้าแรก":
    st.header("ยินดีต้อนรับ")
    st.write("ระบบ Flashcards")

elif menu == "ทำแบบทดสอบ":
    st.header("ทำแบบทดสอบ")

    question = "Python ใช้คำสั่งอะไรแสดงผล?"

    st.write(question)

    answer = st.text_input("คำตอบ")

    if st.button("ส่งคำตอบ"):
        if answer.lower() == "print":
            st.success("ถูกต้อง 🎉")
        else:
            st.error("ผิด ❌")

elif menu == "ตั้งค่าคำถาม":
    st.header("ตั้งค่าคำถาม")

    question = st.text_input("เพิ่มคำถาม")
    answer = st.text_input("เพิ่มคำตอบ")

    if st.button("บันทึก"):
        st.success("บันทึกสำเร็จ")