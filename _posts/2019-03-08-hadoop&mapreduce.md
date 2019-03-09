---
layout:     post
title:      "What is Hadoop?"
subtitle:   " \"From Google Cloud to Hadoop\""
date:       2019-03-08 23:38:00
author:     "Leo"
header-img: "img/post-bg-mapreduce.jpg"
tags:
    - Hadoop
    - Big Data
---

> From the beginning to the end.

## Hadoop是Google的云计算系统的Java开源实现，是一种分布式系统的平台，通过它可以很轻松的搭建一个高效、高质量的分布式系统。

谷歌集群系统主要包括三个部分（所谓的Google三驾马车）：

* 分布式文件系统GFS
 The Google File System发表于SOSP 19(Symposium on Operating Systems Principles)，2003，介绍了用于大型的、分布式的、对大量数据进行访问的可扩展的分布式文件系统——GFS，它运行于廉价的普通硬件上，提供容错功能。

* 分布式并行编程计算模型MapReduce
 MapReduce: simplified data processing on large clusters发表于OSDI 06(Operating Systems Design and Implementation)， 2004，介绍了针对分布式并行计算的一套编程模型MapReduce。

* 分布式数据库(存储系统)Bigtable
 Bigtable: A Distributed Storage System for Structured Data发表于OSDI 07， 2006，分析了设计用于处理海量数据的分布式结构化数据存储系统BigTable的工作原理。

**当前流行的大数据技术都是在这三篇论文基础上发展起来的，典型的就是Apache开源的Hadoop和Hbase。通常我们所理解的狭义Hadoop由HDFS和MapReduce两部分构成，两者缺一不可，也就是说可以通过MapReduce很容易在Hadoop平台上进行分布式计算编程。**

* 分布式文件系统HDFS：类似于FAT32，NTFS，是一种文件格式，是底层的。

* 编程模型MapReduce

* 分布式存储系统Hbase：适合于非结构化数据存储的数据库

详细为什么要进行分布式文件系统和计算设计见[[5]](https://blog.51cto.com/kmzsq/1683118)


[1] https://www.meipian.cn/bpt63y5
[2] https://blog.csdn.net/a6jishuren/article/details/81450283
[3] https://zhidao.baidu.com/question/323886705.html
[4] https://zhidao.baidu.com/question/387588585.html
[5] [hadoop分布式存储&&分布式计算](https://blog.51cto.com/kmzsq/1683118)