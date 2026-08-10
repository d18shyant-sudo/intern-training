text ="A"*2500
print(text)
def chunks(text):
    for i in range(0,len(text),800):
        yield text[i:i+800]
for chunk in chunks(text):
    print(chunk)
    print("chunk end")