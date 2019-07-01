## 实现图像的模糊检测，评价清晰度的好坏



需要的环境：

1.python3.6

2.opencv-python           

### 文件作用

       blurry_image_generation.py 为使用四种模糊算法对原图进行模糊操作。
       clarity_assessment.py  为9种评价方法的函数
       image_median  image_gaussian  image_bilateral  image_average 为使用四种模糊算法生成的图像样本的目录

#### 实验结果：

一共使用了九种评价方法，下面是针对同一张图片的两种不同分辨率的样本进行的实验结果
（得分越高，清晰度越高）
1. Brenner	  

              (84726910, 10552505)                  #原始得分
              (1.0, 0.1245)                         #等比例化后的得分
              2.772712 s                            #every image cost
2. Laplacian  

              (37.1888,2.0921)                      #原始得分
              (1.0, 0.0562)                         #等比例化后的得分
              0.554030 s                            #every image cost
3. SMD        

              (11405048.0, 3470877.0)               #原始得分
              (1.0, 0.30432)                        #等比例化后的得分
              13.20454 s                            #every image cost
4. SMD2       

              (19564461.0, 1976470.0)               #原始得分             
              (1.0, 0.1010)                         #等比例化后的得分
              11.77434 s                            #every image cost
5. Variance   

              (8977334575.8, 8736350299.2)          #原始得分
              (1.0, 0.9731)                         #等比例化后的得分
              9.117599 s                            #every image cost
6. Energy     

              (1681422695, 18463550)                #原始得分
              (1.0, 0.0109)                         #等比例化后的得分
              12.48029 s                            #every image cost
7. Vollath    

              (8928907811.8, 8699682511.2)          #原始得分
              (1.0, 0.9743)                         #等比例化后的得分
              2.625977 s                            #every image cost
8. Entropy    

              (7.7165, 7.6773)                      #原始得分
              (1.0, 0.9949)                         #等比例化后的得分
              0.004246 s                            #every image cost
9. Tenengrad  

              (52.5125, 20.1666)                    #原始得分
              (1.0, 0.3840)                         #等比例化后的得分
              1.434391 s                            #every image cost
              
##### 得出的结论是：  

Brenner  Laplacian  SMD   SMD2   Energy   Tenengrad 表现得比较理想  
Variance Vollath  Entropy 表现得不尽人意





