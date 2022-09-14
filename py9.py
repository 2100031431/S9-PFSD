name="baaghi"
count=0
while True:
    word= input("enter word:").lower()
    count+=1
    if word == name:
        print("word  equal to name")
        break
    if word!= name and count>7:
        print("count:",count)
        print("wprd not equalto name")
        break