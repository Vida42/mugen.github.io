---
layout:     post
title:      "How to use Spark?"
subtitle:   " \"Take it easy.\""
date:       2019-03-09 00:12:00
author:     "Mugen"
header-img: "img/post-bg-spark.jpg"
tags:
    - Spark
    - Big Data
---

> 心急吃不了热豆腐

### 原来学使用也可以从入门到放弃

第一步在看：

[A Gentle Introduction to Apache Spark on Databricks](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/4999972933037924/3726004726361689/8135547933712821/latest.html)

哇，好长不看，去了下一个链接：

[Spark ALS algorithm ML Based](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/4999972933037924/899848065201823/8135547933712821/latest.html)

直接又是扔给我一堆代码……

在了解啥是ALS之前先看看RDD的API吧……

[Collaborative Filtering - RDD-based API](https://spark.apache.org/docs/2.1.1/mllib-collaborative-filtering.html)

文字看得懂，代码就懵逼或者说是不想看。

里面提到的ALS(Alternating Least Squares)算法是协同过滤的一种，基于矩阵分解的办法。

其给出了论文名：Matrix Factorization Techniques for Recommender Systems

搜了下正是2009 Netflix Prize得主的论文，被写进Spark的MLLib库了呀。

然后得到三个链接，是讲这个算法的：

[ALS（Alternating Least Squares）](https://blog.csdn.net/qq_33626989/article/details/82011481)
[论文篇：Matrix Factorization Techniques for RS](https://zhuanlan.zhihu.com/p/28577447?group_id=881547532893851649)
[矩阵分解（MATRIX FACTORIZATION）在推荐系统中的应用](https://blog.csdn.net/lissanwen/article/details/51214275)

第二篇图文并茂的知乎专栏应该不错。原论文也下载了是彩色的耶。就都先不看了先把例子跑起来。

哦对，在看5230讲推荐系统没的途中看到课程推荐用书[Mining of Massive Datasets](http://www.mmds.org/#book)，在YouTube还有位staford??的印度老师在讲这门课。在线MOOC貌似要本校生？算了先不研究了跑偏了……


回到上面的[Collaborative Filtering - RDD-based API](https://spark.apache.org/docs/2.1.1/mllib-collaborative-filtering.html)，其中的Tutorial是a hands-on tutorial for personalized movie recommendation with spark.mllib.，但是链接打不开。找到一个AMPCamp的版本hands-on如下：[Movie Recommendation with MLlib](http://ampcamp.berkeley.edu/5/exercises/movie-recommendation-with-mllib.html)，想着要么从这个作业做起？？回Introduction，啧，要装spark并且还要有Java……

于是问题就回到了到底怎么用Spark?

how to install spark?

I need to have java installed?

then I searched a lot:

[天下也有免费的午餐 - 带你玩转免安装免配置 还免费的Spark 集群](https://www.flyml.net/2016/08/19/learn-spark-free-online/)

### 什么是databricks Community版？

相当于给你了一个在线spark集群，即：learn-spark-free-online。我等尚处spark初级阶段的小白们刚好可以用他们提供的免费版来学习，省去了搭建和维护配置的过程，用来学习或温习Spark API真是完美!

> [md集群(cluster)是啥](https://www.zhihu.com/question/20004877/answer/282033178)？
> 
> 有多台服务器提供相同的服务，每台服务器叫做一个节点，这些节点就构成了一个集群。


还有一份[简明Spark使用指南](http://www.voidcn.com/article/p-oyyjfixg-brm.html)，提到：**Apache Spark网站为所有api提供了一套良好的文档，并且Databricks网站使用各种技术和数据集提供了大量文档和非常有用的教程。多练习并实践!**

这时想起官网教程的好了，兜兜转转的还是得回来看官网教程。又是粗略一翻好长就不想看又右倾投降主义了哈哈……

&，很奇怪百度文库怎么会有这种教程：[databricks基本操作介绍](https://wenku.baidu.com/view/b9ff3a062379168884868762caaedd3383c4b517.html)

