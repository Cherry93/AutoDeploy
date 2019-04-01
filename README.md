# AutoDeploy
自动化部署系统

### 涉及技术

技术|功能说明
----|------|
flask|python的web开发框架  
sqlAlchemy|python的orm框架      
mysql-connector-python|python连接mysql的驱动
logging|日志库
rsync|机器间同步文件
sshpass|可以明文密码连接另一台机器


#### 项目介绍

* AutoDeploy是一个针对于基于Maven的SpringBoot项目的部署和发布系统．
* 基于python语言开发,采用B/S架构
* 部署分为两步,第一步是分支的检出和确定发布项目的版本,第二步是项目的打包和传输到目标主机
* 发布实际上是通过连接远程主机,启动项目
