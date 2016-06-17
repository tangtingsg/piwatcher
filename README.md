### 树莓派python端安装：
##### 1、进入用户目录
打开终端，输入命令
```sh
echo $HOME
```
输出应该为/home/pi 。若不是，创建目录
```sh
mkdir /home/pi
```
进入用户目录
```sh
cd /home/pi
```
##### 2、下载PiWatcher程序
使用git下载程序
```sh
git clone https://github.com/tangtingsg/piwatcher
```
打印当前目录，输出中应该有piwatcher文件夹  
```sh
ls
```
##### 3、安装运行
进入程序目录
```sh
cd piwatcher
```
安装运行
```sh
sudo python3 install.py
```
等待安装完成。查看后台服务状态
```sh
sudo python3 piwatcher.py status
```
应该看到两个正常的绿色服务。此时程序已经正常启动，开机会自启动 
##### 4、访问网页
树莓派同一局域网内访问 **[树莓派ip]:8080** 即可打开二维码网页，如[192.168.0.103:8080](http://192.168.0.103:8080 "树莓派")  
树莓派ip可通过ifconfig命令查看
```sh
ifconfig
```
##### 5、其他操作（均需在程序文件夹中运行终端命令）
- 停止服务：```sudo python3 piwatcher.py stop ```
- 运行服务：```sudo python3 piwatcher.py start ```
- 重启服务：```sudo python3 piwatcher.py restart ```
- 查看服务：```sudo python3 piwatcher.py status ```

##### 6、后续更新程序
停止后台服务
```sh
sudo python3 piwatcher.py stop
```
进入用户目录
```sh
cd /home/pi
```
删除安装文件
```sh
sudo rm piwatcher -rf
```
重新下载安装
```sh
git clone https://github.com/tangtingsg/piwatcher
cd piwatcher
sudo python3 install.py
```
