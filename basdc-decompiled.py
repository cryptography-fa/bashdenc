# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16 (default, Jul  7 2019, 21:05:54)
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <script>
# Compiled at: 2019-08-09 12:08:42
import os
import sys
import time
 
p   = '\x1b[0m'
m   = '\x1b[91m'
h   = '\x1b[92m'
k   = '\x1b[93m'
b   = '\x1b[94m'
u   = '\x1b[95m'
bm  = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'
log = '\n    %s\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n       %sAuthor %s  : %sSazXt\n       %scodeName %s: %sBashDencript\n     %s\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\n' % (p, h, k, p, h, k, p, p)
 
try:
    os.system('reset')
    print log
    bx = raw_input('%s[%s\xe2\x9d\x97%s] %sFile %s: %s' % (b, m, b, p, k, h))
    ob_ = open(bx).read().replace('eval', 'echo')
    _res = open('un.sh', 'w')
    _res.write(ob_)
    _res.close()
    reb_ = bx.replace('.sh', '_denc.sh')
    os.system('sh un.sh > ' + reb_)
    _vew = open(reb_).read()
    _edAu = open(reb_, 'w')
    _edAu.write('#Dencript By SazXt\n#https://github.com/Sazxt\n' + _vew)
    _edAu.close()
    if 'echo' in _vew:
        os.system('sh ' + reb_ + ' > ok.sh')
        dc_ = open('ok.sh').read()
        uc_ve = open(reb_, 'w')
        uc_ve.write(dc_ + '\n#Dencript By SazXt\n#https://github.com/Sazxt')
        uc_ve.close()
        os.system('rm ok.sh')
    os.system('rm un.sh')
    print '%s[%s\xe2\x9d\x97%s] %sBerhasil Mengirim Percobaan ke %s' % (b, m, b, p, h) + reb_
except IOError:
    print '%s[%s\xe2\x9d\x97%s] %sFile Tidak Di Temukan !' % (b, m, b, p)
except:
    print '%s[%s\xe2\x9d\x97%s] %sExit..' % (b, m, b, p)
