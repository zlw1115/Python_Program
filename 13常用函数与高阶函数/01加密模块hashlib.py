'''
hashlib模块
难破解 不可逆
函数名     参数      介绍              举例                      返回值
md5     byte        Md5算法加密        hashlib.md5(b' hello')   Hash对象
sha1    byte        Sha1算法加密        hashlib.sha1(b' hello') Hash对象
sha256  byte        Sha256算法加密        hashlib.sha256(b' hello') Hash对象
sha512  byte        Sha512算法加密        hashlib.sha512(b' hello') Hash对象
    数值越高，加密后，被破解的概率越低

'''
import hashlib
import time

base_sign = 'muke'
def custom():
    a_timestamp = int(time.time())
    _token = '%s%s' % (base_sign,a_timestamp)
    hashobj = hashlib.sha1(_token.encode('utf-8'))
    # 十六进制加密串
    a_token = hashobj.hexdigest()
    return a_token,a_timestamp

def b_service_check(token,timestamp):
    _token = '%s%s' % (base_sign,timestamp)
    b_token = hashlib.sha1(_token.encode('utf-8')).hexdigest()
    if b_token == token:
        return True
    else:
        return False


if __name__ == '__main__':
    need_help_token,timestamp = custom()
    # print(need_help_token,timestamp)
    result = b_service_check(need_help_token,timestamp)
    print(result)