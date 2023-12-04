#!/usr/bin/python3
import Ice 
Ice.loadSlice('cristian.ice')
import ssdd
import time

comunicador = Ice.initialize()

proxy_cristian_str='Cristian -t -e 1.1:tcp -h 192.168.8.224 -p 4080 -t 60000'
proxy_cristian=comunicador.stringToProxy(proxy_cristian_str)
cristian=ssdd.CristianPrx.checkedCast(proxy_cristian)

proxy_report_str='SyncReport -t -e 1.1:tcp -h 192.168.8.224 -p 4080 -t 60000'
proxy_report=comunicador.stringToProxy(proxy_report_str)
report=ssdd.SyncReportPrx.checkedCast(proxy_report)

t1=time.time()
tiempo_servidor=cristian.getServerTime('04864501R', t1)
print('El tiempo del servidor es: ', tiempo_servidor)
t2=time.time()

T=tiempo_servidor+(t2-t1)/2

error=(t2-t1)/2
print('El error es: ', error)
report.notifyTime('04864501R', 'oscar gomez toledano',t2, T, error)

comunicador.destroy()