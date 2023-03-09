n = int(input())
i = 2

star='*'
s1 = star
s2 = [s1+' '*len(s1)+ s1, ' '*len(s1) + star + ' '*len(s1), s1+' '*len(s1)+ s1]

fst_line = ['',s2[0]]
scd_line = ['',s2[1]]
trd_line = ['',s2[2]]

p2_fst = ['',' '*len(s2[2])]
p2_scd = ['',' '*len(s2[2])]
p2_trd = ['',' '*len(s2[2])]

mat = [0,[s1],s2]

if n == 1:
    print(star)
elif n == 2:
    for a in s2:
        print(a)
else:
    p2_fst = ['',' '*len(s2[2]), p2_fst[1]+ fst_line[1] + p2_fst[1]]
    p2_scd = ['',' '*len(s2[2]), p2_scd[1]+ scd_line[1] + p2_scd[1]]
    p2_trd = ['',' '*len(s2[2]), p2_trd[1]+ trd_line[1] + p2_trd[1]]
    while True:
        if i == n:         
            break
        
        
           

        fst_line.append(fst_line[i-1]+' '*len(fst_line[i-1])+ fst_line[i-1])
        scd_line.append(scd_line[i-1] + ' '*len(scd_line[i-1]) + scd_line[i-1])
        trd_line.append(trd_line[i-1] + ' '*len(trd_line[i-1]) + trd_line[i-1])
        
        p2_fst.append(p2_fst[i] + ' '* len(p2_fst[i]) + p2_fst[i])
        p2_scd.append(p2_scd[i] + ' '* len(p2_scd[i]) + p2_scd[i])
        p2_trd.append(p2_trd[i] + ' '* len(p2_trd[i]) + p2_trd[i])
          

        m1 = [fst_line[i], scd_line[i], trd_line[i]]
        m2 = [p2_fst[i], p2_scd[i], p2_trd[i]]
        m3 = [fst_line[i], scd_line[i], trd_line[i]]
        mat.append(m1+m2+m3)
        
        
        ans=[]
        for fst in mat[i+1]:
            ans.append(fst)
        if i == 3:
            for scd in mat[i]:
                ans.append(' '*(len(scd)-1)+scd)
            for fst in mat[i+1]:
                ans.append(fst)  
                
        if i ==4:
            for scd in mat[i-1]:
                ans.append(' '*(len(scd))+scd+' '*(len(scd)*5)+scd)
            for fst in mat[i+1]:
                ans.append(fst)
            for fst in mat[i]:
                ans.append(' '*(len(fst)-1)+fst)
            for scd in mat[i-1]:
                ans.append(' '*(len(fst)-1+len(scd))+scd)
            for fst in mat[i]:
                ans.append(' '*(len(fst)-1)+fst)
            for fst in mat[i+1]:
                ans.append(fst)
            for scd in mat[i-1]:
                ans.append(' '*(len(scd))+scd+' '*(len(scd)*5)+scd)
            for fst in mat[i+1]:
                ans.append(fst)
        i+=1
    for a in ans:
        print(a)
