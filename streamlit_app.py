import streamlit as st

st.title("健康小问题")
def main():
    variable_from_url = st.experimental_get_query_params().get("variable", [0])[0]
    
    if variable_from_url == "0":
        #variable_from_url = "X"
        st.session_state.question = "questions_chen"
    elif variable_from_url == "1":
        #variable_from_url = "X"
        st.session_state.question == "questions_chi"
    elif variable_from_url == "2":
        #variable_from_url = "X"
        st.session_state.question = "questions_fu"
    elif variable_from_url == "3":
        #variable_from_url = "X"
        st.session_state.question = "questions_shi"
    elif variable_from_url == "4":
        #variable_from_url = "X"
        st.session_state.question = "questions_shu"
    elif variable_from_url == "5":
        #variable_from_url = "X"
        st.session_state.question = "questions_xu"
    else:
        st.session_state.question = st.session_state.question 
        
    questions_chen = [
        {
            "question": "你比较胖/瘦？",
            "options": ["胖", "瘦"],
            "answer": ""
        },
        {
            "question": "你是否最近感觉到困乏疲惫？",
            "options": ["是", "否"],
            "answer": ""
        },
        {
            "question": "你最近吃饭的胃口怎么样？",
            "options": ["好", "坏"],
            "answer": ""
        }
   ]
    questions_chi = [
        {
            "question": "你长期从事体力劳动或高强度运动吗？",
            "options": ["是", "否"],
            "answer": 
        },
        {
            "question": "你最近排便顺畅吗？",
            "options": ["是", "否"],
            "answer": 
        },
        {
            "question": "你常居住在高海拔区？",
            "options": ["是", "否"],
            "answer": 
        },
        {
            "question": "你最近有吹冷风着凉的经历吗？",
            "options": ["是", "否"],
            "answer":
        }
    ]
    questions_fu = [

        {
            "question": "你感到冷/热吗？",
            "options": ["冷", "热"],
            "answer":
        },
        {
            "question": "你比较胖/瘦？",
            "options": ["胖", "瘦"],
            "answer":
        },
        {
            "question": "你是否有长期的疾病史？",
            "options": ["是", "否"],
            "answer":
        }
    ]
    questions_shi = [
        {
            "question": "你最近是否发烧或者感冒过？",
            "options": ["是", "否"],
            "answer":
        },
        {
            "question": "你喜欢喝酒吗？",
            "options": ["是", "否"],
            "answer":
        },
        {
            "question": "你经常熬夜吗？",
            "options": ["是", "否"],
            "answer":
        },
        {
            "question": "你最近总是发脾气吗？",
            "options": ["是", "否"],
            "answer":
        }
    ]
    questions_shu = [
        {
            "question": "你感觉到热吗？",
            "options": ["是", "否"],
            "answer":
        },
        {
            "question": "你晚上睡觉流汗吗？",
            "options": ["是", "否"],
            "answer":
        },
        {
            "question": "你常常感觉气短心跳加速吗？",
            "options": ["是", "否"],
            "answer": 
        }
    ]
    questions_xu = [
        {
            "question": "你最近有消化不良吗？",
            "options": ["是", "否"],
            "answer":
        },
        {
            "question": "你贫血吗？",
            "options": ["是", "否"],
            "answer":
        },
        {
            "question": "你瘦吗？",
            "options": ["是", "否"],
            "answer":
        }
    ]

    # 沉脉
    if st.session_state.question == "questions_chen":
        i=0
        current_question = questions_chen[i]
        st.write(current_question["question"])
        
        for option in current_question["options"]:
            if st.button(option):
                current_question["answer"] = option
                i += 1
                break
        
        if current_question["answer"]:
            st.button("确认")
    else:
        st.title("选项已完成")
        st.write("您已完成所有选项。")
    
    #迟脉
     if st.session_state.question == "questions_chi":
        i=0
        current_question = questions_chi[i]
        st.write(current_question["question"])
        
        for option in current_question["options"]:
            if st.button(option):
                current_question["answer"] = option
                i += 1
                break
        
        if current_question["answer"]:
            st.button("确认")
    else:
        st.title("选项已完成")
        st.write("您已完成所有选项。")
    
    #浮脉
     if st.session_state.question == "questions_fu":
        i=0
        current_question = questions_fu[i]
        st.write(current_question["question"])
        
        for option in current_question["options"]:
            if st.button(option):
                current_question["answer"] = option
                i += 1
                break
        
        if current_question["answer"]:
            st.button("确认")
    else:
        st.title("选项已完成")
        st.write("您已完成所有选项。")
    
    #实脉
     if st.session_state.question == "questions_shi":
        i=0
        current_question = questions_shi[i]
        st.write(current_question["question"])
        
        for option in current_question["options"]:
            if st.button(option):
                current_question["answer"] = option
                i += 1
                break
        
        if current_question["answer"]:
            st.button("确认")
    else:
        st.title("选项已完成")
        st.write("您已完成所有选项。")
    
    #数脉
     if st.session_state.question == "questions_shu":
        i=0
        current_question = questions_shu[i]
        st.write(current_question["question"])
        
        for option in current_question["options"]:
            if st.button(option):
                current_question["answer"] = option
                i += 1
                break
        
        if current_question["answer"]:
            st.button("确认")
    else:
        st.title("选项已完成")
        st.write("您已完成所有选项。")
    
    #虚脉
    if st.session_state.question == "questions_xu":
        i=0
        current_question = questions_xu[i]
        st.write(current_question["question"])
        
        for option in current_question["options"]:
            if st.button(option):
                current_question["answer"] = option
                i += 1
                break
        
        if current_question["answer"]:
            st.button("确认")
    else:
        st.title("选项已完成")
        st.write("您已完成所有选项。")

if __name__ == "__main__":
    if 'question' not in st.session_state:
        st.session_state.question = "e"
main()
