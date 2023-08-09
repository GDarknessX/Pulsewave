# Pulsewave
import streamlit as st

def main():
    st.title("选择题网站")

    # 问题和选项
    question = "哪种编程语言是最流行的？"
    option_a = "Python"
    option_b = "Java"

    st.write(question)

    # 显示选项按钮
    if st.button(option_a):
        st.write(f"您选择了 {option_a}。")
    elif st.button(option_b):
        st.write(f"您选择了 {option_b}。")

if __name__ == "__main__":
    main()
