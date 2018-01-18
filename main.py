#!/usr/bin/python2.7 
#  #!/usr/bin/env python

import os
import re


def main():
    dir_path = os.getcwd() 
    file_path =  os.getcwd() + '/test.csv'
    file2_path = os.getcwd() + '/new_file.txt'
    print(file_path)
    print(file2_path)
    f1 = open(file_path,'r')
    f2 = open(file2_path,'w+')
    list_my = []
    line_count = 0
    for line in f1:
        line_count += 1
        matched = re.search(r'^Date.(\d+\/\d+\/\d+).*$', line)  #Date.03/01/2018  ^Date.(\d+\/\d+\/\d+)
        if matched:
            matched = matched.group(1)
            our_date = matched
            print(matched)
        matched = re.search(r'^Time.(\d+:\d+:\d+).*$', line)  #Time.13:46:16  ^Time.(\d+:\d+:\d+)
        if matched:
            matched = matched.group(1)
            our_time = matched
            print(matched)
        if line_count > 34:
            matched = re.search(r'(^.*$)', line)  #2499333330.-80.5526820409414.
            if matched:
                matched = matched.group(1)
                whole_line = our_date + ' ' + our_time + ' ' + matched
                #print(whole_line)
                list_my.append(whole_line)
                list_my.append('\n')
    for each in list_my:
        print(each)
        f2.write("%s" % each)
    f1.close()
    f2.close() 

    
if __name__ == '__main__':
  main()
