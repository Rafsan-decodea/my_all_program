
import subprocess

def  finding_file():
    inp = raw_input('input file name ===>')
    File  = subprocess.check_output(['dir',inp,'/s','/p','|','findstr','Directory of'],shell=True)#dir secret.doc /s /p
    output = File.split("\n")
    for x in output:
        y = x.split(' ')
        for z in y:
            if len(z) >10:
                print z
                subprocess.call(['explorer',z])



if __name__ == '__main__':
    finding_file()