 import streamlit as st

st.title("健康小问题")



def main():

    # 问题和选项
    option_aa = "沉脉"
    option_bb = "迟脉"
    option_cc = "浮脉"
    option_dd = "实脉"
    option_ee = "数脉"
    option_ff = "虚脉"
    
    question_a = "你比较胖/瘦？"    # Chenmai
    option_a_a = "胖"
    option_a_b = "瘦"
    
    question_b = "你是否最近感觉到困乏疲惫？"
    option_b_a = "是"
    option_b_b = "否"
    
    question_c = "你最近吃饭的胃口怎么样？"
    option_c_a = "好"
    option_c_b = "坏"
    
    question_d = "你长期从事体力劳动或高强度运动吗？"    #Chimai
    option_d_a = "是"
    option_d_b = "否"
    
    question_e = "你最近排便顺畅吗？"   
    option_e_a = "是"
    option_e_b = "否"
    
    question_f = "你常居住在高海拔区？"
    option_f_a = "是"
    option_f_b = "否"
    
    question_g = "你最近有吹冷风着凉的经历吗？"
    option_g_a = "是"
    option_g_b = "否"
    
    question_h = "你感到冷/热吗？"    #Fumai
    option_h_a = "冷"
    option_h_b = "热"
    
    question_i= "你比较胖/瘦？"
    option_i_a = "胖"
    option_i_b = "瘦"
    
    question_j = "你是否有长期的疾病史？"
    option_j_a = "是"
    option_j_b = "否"
    
    question_k = "你最近是否发烧或者感冒过？" #Shimai
    option_k_a = "是"
    option_k_b = "否"
    
    question_l = "你喜欢喝酒吗？"
    option_l_a = "是"
    option_l_b = "否"
    
    question_m = "你经常熬夜吗？"
    option_m_a = "是"
    option_m_b = "否"
    
    question_n = "你最近总是发脾气吗？"
    option_n_a = "是"
    option_n_b = "否"
    
    question_o = "你感觉到热吗？"    #Shumai
    option_o_a = "是"
    option_o_b = "否"
    
    question_p = "你晚上睡觉流汗吗？"
    option_p_a = "是"
    option_p_b = "否"
    
    question_q = "你常常感觉气短心跳加速吗？"
    option_q_a = "是"
    option_q_b = "否"
    
    question_r = "你最近有消化不良吗？" #Xumai
    option_r_a = "是"
    option_r_b = "否"
    
    question_s = "你贫血吗？"
    option_s_a = "是"
    option_s_b = "否"
    
    question_t = "你瘦吗？"
    option_t_a = "是"
    option_t_b = "否"

