# Pulsewave
import streamlit as st

def main():
    st.title("选择题网站")

    # 问题和选项
    question_a = "哪种编程语言是最流行的？"
    option_a_a = "Python"
    option_a_b = "Java"

    question_b = "下面哪个城市是法国的首都？"
    option_b_a = "巴黎"
    option_b_b = "伦敦"

    if st.session_state.question == "a":
        st.write(question_a)

        # 显示选项按钮
        if st.button(option_a_a):
            st.write(f"您选择了 {option_a_a}。")
            st.session_state.question = "b"
            st.experimental_rerun()

        elif st.button(option_a_b):
            st.write(f"您选择了 {option_a_b}。")
            st.session_state.question = "b"
            st.experimental_rerun()

    elif st.session_state.question == "b":
        st.write(question_b)

        # 显示选项按钮
        if st.button(option_b_a):
            st.write(f"您选择了 {option_b_a}。")
            st.session_state.question = "a"
            st.experimental_rerun()

        elif st.button(option_b_b):
            st.write(f"您选择了 {option_b_b}。")
            st.session_state.question = "a"
            st.experimental_rerun()

if __name__ == "__main__":
    if 'question' not in st.session_state:
        st.session_state.question = "a"
    main()
