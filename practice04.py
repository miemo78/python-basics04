sample_list = ["yamada",100,"taro",True]

#このリストの中身は xx と xx と xx です。
def output_list(L):
    L=[str(a) for a in L]
    L="と".join(L)
    print("このリストの中身は" + L + "です")

output_list(sample_list)