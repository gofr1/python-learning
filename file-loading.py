# get file from internet and write to local file
import urllib.request

links = open('../file_name','r')
i = 1

for link in links:
    print(link)
    name = f'name{i}.ext'
    file = urllib.request.urlopen(link)
    with open(name,'wb') as output:
        output.write(file.read())
    i+=1

links.close()
