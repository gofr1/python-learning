# get file from internet and write to local file
import urllib.request

links = open('../file_name','r')
i = 1

for link in links:
    print(link)
    name = f'name{i}.ext'
    file = urllib.request.urlopen(link)
    print(f'Processing: {link.strip()}...')
    with open(name,'wb') as output:
        _ = output.write(file.read())
    print(f'File: {name} is saved!')
    i+=1

links.close()