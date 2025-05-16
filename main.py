romen_format = input("Çevirmek istediğiniz roma rakamını girin: ")

romen_to_int_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

arabic_value = 0
prev_value = 0
prev_char=""
repeat_count = 0
failure=False

for i in reversed(romen_format):
    value = romen_to_int_dict[i]
    if i == prev_char:
        repeat_count+=1
        if repeat_count > 3:
            failure=True
            print("Bir rakam en fazla 3 kez tekrar edebilir!")
            break

    else:
        repeat_count = 1

    if value < prev_value:
        arabic_value -= value

    else:
        arabic_value += value
        prev_value = value

    prev_char=i

if failure:
    print("Hatalı sayı girdiniz!")
else:
    print("Girmek istediğiniz değerin sayısal değeri: ",arabic_value)
