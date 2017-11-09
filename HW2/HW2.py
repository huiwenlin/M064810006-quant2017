
# coding: utf-8

# In[1]:


#載入模組
import os


# In[2]:


#定義 maim函數，把下面的東西放到main裡
def main():
    #print為印出 括弧中放字串Hello World!要加上""
    print("Hello World!")
    #印出this is alice's greeting.字串
    print("this is alice's greeting.")
    #印出this is bob\'s greeting.字串
    print('this is bob\'s greeting.') 
    #""和''的用法是一樣的 
    
    #給數字到foo函數
    foo(5,10) 
    #印出Current working directory is字串並取工作目錄
    print ('Current working directory is' + os.getcwd())
    #印出 = 10次，也就是==========
    print('=' *10 )
    
     #定義變數的值
    counter =0
    counter +=1
    
    #把apple,oranges,cats放入list(可以改變成不同形式)
    food = ["apple","oranges","cats"] 
    #food裡面的迴圈
    for i in food: 
        print("i like to eat"+i) 
        
    print('count to ten:') #印出count to ten:
    
    for i in range(10):
        
        print (i+1) #因為預設0開始所以+1

#定義函數foo        
def foo(c, d): 
    res=(c+d)  #給定變數要做甚麼計算
    print ('{} plus {} is equal to {}'.format(c,d,res)) #給定輸出形式(c plus d is equal to res)
    if res < 50:
        print('foo')    #如果計算結果小於50就印出foo
    elif res>=50  and (c==42):
        print ('bar') #如果計算結果大於等於50和變數c判定為42同時成立時則印出bar
    else:
        print ('moo') #如果都不是上述結果印出moo
    return res 
if __name__=='__main__': #此CODE是被執行還是拿來執行
    main()

