##reverse complement(역염기서열) 찾기

#DNA 염기서열을 상보적으로 바꾸는 Complement()함수
def comp(seq):
    com_dict = {'A':'T','T':'A','C':'G','G':'C'}
    seq_comp = ""
    for char in seq:
        seq_comp = seq_comp + comp_dict[char]
    return seq_comp

#DNA 염기서열을 역순으로 바꾸는 Reverse 함수
def rev(seq):
    seq_rev = "".join(reversed(seq))
    return seq_rev

#DNA를 상보적 역순으로 바꾸는 rev_comp 함수
def rev_comp(seq):
    temp = comp(seq)
    return rev(tmp)

src = input("DNA sequence:")
cnvt = int(input("1(comp),2(rev),3(Rev_comp):"))
if(cnvt >=1 and cnvt <=3):
    if(cnvt ==1):
        rst = comp(src)
    elif(cnvt ==2):
        rst = rev(src)
    else:
        rst = rev_comp(src)
    print(src,"->",rst)

else:
    print("1(comp),2(rev),3(rev_comp)!!")
