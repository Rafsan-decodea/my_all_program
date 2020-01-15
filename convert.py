import argparse
from PIL import Image
import random
rand = random.randint(1,1000)


def main(args):
     a = Image.open('{0}'.format(args.f)).convert('RGB').resize((int(args.h),int(args.w)), Image.ANTIALIAS)
     f = a.save('converted{0}.{1}'.format(rand,args.e))
     print '[+]converting Image Succes'
     print '[+]File Save name is ===>Convert{0}.{1}'.format(rand,args.e)

def about():
    print '-'*100
    print '[+]Command Line Free Image Converter'
    print '  [+]Code by Md Rafsan jani shazid'
    print '     [+]Email==> shazidno123@gmail.com'
    print '-'*100


if __name__ =='__main__':
    about()
    parser = argparse.ArgumentParser()
    parser.add_argument('--f',help='input file name')
    parser.add_argument('--h',help='input image hight')
    parser.add_argument('--w',help='input Wide  Width')
    parser.add_argument('--e',help='input File extention.. just put only Extention ex: jpg , ico , PNG  etc ')
    args = parser.parse_args()

    try:
      main(args)
    except:
        print '[!!]Some Thing Wrong When You Make Operation or File Extention is not Recognible, Pass --h argument '

