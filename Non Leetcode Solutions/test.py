seq_cnt=0
seq_len=0
seq_dif=0
a=[3, 5, 3, 6, 3, 4, 10, 4, 5, 2]
n=len(a)
for i in range(n-1):
    dif=a[i]-a[i+1]
    if seq_dif!=dif and seq_len>=3:
        seq_cnt+=1
        seq_len=0
        seq_dif=dif
    elif seq_dif!=dif:
        seq_len=0
        seq_dif=dif
    elif seq==dif:
        seq_len+=1
print(seq_cnt,seq_len,seq_dif)
