text="helloworldtotheworldofpullechanandkaradikuttanamaar"
count_vov=0
count_con=0

vov_seq=("a","e","i","o","u")
for ch in text:

    if ch in vov_seq:

        count_vov+=1
    else:
        count_con+=1

print(f"no of vowels ={count_vov}")

print(f"no of consonents =  {count_con}")

    