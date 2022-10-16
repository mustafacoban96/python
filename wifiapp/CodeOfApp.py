import os
import re
import subprocess
import shutil



class WifiPassword():
    def __init__(self):
        pass

    def main(self):
        os.mkdir("C:/keyss/")
        subprocess.run("netsh wlan show profile",shell=True)
        subprocess.run("netsh wlan export profile folder=C:\keyss\ key=clear",shell=True,capture_output=True)
        file_list=os.listdir("C:/keyss/")
        files=[]
        for x in file_list:
            if x.endswith(".xml")==True:
                files.append(x)
        counter = 1
        index = 0
        content = open(f"C:/keyss/{files[index]}","r")
        password_str=""
        while counter <= len(files):
            try:
                for word in content:
                    
                    x = word.strip()
                    y = re.search("^<keyMaterial>.*</keyMaterial>$",x)
                    
                    if y == None:
                        continue
                    else:
                        new_type = str(y.group())
                        right_side = new_type.rstrip("</keyMaterial>")
                        left_side = right_side.lstrip("<keyMaterial>")
                        pure_password = left_side
                        #print(files[index],"======>",pure_password)# group() gives value of match that in class type.
                        password_str += (str(files[index]).rstrip(".xml").lstrip("Wi-Fi-"))+" =====> "+pure_password +"\n"
                counter +=1
                index +=1
                content = open(f"C:/keyss/{files[index]}","r")
                #with open("C:/keyss/passwords.txt","a") as f:
                #   f.write(files[index] + " ===> "+ pure_password + "\n")
                    
            except IndexError:
                print("Searching finished")
                break
        content.close()
        shutil.rmtree("C:\keyss",ignore_errors=False,onerror=None)
        return password_str




