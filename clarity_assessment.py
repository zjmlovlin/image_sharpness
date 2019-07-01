import cv2
import numpy as np
import math
import time
from skimage import filters
def brenner(img):
    '''
    :param img:narray             the clearer the image,the larger the return value
    :return: float 
    '''
    shape = np.shape(img)
    
    out = 0
    for y in range(0, shape[1]):
        for x in range(0, shape[0]-2):
            
            out+=(int(img[x+2,y])-int(img[x,y]))**2
            
    return out

def Laplacian(img):
    
    return cv2.Laplacian(img,cv2.CV_64F).var()

def SMD(img):
    
    shape = np.shape(img)
    out = 0
    for y in range(0, shape[1]-1):
        for x in range(0, shape[0]-1):
            out+=math.fabs(int(img[x,y])-int(img[x,y-1]))
            out+=math.fabs(int(img[x,y]-int(img[x+1,y])))
    return out

def SMD2(img):
    
    shape = np.shape(img)
    out = 0
    for y in range(0, shape[1]-1):
        for x in range(0, shape[0]-1):
            out+=math.fabs(int(img[x,y])-int(img[x+1,y]))*math.fabs(int(img[x,y]-int(img[x,y+1])))
    return out

def variance(img):
    
    out = 0
    u = np.mean(img)
    shape = np.shape(img)
    for y in range(0,shape[1]):
        for x in range(0,shape[0]):
            out+=(img[x,y]-u)**2
    return out

def energy(img):
 
    shape = np.shape(img)
    out = 0
    for y in range(0, shape[1]-1):
        for x in range(0, shape[0]-1):
            out+=((int(img[x+1,y])-int(img[x,y]))**2)*((int(img[x,y+1]-int(img[x,y])))**2)
    return out

def Vollath(img):
  
    
    shape = np.shape(img)
    u = np.mean(img)
    out = -shape[0]*shape[1]*(u**2)
    for y in range(0, shape[1]):
        for x in range(0, shape[0]-1):
            out+=int(img[x,y])*int(img[x+1,y])
    return out

def entropy(img):

    [rows, cols] = img.shape
    h = 0
    hist_gray = cv2.calcHist([img],[0],None,[256],[0.0,255.0])
    # hn valueis not correct
    hb = np.zeros((256, 1), np.float32)
    #hn = np.zeros((256, 1), np.float32)
    for j in range(0, 256):
        hb[j, 0] = hist_gray[j, 0] / (rows*cols)
    for i in range(0, 256):
        if hb[i, 0] > 0:
            h = h - (hb[i, 0])*math.log(hb[i, 0],2)
                
    out = h
    return out
    """
    tmp = []
    for i in range(256):
        tmp.append(0)
    val = 0
    k = 0
    out = 0
    
    img = np.array(img)
    for i in range(len(img)):
        for j in range(len(img[i])):
            val = img[i][j]
            tmp[val] = float(tmp[val] + 1)
            k =  float(k + 1)
    for i in range(len(tmp)):
        tmp[i] = float(tmp[i] / k)
    for i in range(len(tmp)):
        if(tmp[i] == 0):
            out = out
        else:
            out = float(out - tmp[i] * (math.log(tmp[i]) / math.log(2.0)))
    return out
    """
def Tenengrad(img):
    tmp = filters.sobel(img)
    out = np.sum(tmp**2)
    out = np.sqrt(out)
    return out
  
def main(img1, img2):
    l = []
    time1 = []
    for i in range(9):
        l.append([])
    start = time.clock()
    l[0].append(brenner(img1))
    l[0].append(brenner(img2))
    end = time.clock()
    time1.append(end-start)
    start = time.clock()  
    l[1].append(Laplacian(img1))
    l[1].append(Laplacian(img2))
    end = time.clock()
    time1.append(end-start)
    start = time.clock()
    l[2].append(SMD(img1))
    l[2].append(SMD(img2))
    end = time.clock()
    time1.append(end-start)
    start = time.clock()
    l[3].append(SMD2(img1))
    l[3].append(SMD2(img2))
    end = time.clock()
    time1.append(end-start)
    start = time.clock()
    l[4].append(variance(img1))
    l[4].append(variance(img2))
    end = time.clock()
    time1.append(end-start)
    start = time.clock() 
    l[5].append(energy(img1))
    l[5].append(energy(img2))
    end = time.clock()
    time1.append(end-start)
    start = time.clock()
    l[6].append(Vollath(img1))
    l[6].append(Vollath(img2))
    end = time.clock()
    time1.append(end-start)
    start = time.clock()
    l[7].append(entropy(img1))
    l[7].append(entropy(img2))
    end = time.clock()
    time1.append(end-start)
    start = time.clock()
    l[8].append(Tenengrad(img1))
    l[8].append(Tenengrad(img2))
    end = time.clock()
    time1.append(end-start)
    l_method=['Brenner', 'Laplacian', 'SMD', 'SMD2', 'Variance', 'Energy', 'Vollath', 'Entropy', 'Tenengrad']
    for i in range(9):
        print('---------------------------')
        print (l_method[i])     #method name
        print(l[i][0],l[i][1])     # original value
        print(float(l[i][0])/float(np.max(l[i])),float(l[i][1])/float(np.max(l[i])))   #original value/max value
        print('every image cost %f s'%time1[i])
        
if __name__ == '__main__':
    #original image
    img1 = cv2.imread('./image_average/image1.jpeg')
    img2 = cv2.imread('./image_average/image5.jpeg')
    #gray
    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    main(img1,img2)
