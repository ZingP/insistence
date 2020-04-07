# psutil
In [1]: import psutil                                                       

## 获取CPU信息
In [2]: psutil.cpu_count()                 # CPU逻辑数量                                               
Out[2]: 8

In [3]: psutil.cpu_count(logical=False)    # CPU物理核心                                   
Out[3]: 4

In [4]: psutil.cpu_times()                 # 统计CPU的用户／系统／空闲时间                                             
Out[4]: scputimes(user=830519.73, nice=0.0, system=723038.84, idle=42315894.17)

- 实现类似top命令的CPU使用率，每秒刷新一次，累计10次
In [6]: for x in range(10): 
   ...:     r = psutil.cpu_percent(interval=1, percpu=True) 
   ...:     print(r) 
   ...:                                                                         
[19.0, 0.0, 12.7, 1.0, 8.0, 1.0, 4.0, 1.0]
[20.0, 0.0, 12.1, 0.0, 8.0, 0.0, 4.0, 1.0]
[32.0, 5.0, 23.0, 4.0, 19.0, 4.0, 16.0, 2.0]
[20.0, 0.0, 15.0, 0.0, 7.1, 0.0, 5.9, 2.0]
[24.8, 1.0, 14.9, 1.0, 9.0, 1.0, 8.1, 0.0]
[34.0, 4.0, 27.0, 4.0, 24.8, 4.0, 17.8, 5.0]
[28.7, 2.0, 20.0, 1.0, 13.0, 2.0, 11.0, 1.0]
[21.0, 1.0, 15.8, 1.0, 10.9, 0.0, 6.9, 1.0]
[22.0, 0.0, 14.9, 0.0, 9.0, 0.0, 7.0, 0.0]
[25.0, 2.0, 15.2, 1.0, 11.0, 1.0, 5.0, 0.0]


## 获取内存信息
In [7]: psutil.virtual_memory()           # 获取物理内存信息                                          
Out[7]: svmem(total=17179869184, available=5688819712, percent=66.9, used=9728593920, free=159133696, active=5531738112, inactive=5306654720, wired=4196855808)

In [8]: psutil.swap_memory()              # 获取交换内存信息                                        
Out[8]: sswap(total=5368709120, used=4316463104, free=1052246016, percent=80.4, sin=659438723072, sout=4277862400)
- 注意： 返回的是字节为单位的整数。 总内存17179869184/1024/1024/1024 = 16.0 G。


## 获取磁盘信息
In [9]: psutil.disk_partitions()          # 磁盘分区信息                             
Out[9]: 
[sdiskpart(device='/dev/disk1s1', mountpoint='/', fstype='apfs', opts='rw,local,rootfs,dovolfs,journaled,multilabel'),
 sdiskpart(device='/dev/disk1s4', mountpoint='/private/var/vm', fstype='apfs', opts='rw,noexec,local,dovolfs,dontbrowse,journaled,multilabel,noatime')]
- 有两个分区，磁盘格式apfs，opts中journaled表示支持日志。

In [10]: psutil.disk_usage('/')           # 磁盘使用情况                             
Out[10]: sdiskusage(total=250685575168, used=118098038784, free=125440405504, percent=48.5)
- 磁盘总共250685575168/1024/1024/1024233.469G，已使用48.5%。

In [11]: psutil.disk_io_counters()        # 磁盘IO                                 
Out[11]: sdiskio(read_count=55081907, write_count=65301593, read_bytes=996595785728, write_bytes=1063386177536, read_time=18258582, write_time=10621452)


## 获取网络信息
In [12]: psutil.net_io_counters()         # 获取网络读写字节／包的个数              
Out[12]: snetio(bytes_sent=80803235840, bytes_recv=124806110208, packets_sent=254195219, packets_recv=182450714, errin=0, errout=130782, dropin=0, dropout=0)

In [13]: psutil.net_if_addrs()            # 获取网络接口信息

In [14]: psutil.net_if_stats()            # 获取网络接口状态

In [15]: psutil.net_connections()         # 获取当前网络连接信息


## 获取进程信息
In [16]: psutil.pids()                    # 所有进程ID                                         
Out[16]: [0,1,39,40, ...]

In [17]: import os                                                          

In [18]: os.getpid()                                                        
Out[18]: 70042

In [19]: p = psutil.Process(os.getpid())  # 获取指定进程                                  

In [20]: p.name()         # 进程名称                                                
Out[20]: 'python3.7'

In [21]: p.exe()          # 进程exe路径                                              
Out[21]: '/opt/anaconda3/bin/python3.7'

In [22]: p.cwd()          # 进程工作目录                                             
Out[22]: '/Users/liuyouyuan/workspace/pyproject/scripts'

In [23]: p.cmdline()      # 进程启动的命令行                                     
Out[23]: ['/opt/anaconda3/bin/python', '/opt/anaconda3/bin/ipython']

In [24]: p.ppid()         # 父进程ID                                                
Out[24]: 46810

In [25]: p.parent()       # 父进程                                                
Out[25]: psutil.Process(pid=46810, name='zsh', started='2020-03-30 15:24:07')

In [26]: p.children()     # 子进程列表                                          
Out[26]: []

In [27]: p.status()       # 进程状态                                              
Out[27]: 'running'

In [28]: p.username()     # 进程用户名                                          
Out[28]: 'liuyouyuan'

In [29]: p.create_time()  # 进程创建时间                                     
Out[29]: 1586241277.044256

In [30]: p.terminal()     # 进程终端                                            
Out[30]: '/dev/ttys003'

In [31]: p.cpu_times()    # 进程使用的CPU时间                                  
Out[31]: pcputimes(user=3.119619328, system=0.63911072, children_user=0.0, children_system=0.0)

In [32]: p.memory_info()  # 进程使用的内存                                   
Out[32]: pmem(rss=73498624, vms=4479959040, pfaults=28482, pageins=185)

In [33]: p.open_files()   # 进程打开的文件                                    
Out[33]: 
[popenfile(path='/Applications/Visual Studio Code.app/Contents/Resources/electron.asar', fd=26),
 popenfile(path='/Applications/Visual Studio Code.app/Contents/Resources/app/node_modules.asar', fd=28),
 popenfile(path='/System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/HIToolbox.framework/Versions/A/Resources/English.lproj/Localized.rsrc', fd=33)]

In [34]: p.connections()  # 进程相关网络连接                                 
Out[34]: []

In [35]: p.num_threads()  # 进程的线程数量                                   
Out[35]: 6

In [36]: p.threads()      # 所有线程信息                                         
Out[36]: 
[pthread(id=1, user_time=3.008698, system_time=0.4743),
 pthread(id=2, user_time=0.008189, system_time=0.028232),
 pthread(id=3, user_time=3.7e-05, system_time=2.4e-05),
 pthread(id=4, user_time=3.8e-05, system_time=2.5e-05),
 pthread(id=5, user_time=3.3e-05, system_time=1.6e-05),
 pthread(id=6, user_time=2e-05, system_time=1.7e-05)]

In [37]: p.environ()      # 进程环境变量                                         
Out[37]: 
{'TMPDIR': '/var/folders/ys/hf5c1mt91qgdq3r803d6qdq80000gn/T/',
 '__CF_USER_TEXT_ENCODING': '0x1F5:0x19:0x34',
 'SHELL': '/bin/zsh',
 ...
 '_': '/opt/anaconda3/bin/ipython'}

In [38]: p.terminate()    # 结束进程                                           
[1]    70042 terminated  ipython
(base) 