# 获取传递的变量
    variable_from_url = st.experimental_get_query_params().get("variable", [0])[0]
    
    if variable_from_url == "0":
        st.session_state.question = "a"
        # 沉脉
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
                st.session_state.question = "c"
                st.experimental_rerun()
        
            elif st.button(option_b_b):
                st.write(f"您选择了 {option_b_b}。")
                st.session_state.question = "c"
                st.experimental_rerun()
                
        elif st.session_state.question == "c":
            st.write(question_c)
        
            # 显示选项按钮
            if st.button(option_c_a):
                st.write(f"您选择了 {option_c_a}。")
                st.session_state.question = "c"
                st.experimental_rerun()
        
            elif st.button(option_c_b):
                st.write(f"您选择了 {option_b_b}。")
                st.session_state.question = "c"
                st.experimental_rerun()
            st.experimental_rerun()
            
    elif variable_from_url == "1":
        st.session_state.question == "d"
        #迟脉
        if st.session_state.question == "d":
            st.write(question_d)
        
            # 显示选项按钮
            if st.button(option_d_a):
                st.write(f"您选择了 {option_d_a}。")
                st.session_state.question = "e"
                st.experimental_rerun()
        
            elif st.button(option_d_b):
                st.write(f"您选择了 {option_d_b}。")
                st.session_state.question = "e"
                st.experimental_rerun()
        
        elif st.session_state.question == "e":
            st.write(question_e)
        
            # 显示选项按钮
            if st.button(option_e_a):
                st.write(f"您选择了 {option_e_a}。")
                st.session_state.question = "f"
                st.experimental_rerun()
        
            elif st.button(option_e_b):
                st.write(f"您选择了 {option_e_b}。")
                st.session_state.question = "f"
                st.experimental_rerun()
                
        elif st.session_state.question == "f":
            st.write(question_f)
        
            # 显示选项按钮
            if st.button(option_f_a):
                st.write(f"您选择了 {option_f_a}。")
                st.session_state.question = "g"
                st.experimental_rerun()
        
            elif st.button(option_f_b):
                st.write(f"您选择了 {option_f_b}。")
                st.session_state.question = "g"
                st.experimental_rerun()
    
    elif variable_from_url == "2":
        st.session_state.question = "h"
         #浮脉
        if st.session_state.question == "h":
            st.write(question_h)
        
            # 显示选项按钮
            if st.button(option_h_a):
                st.write(f"您选择了 {option_h_a}。")
                st.session_state.question = "i"
                st.experimental_rerun()
        
            elif st.button(option_h_b):
                st.write(f"您选择了 {option_h_b}。")
                st.session_state.question = "i"
                st.experimental_rerun()
        
        elif st.session_state.question == "i":
            st.write(question_i)
        
            # 显示选项按钮
            if st.button(option_i_a):
                st.write(f"您选择了 {option_i_a}。")
                st.session_state.question = "j"
                st.experimental_rerun()
        
            elif st.button(option_i_b):
                st.write(f"您选择了 {option_i_b}。")
                st.session_state.question = "j"
                st.experimental_rerun()
                
        elif st.session_state.question == "j":
            st.write(question_j)
        
            # 显示选项按钮
            if st.button(option_j_a):
                st.write(f"您选择了 {option_j_a}。")
                st.session_state.question = "j"
                st.experimental_rerun()
        
            elif st.button(option_j_b):
                st.write(f"您选择了 {option_j_b}。")
                st.session_state.question = "j"
                st.experimental_rerun()
    
    elif variable_from_url == "3":
        st.session_state.question = "k"
        #实脉
        if st.session_state.question == "k":
            st.write(question_k)
    
            # 显示选项按钮
            if st.button(option_k_a):
                st.write(f"您选择了 {option_k_a}。")
                st.session_state.question = "l"
                st.experimental_rerun()
        
            elif st.button(option_k_b):
                st.write(f"您选择了 {option_k_b}。")
                st.session_state.question = "l"
                st.experimental_rerun()
    
        elif st.session_state.question == "l":
            st.write(question_l)
        
            # 显示选项按钮
            if st.button(option_l_a):
                st.write(f"您选择了 {option_l_a}。")
                st.session_state.question = "m"
                st.experimental_rerun()
        
            elif st.button(option_l_b):
                st.write(f"您选择了 {option_l_b}。")
                st.session_state.question = "m"
                st.experimental_rerun()
                
        elif st.session_state.question == "m":
            st.write(question_m)
        
            # 显示选项按钮
            if st.button(option_m_a):
                st.write(f"您选择了 {option_m_a}。")
                st.session_state.question = "n"
                st.experimental_rerun()
        
            elif st.button(option_m_b):
                st.write(f"您选择了 {option_m_b}。")
                st.session_state.question = "n"
                st.experimental_rerun()
        
        elif st.session_state.question == "n":
            st.write(question_n)
        
            # 显示选项按钮
            if st.button(option_n_a):
                st.write(f"您选择了 {option_n_a}。")
                st.session_state.question = "n"
                st.experimental_rerun()
        
            elif st.button(option_n_b):
                st.write(f"您选择了 {option_n_b}。")
                st.session_state.question = "n"
                st.experimental_rerun()
                
    elif variable_from_url == "4":
        st.session_state.question = "o"
        #数脉
        if st.session_state.question == "o":
            st.write(question_o)
    
            # 显示选项按钮
            if st.button(option_o_a):
                st.write(f"您选择了 {option_o_a}。")
                st.session_state.question = "p"
                st.experimental_rerun()
        
            elif st.button(option_o_b):
                st.write(f"您选择了 {option_o_b}。")
                st.session_state.question = "p"
                st.experimental_rerun()
    
        elif st.session_state.question == "p":
            st.write(question_p)
        
            # 显示选项按钮
            if st.button(option_p_a):
                st.write(f"您选择了 {option_p_a}。")
                st.session_state.question = "q"
                st.experimental_rerun()
        
            elif st.button(option_p_b):
                st.write(f"您选择了 {option_p_b}。")
                st.session_state.question = "q"
                st.experimental_rerun()
                
        elif st.session_state.question == "q":
            st.write(question_q)
        
            # 显示选项按钮
            if st.button(option_q_a):
                st.write(f"您选择了 {option_q_a}。")
                st.session_state.question = "q"
                st.experimental_rerun()
        
            elif st.button(option_q_b):
                st.write(f"您选择了 {option_q_b}。")
                st.session_state.question = "q"
                st.experimental_rerun()
    elif variable_from_url == "5":
        st.session_state.question = "r"
        #虚脉
        if st.session_state.question == "r":
            st.write(question_r)
    
        # 显示选项按钮
            if st.button(option_r_a):
                st.write(f"您选择了 {option_r_a}。")
                st.session_state.question = "s"
                st.experimental_rerun()
        
            elif st.button(option_r_b):
                st.write(f"您选择了 {option_r_b}。")
                st.session_state.question = "s"
                st.experimental_rerun()
    
        elif st.session_state.question == "s":
            st.write(question_s)
        
            # 显示选项按钮
            if st.button(option_s_a):
                st.write(f"您选择了 {option_s_a}。")
                st.session_state.question = "t"
                st.experimental_rerun()
        
            elif st.button(option_s_b):
                st.write(f"您选择了 {option_s_b}。")
                st.session_state.question = "t"
                st.experimental_rerun()
                
        elif st.session_state.question == "t":
            st.write(question_t)
        
            # 显示选项按钮
            if st.button(option_t_a):
                st.write(f"您选择了 {option_t_a}。")
                st.session_state.question = "t"
                st.experimental_rerun()
        
            elif st.button(option_t_b):
                st.write(f"您选择了 {option_t_b}。")
                st.session_state.question = "t"
                st.experimental_rerun()
    
    
        
        # 问题和选项
        option_aa = "沉脉"
        option_bb = "迟脉"
        option_cc = "浮脉"
        option_dd = "实脉"
        option_ee = "数脉"
        option_ff = "虚脉"
    
        question_a = "你比较胖/瘦？"    # Chenmai
        option_a_a = "胖"
        option_a_b = "瘦"
    
        question_b = "你是否最近感觉到困乏疲惫？"
        option_b_a = "是"
        option_b_b = "否"
     
        question_c = "你最近吃饭的胃口怎么样？"
        option_c_a = "好"
        option_c_b = "坏"
     
        question_d = "你长期从事体力劳动或高强度运动吗？"    #Chimai
        option_d_a = "是"
        option_d_b = "否"
     
        question_e = "你最近排便顺畅吗？"   
        option_e_a = "是"
        option_e_b = "否"
     
        question_f = "你常居住在高海拔区？"
        option_f_a = "是"
        option_f_b = "否"
     
        question_g = "你最近有吹冷风着凉的经历吗？"
        option_g_a = "是"
        option_g_b = "否"
     
        question_h = "你感到冷/热吗？"    #Fumai
        option_h_a = "冷"
        option_h_b = "热"
     
        question_i= "你比较胖/瘦？"
        option_i_a = "胖"
        option_i_b = "瘦"
     
        question_j = "你是否有长期的疾病史？"
        option_j_a = "是"
        option_j_b = "否"
     
        question_k = "你最近是否发烧或者感冒过？" #Shimai
        option_k_a = "是"
        option_k_b = "否"
     
        question_l = "你喜欢喝酒吗？"
        option_l_a = "是"
        option_l_b = "否"
     
        question_m = "你经常熬夜吗？"
        option_m_a = "是"
        option_m_b = "否"
     
        question_n = "你最近总是发脾气吗？"
        option_n_a = "是"
        option_n_b = "否"
     
        question_o = "你感觉到热吗？"    #Shumai
        option_o_a = "是"
        option_o_b = "否"
     
        question_p = "你晚上睡觉流汗吗？"
        option_p_a = "是"
        option_p_b = "否"
     
        question_q = "你常常感觉气短心跳加速吗？"
        option_q_a = "是"
        option_q_b = "否"
     
        question_r = "你最近有消化不良吗？" #Xumai
        option_r_a = "是"
        option_r_b = "否"
     
        question_s = "你贫血吗？"
        option_s_a = "是"
        option_s_b = "否"
    
        question_t = "你瘦吗？"
        option_t_a = "是"
        option_t_b = "否"
