#!/usr/bin/env python3

from string import Template # more secure than format string method

def main():
    str1 = "Advanced {0} the {1}".format("python", "First chapter")
    print(str1)

    # create a template w/placeholders
    templ = Template("Advanced ${language} the ${chapter}")

    # use the substitute method with keyword arguments
    str2 = templ.substitute(language="python", chapter="First chapter")
    print(str2)
    
    # use the substute method with a dictionary
    data = {"language": "python", "chapter": "First chapter"}
    str3 = templ.substitute(data)
    print(str3)

if __name__ == '__main__':
    main()