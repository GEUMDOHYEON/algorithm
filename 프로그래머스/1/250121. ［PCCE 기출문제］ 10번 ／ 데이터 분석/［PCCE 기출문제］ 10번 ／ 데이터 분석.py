def solution(data, ext, val_ext, sort_by):
    answer = []
    
    e = 0
    if ext == "code":
        e = 0
    elif ext == "date":
        e = 1
    elif ext == "maximum":
        e = 2
    elif ext == "remain":
        e = 3
    s = 0
    if sort_by == "code":
        s = 0
    elif sort_by == "date":
        s = 1
    elif sort_by == "maximum":
        s = 2
    elif sort_by == "remain":
        s = 3
        

    for d in data:
        if val_ext > d[e]:
            answer.append(d)
    answer.sort(key=lambda x:x[s])
    return answer