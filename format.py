import sys
import os
sys.path.append(os.path.dirname(__file__) + '/CambridgeDict/cambridge_parser')
from CambridgeDict.cambridge_parser import define
from pprint import pprint
from termcolor import colored
# import argparse
from colored import Fore, Back, Style

# parser = argparse.ArgumentParser(description='Videos to images')
# parser.add_argument('indir', type=str, help='Input dir for videos')
# parser.add_argument('outdir', type=str, help='Output dir for image')
# args = parser.parse_args()
# print(args.indir)
    
SET = ['definitions', 'examples']
    
t = '  '
tt = t*2
ttt = t*3   
    
def format(word):
    res = define(word=word, dictionary_type="english")
    
    # if didn't find in cambridge dictionary
    if not res:
        print(f'{Fore.light_magenta}Sorry {Fore.red}(-_-){Fore.light_magenta}. There is no definition of this word in CambridgeDict!!{Style.reset}')
        # print(f'{Fore.light_blue}Background color {Back.black} yellow with red text!{Style.reset}')
        return True
    
    res_key = list(res[0].keys())
    print(res_key)
    ### possible to add key
    for key in res_key:
        print('key is ', key)
        if len(key) > len(word):
            continue
        cout = ''
        cout += key+'\n'
        pprint(res)
        for ind in res[0][key]:
            if not ind['POS'] or not ind['data'][SET[0]]: 
                res[0].pop(key) # !!!
                continue
            cout += t + colored(ind['POS'][0], 'green') + ':\n'
            tmpl = 'A'
            for elem in range(len(ind['data'][SET[0]])):
                for set in SET:
                    cout += tt + f'{Fore.light_magenta}' + set + f'{Style.reset}:\n'
                    if type(ind['data'][set][elem]) is list:
                        tmp = 0
                        for deff_exmp in ind['data'][set][elem]:
                            tmp += 1
                            cout += ttt + f' {tmp}. '+ deff_exmp + '\n'
                    else: cout += ttt + f'{tmpl}) ' + ind['data'][set][elem] + '\n'
                tmpl = chr(ord(tmpl) + 1)
                cout += colored('-'*60, 'blue') + '\n'
        print(cout)

    return None if not res else res

def format_arg(res, args):
    
    res_key = list(res[0].keys())
    name = None
    for key in res_key:
        if len(key) > len(args[0]):
            continue
        elif key.lower() == args[0]:
            name = key
        elif len(res[0]) == 1: 
            name = list(res[0].keys())[0]
        else:
            return None
    
    speech_part = args[1]
    # res[0][name][speech_part] need to be fixed
    # print(ord(args[2].lower()) - ord('a'), ord(args[3].lower()) - 1)
    # pprint(res)
    for ind in res[0][name]:
        if speech_part == ind['POS'][0]:
            touch = res[0][name].index(ind)
            definition = res[0][name][touch]['data'][SET[0]][ord(args[2].lower()) - ord('a')]
            example = res[0][name][touch]['data'][SET[1]][ord(args[2].lower()) - ord('a')][ord(args[3].lower()) - ord('1')]
            return (name, speech_part, definition, example)



    

# format('by')