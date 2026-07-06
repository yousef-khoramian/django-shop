def group_list(list,size):
    grouped_list=[]
    for item in range(0,len(list),size):
        grouped_list.append(list[item:item+size])
    return grouped_list

