import random
#import os
import subprocess
fn = 'randSamp.htm'
d = int(input('#Input a number:'))
dd = d*d
r = []
r = random.sample(range(dd), dd)
# print(r,sum(r),end='\n\n')
f = open(fn, 'w')
f.write('<html>')
f.write('<style>.odd{background-color:#cdc;} table{border-collapse: collapse;} td{text-align:center;} td:hover{background-color:yellow;}</style>')
f.write('<script>  function clik(obj){  obj.style.backgroundColor="red"; }</script>')
f.write('<body><table border=1 width="100%" height="100%">')
for i in range(1, dd+1):
    if i%d == 1:
        f.write('<tr>')
    if r[i-1] % 2:
        f.write('<td class=odd>%d' % r[i-1] + '</td>')
    else:
        f.write('<td onClick="clik(this)">%d' % r[i-1] + '</td>')
    print('%4d' % r[i-1], end='')
    if i % d == 0:
        f.write('</tr>')
        print()
f.write('</table></body></html>')
f.close()
#os.system(fn)
subprocess.call(fn, shell=True)
