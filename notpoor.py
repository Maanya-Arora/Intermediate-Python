string = input("enter your string:")
ss_not = string.find("not")
ss_poor = string.find("poor")
len_poor = ss_poor + 4
if ss_not != -1:
    if ss_not < ss_poor:
        newstring = string.replace(string[ss_not:len_poor],"good")
        print(newstring)