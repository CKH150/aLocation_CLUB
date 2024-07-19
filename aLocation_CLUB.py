import streamlit as st
from convert_to_ordinal import num2ord
import numpy as np
import scipy
import pandas as pd


st.title(" 會司其職 ")
st.caption(" Version Aplha 0.2 ")


n = int(4)
members = ["Leo","Winnie","Layla","Hin"]
n_member=len(members)
posts = ["主席","副主席","學術幹事","宣傳幹事"]

col_names = [f"第{d+1}志願" for d in range(n)]
df1 = pd.DataFrame(columns=col_names)
col_configs = [None]*n

priority_table = [None] * n_member
iii = 0

for respondent in members:
    try:
        print(f"Hi, {respondent}.\n學會當中有如下職位： {posts}。")
        
        st.subheader(respondent)
        raw_priority_list = st.multiselect(
            f"Hello, {respondent}！請按照你个人的偏好程度為這些職位排序（從最希望擔任到最不希望擔任）： ",
            options = posts
            )
        
        new_row = pd.DataFrame([raw_priority_list], columns=col_names)  # 创建一个只包含新行的DataFrame
        df1 = pd.concat([df1, new_row], ignore_index=True)  # 将新行添加到原始DataFrame
        
        priority_list = []
        for raw_option in raw_priority_list: 
            choice_num = posts.index(raw_option)
            priority_list.append(choice_num)
            
        priority_table[iii] = priority_list
        iii += 1
    except BaseException:
        pass

try:
    column_configuration = dict.fromkeys(col_names, 0)

    for k in range(n):
        col_configs[k] = st.column_config.SelectboxColumn(
                col_names[k],
                options=posts
        )


    for i in range(n):
        column_configuration[col_names[i]] = col_configs[i]
        

    matrix = np.array(priority_table)
    row_ind, col_ind = scipy.optimize.linear_sum_assignment(matrix)
        
    corre = list(col_ind)
    report = ""
    allocatee_list = []

    for i in range(n_member):
        post_allocated = posts[i]
        member_number = corre.index(i)
        allocatee = members[member_number]
        allocatee_list.append(allocatee)
        

    st.success("分配成功", icon="🔥")

    st.header(" 分配結果：")
    st.write(
        pd.DataFrame({
        '職位': posts,
        '最優擔任者': allocatee_list}
        )
    )
except BaseException:
        pass