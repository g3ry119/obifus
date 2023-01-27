import random
import string
import zlib
import base64

class damon:
    def grand():
        return ''.join(random.choices(string.ascii_letters, k=40))

    sector_01, sector_02, sector_03, sector_04, sector_05, sector_06, sector_07 = grand(), grand(), grand(), grand(), grand(), grand(), grand()
    class compontents:
        def split_string(string, pieces):
            return [string[i:i+len(string)//pieces] for i in range(0, len(string), len(string)//pieces)]

        def hexescstr(string):
            return ''.join(f'\\x{ord(c):02x}' for c in string)

        def toHex(content):            
            ncon = content.encode().hex().translate(str.maketrans('abcdef0123456789', 'mnopqxiljfy;:,./'))
            return f"{damon.sector_04}=eval('{damon.compontents.hexescstr('eval')}');{damon.sector_07},{damon.sector_06},{damon.sector_05},{damon.sector_02},{damon.sector_03}={damon.sector_04}('{damon.compontents.hexescstr('bytes.decode')}'),{damon.sector_04}('{damon.compontents.hexescstr('str.translate')}'),{damon.sector_04}('{damon.compontents.hexescstr('str.maketrans')}'),{damon.sector_04}('{damon.compontents.hexescstr('exec')}'),{damon.sector_04}('{damon.compontents.hexescstr('bytes.fromhex')}');(lambda {damon.sector_01}:{damon.sector_02}({damon.sector_07}({damon.sector_03}({damon.sector_01}))))({damon.sector_06}('{ncon}',{damon.sector_05}('{damon.compontents.hexescstr('mnopqxiljfy;:,./')}','{damon.compontents.hexescstr('abcdef0123456789')}')))"

        def compress(content):
            this_sector = [damon.grand(), damon.grand(), damon.grand(), damon.grand(), damon.grand(), damon.grand(), damon.grand()]
            return f"import zlib as {this_sector[0]}; {this_sector[1]} = {this_sector[0]}.decompress; {this_sector[2]}=eval('{damon.compontents.hexescstr('exec')}');{this_sector[0]}={this_sector[0]};{this_sector[3]}={this_sector[1]};{this_sector[0]}={this_sector[2]};{this_sector[0]}({this_sector[3]}({str(zlib.compress(content.encode()))}))"

        def base64(content):
            return f"__import__('builtins').exec(__import__('builtins').compile(__import__('base64').b64decode(\"{base64.b64encode(content.encode()).decode()}\"),'<string>','exec'))"

    def obfuscate(code):
        stage1 = damon.compontents.toHex(code)
        damon.sector_01, damon.sector_02, damon.sector_03, damon.sector_04, damon.sector_05, damon.sector_06, damon.sector_07 = damon.grand(), damon.grand(), damon.grand(), damon.grand(), damon.grand(), damon.grand(), damon.grand()
        stage2 = damon.compontents.toHex("[print('',end='',flush=True) for _ in range(10)];"*6) +";"+ stage1+";"
        damon.sector_01, damon.sector_02, damon.sector_03, damon.sector_04, damon.sector_05, damon.sector_06, damon.sector_07 = damon.grand(), damon.grand(), damon.grand(), damon.grand(), damon.grand(), damon.grand(), damon.grand()
        stage2 += damon.compontents.toHex("[print('',end='',flush=True) for _ in range(10)];"*10)
        damon.sector_01, damon.sector_02, damon.sector_03, damon.sector_04, damon.sector_05, damon.sector_06, damon.sector_07 = damon.grand(), damon.grand(), damon.grand(), damon.grand(), damon.grand(), damon.grand(), damon.grand()
    
        stage3 = damon.compontents.compress(stage2)
        stage3 = damon.compontents.base64(stage3)

        return stage3

code = """
print("Hello, World!")
"""

print(damon.obfuscate(code))