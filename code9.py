#file I/O

with open("practice.test","r") as f:
    data = f.read()
    new_data = data.replace("python","Java")
    print(new_data)

def check_for_word():

    with open("practice.test","r") as f:
        data = f.read()
        if(data.find("learning") != -1):
            print("the word exists in the file")
        else:
            print("the word does not exist in the file")

check_for_word()

