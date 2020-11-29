---
layout:     post
title:      "Setting Personal Domain"
subtitle:   " \"with Tencent Cloud\""
date:       2019-10-09 14:57:00
author:     "Mugen"
header-img: "img/post-bg-tccloud.jpg"
tags:
    - Kit
    - Knowledge
---

> It took less time than expected.


昨晚23：30吧，开始在腾讯云购买域名。新用户享受免费SSL证书+免费域名解析+备案领礼包。还有.com域名新用户特惠价23元首年。

这里面的优惠：

* SSL证书最后被证明不需要，因为github从18年5月开始自定义域名也可以支持HTTPS

* 免费域名解析（没这个活动腾讯也有免费解析[[6](https://cloud.tencent.com/product/cns)]……）

* 备案领礼包不需要，因为备案的网站主要是指在中国大陆开展网站服务的网站，由于我们使用的是国外的服务器，所以暂时是不需要备案的。但是依旧要注意网页的使用，避免非法信息的传播[[1]()]。

用微信注册后需要实名认证，用微信付0.01即可。之后买域名，再付22.99。等待3-5分钟后审核通过，接下来需要对注册的域名进行实名认证，填姓名联系方式住址上传身份证。完成后通知为“预计在3-5个工作日内完成审核”，实际几分钟即可通过。通过后可以开始解析。

按他人[[1](https://blog.csdn.net/u012348774/article/details/79577333)],[[2](https://segmentfault.com/a/1190000011203711)]步骤操作。因A配置记录值是IP而github.io的IP可能会改变，所以统一使用`CNAME`配置解析。

在腾讯云[我的域名](https://console.cloud.tencent.com/domain)内添加两条解析。之后需要等数十分钟生效。

![如图](/img/in-post/personal-domain.png)

GIthub方面需在`github pages`的仓库根目录里加上`CNAME`文件，在内写上域名（无需http头和www）。或者在`github pages`的仓库`Settings`直接设置`Custom domain`为自己的域名。

这个时候已经实现了http访问。

接下来由于想使用https访问，购买前提示新用户有免费SSL证书，就去看了下（每次想找到域名或SSL只能找到订单这个入口…），然而点击资源ID后，控制台跳到证书管理模块，里面并没有证书记录。看到上面有免费申请证书，又申请了，原来本就存在可免费申请的证书…注意密钥要保存好，丢了只能重新申请。今早状态变为已颁发，然后下载，按照证书安装指引，使用IIS 服务器证书安装。

可是安装后出问题了，使用HTTPS访问显示not secured，点击查看证书显示是www.github.com的。换用edge亦如此。这时搜了好多，大概原因是：

> 自定义域名如果没有使用第三方 CDN + 为你的域名申请的证书配合 GitHub Pages 使用的话，不要使用 https 访问，因为默认是使用的 www.github.com 的证书，与你的域名不匹配自然就会报证书错误了[3]。

由于年代久远作者懒得配置了但我得配置啊……查了小半个上午有好多方法，尝试了半天改DNS后来看到说如果是用的不是`A`配置不需要改DNS，会自动配置好。尝试这个之前github点不了`Enforce Https`，提示`Not yet available for your site because the certificate has not finished being issued`。删除CNAME文件后立刻再写域名，可以强制转了，但是https是not secured的呀。从[5]里的个人证书从github.com变为个人域名得到一些灵感。在知道和DNS无关后，又在`Custom domain`删了域名，等了几分钟，再写上，再enforce。这时已经把IIS里的https证书删了。但是还是不安全，又在搜了一些网页后试了下edge，可以了，小灰锁，显示证书已颁给个人域名。然后这时删除了24h内的chrome的cookie等，再试，可以了。


[1] [Github博客+腾讯云域名](https://blog.csdn.net/u012348774/article/details/79577333)

[2] [Github pages 绑定个人域名](https://segmentfault.com/a/1190000011203711)

[3] [GitPage配置自定义域名后提示证书错误](https://github.com/mzlogin/mzlogin.github.io/issues/6)

[4] [A配置下GitHub Pages添加HTTPS](https://poplite.xyz/post/2018/05/03/how-to-enable-https-for-custom-domain-on-github-pages.html)

[5] [Github Pages绑定自定义域名并开启https最新方法(2018/5/8已解决)](https://www.4spaces.org/how-to-enable-https-support-on-custom-domains/)

[6] [DNS解析 DNSPod](https://cloud.tencent.com/product/cns)