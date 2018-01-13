# Py3.5_xiciIP_spider
对xici代理公开的ip地址进行抓取并验证有效性存入数据库

数据库创建如下：
CREATE TABLE `xiciip` (
`ip`  varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
`place`  varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
`protocol`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
PRIMARY KEY (`ip`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
ROW_FORMAT=DYNAMIC
;


有问题欢迎前往我的博客与我交流，博客地址：http://blog.csdn.net/wy_97/article/details/79054599
