from sys import stdin

while True:
    s=stdin.readline().rstrip()
    st=[]

    if s=='.':
        break
    
    suc=True
    for i in range(len(s)):
        c=s[i]

        if c=='(' or c=='{' or c=='[':
            st.append(c)
        elif c==')' or c=='}' or c==']':
            if len(st)==0:
                suc=False
                break
            
            p=st.pop()
            if c==')' and not p=='(':
                suc=False
                break
            elif c=='}' and not p=='{':
                suc=False
                break
            elif c==']' and not p=='[':
                suc=False
                break
    if len(st)>0:
        suc=False

    if suc:
        print("yes")
    else:
        print("no")