'''    
    if st.session_state.question == "initial":
        st.write("请选择一个脉象：")
        if st.button("沉脉"):
            st.session_state.question = "a"
            st.experimental_rerun()
        elif st.button("迟脉"):
            st.session_state.question = "d"
            st.experimental_rerun()
        elif st.button("浮脉"):
            st.session_state.question = "h"
            st.experimental_rerun()
        elif st.button("实脉"):
            st.session_state.question = "k"
            st.experimental_rerun()
        elif st.button("数脉"):
            st.session_state.question = "o"
            st.experimental_rerun()
        elif st.button("虚脉"):
            st.session_state.question = "r"
            st.experimental_rerun()
'''  
'''
    # 沉脉
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
            st.session_state.question = "c"
            st.experimental_rerun()
    
        elif st.button(option_b_b):
            st.write(f"您选择了 {option_b_b}。")
            st.session_state.question = "c"
            st.experimental_rerun()
            
    elif st.session_state.question == "c":
        st.write(question_c)
    
        # 显示选项按钮
        if st.button(option_c_a):
            st.write(f"您选择了 {option_c_a}。")
            st.session_state.question = "c"
            st.experimental_rerun()
    
        elif st.button(option_c_b):
            st.write(f"您选择了 {option_b_b}。")
            st.session_state.question = "c"
            st.experimental_rerun()
    
    #迟脉
    if st.session_state.question == "d":
        st.write(question_d)
    
        # 显示选项按钮
        if st.button(option_d_a):
            st.write(f"您选择了 {option_d_a}。")
            st.session_state.question = "e"
            st.experimental_rerun()
    
        elif st.button(option_d_b):
            st.write(f"您选择了 {option_d_b}。")
            st.session_state.question = "e"
            st.experimental_rerun()
    
    elif st.session_state.question == "e":
        st.write(question_e)
    
        # 显示选项按钮
        if st.button(option_e_a):
            st.write(f"您选择了 {option_e_a}。")
            st.session_state.question = "f"
            st.experimental_rerun()
    
        elif st.button(option_e_b):
            st.write(f"您选择了 {option_e_b}。")
            st.session_state.question = "f"
            st.experimental_rerun()
            
    elif st.session_state.question == "f":
        st.write(question_f)
    
        # 显示选项按钮
        if st.button(option_f_a):
            st.write(f"您选择了 {option_f_a}。")
            st.session_state.question = "g"
            st.experimental_rerun()
    
        elif st.button(option_f_b):
            st.write(f"您选择了 {option_f_b}。")
            st.session_state.question = "g"
            st.experimental_rerun()
    
    #浮脉
    if st.session_state.question == "h":
        st.write(question_h)
    
        # 显示选项按钮
        if st.button(option_h_a):
            st.write(f"您选择了 {option_h_a}。")
            st.session_state.question = "i"
            st.experimental_rerun()
    
        elif st.button(option_h_b):
            st.write(f"您选择了 {option_h_b}。")
            st.session_state.question = "i"
            st.experimental_rerun()
    
    elif st.session_state.question == "i":
        st.write(question_i)
    
        # 显示选项按钮
        if st.button(option_i_a):
            st.write(f"您选择了 {option_i_a}。")
            st.session_state.question = "j"
            st.experimental_rerun()
    
        elif st.button(option_i_b):
            st.write(f"您选择了 {option_i_b}。")
            st.session_state.question = "j"
            st.experimental_rerun()
            
    elif st.session_state.question == "j":
        st.write(question_j)
    
        # 显示选项按钮
        if st.button(option_j_a):
            st.write(f"您选择了 {option_j_a}。")
            st.session_state.question = "j"
            st.experimental_rerun()
    
        elif st.button(option_j_b):
            st.write(f"您选择了 {option_j_b}。")
            st.session_state.question = "j"
            st.experimental_rerun()
    
    #实脉
    if st.session_state.question == "k":
        st.write(question_k)
    
        # 显示选项按钮
        if st.button(option_k_a):
            st.write(f"您选择了 {option_k_a}。")
            st.session_state.question = "l"
            st.experimental_rerun()
    
        elif st.button(option_k_b):
            st.write(f"您选择了 {option_k_b}。")
            st.session_state.question = "l"
            st.experimental_rerun()
    
    elif st.session_state.question == "l":
        st.write(question_l)
    
        # 显示选项按钮
        if st.button(option_l_a):
            st.write(f"您选择了 {option_l_a}。")
            st.session_state.question = "m"
            st.experimental_rerun()
    
        elif st.button(option_l_b):
            st.write(f"您选择了 {option_l_b}。")
            st.session_state.question = "m"
            st.experimental_rerun()
            
    elif st.session_state.question == "m":
        st.write(question_m)
    
        # 显示选项按钮
        if st.button(option_m_a):
            st.write(f"您选择了 {option_m_a}。")
            st.session_state.question = "n"
            st.experimental_rerun()
    
        elif st.button(option_m_b):
            st.write(f"您选择了 {option_m_b}。")
            st.session_state.question = "n"
            st.experimental_rerun()
    
    elif st.session_state.question == "n":
        st.write(question_n)
    
        # 显示选项按钮
        if st.button(option_n_a):
            st.write(f"您选择了 {option_n_a}。")
            st.session_state.question = "n"
            st.experimental_rerun()
    
        elif st.button(option_n_b):
            st.write(f"您选择了 {option_n_b}。")
            st.session_state.question = "n"
            st.experimental_rerun()
    
    #数脉
    if st.session_state.question == "o":
        st.write(question_o)
    
        # 显示选项按钮
        if st.button(option_o_a):
            st.write(f"您选择了 {option_o_a}。")
            st.session_state.question = "p"
            st.experimental_rerun()
    
        elif st.button(option_o_b):
            st.write(f"您选择了 {option_o_b}。")
            st.session_state.question = "p"
            st.experimental_rerun()
    
    elif st.session_state.question == "p":
        st.write(question_p)
    
        # 显示选项按钮
        if st.button(option_p_a):
            st.write(f"您选择了 {option_p_a}。")
            st.session_state.question = "q"
            st.experimental_rerun()
    
        elif st.button(option_p_b):
            st.write(f"您选择了 {option_p_b}。")
            st.session_state.question = "q"
            st.experimental_rerun()
            
    elif st.session_state.question == "q":
        st.write(question_q)
    
        # 显示选项按钮
        if st.button(option_q_a):
            st.write(f"您选择了 {option_q_a}。")
            st.session_state.question = "q"
            st.experimental_rerun()
    
        elif st.button(option_q_b):
            st.write(f"您选择了 {option_q_b}。")
            st.session_state.question = "q"
            st.experimental_rerun()
    
    #虚脉
    if st.session_state.question == "r":
        st.write(question_r)
    
        # 显示选项按钮
        if st.button(option_r_a):
            st.write(f"您选择了 {option_r_a}。")
            st.session_state.question = "s"
            st.experimental_rerun()
    
        elif st.button(option_r_b):
            st.write(f"您选择了 {option_r_b}。")
            st.session_state.question = "s"
            st.experimental_rerun()
    
    elif st.session_state.question == "s":
        st.write(question_s)
    
        # 显示选项按钮
        if st.button(option_s_a):
            st.write(f"您选择了 {option_s_a}。")
            st.session_state.question = "t"
            st.experimental_rerun()
    
        elif st.button(option_s_b):
            st.write(f"您选择了 {option_s_b}。")
            st.session_state.question = "t"
            st.experimental_rerun()
            
    elif st.session_state.question == "t":
        st.write(question_t)
    
        # 显示选项按钮
        if st.button(option_t_a):
            st.write(f"您选择了 {option_t_a}。")
            st.session_state.question = "t"
            st.experimental_rerun()
    
        elif st.button(option_t_b):
            st.write(f"您选择了 {option_t_b}。")
            st.session_state.question = "t"
            st.experimental_rerun()
    '''
if __name__ == "__main__":
    if 'question' not in st.session_state:
        st.session_state.question = "initial"
    main()
