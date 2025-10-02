
import re
# reqular expression input mail adresi formatını uyuyor mu degil mi gibi 
# sayısal ifadeler ile sadece sayısal ifade istersiniz

result = dir(re)

str = "Python Kursu: Python programlama Rehberiniz | 40 saat"

# re.findall()

result = re.findall("Python",str)
result = len(result)

# re.split()

# result = re.split(" ",str)

# re.sub() substring degistirme yapar

# result = re.sub(" ","*",str)

# result = re.sub("\s","-",str)

str = "Python Kursu: Python programlama Rehberiniz | 40 saat"

result = re.search("Python",str)

# result = result.span()

# result = result.start()
# result = result.end()

# result = result.string

# result = re.findall("[abc]",str)

# result = re.findall("[sat]",str)

result = re.findall("[0-5]",str)

# ^abc dısındaki karekterler
result =re.findall("[^abc]",str)



str = "Python Kursu: Python programlama Rehberiniz | 40 saat"

result = re.findall("[^0-9]",str)

# . herhangi bir karakter a b c gibi
# .. iki karakter ab ac 

str = "Python aKursu: Python programlama Rehberiniz | 40 saat"

# $ belirtilen ile biityor mu

# result = re.findall("saatt$",str)

# {} --> karakter sayısını kontrol eder

str = "Python aKursu: Python programlama Rehberiniz | 40 saat"

# result =re.findall("[0-9]{2}",str) # 0-9 arasında 2 basamaklı karakter arıyoruz



str = "Python aKursu: Python programlama Rehberiniz | 40 saat"

result = re.findall("saat\Z",str)

print(result)



