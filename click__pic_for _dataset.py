#!/usr/bin/env python
# coding: utf-8

# In[13]:


import cv2


# In[14]:


x = cv2.VideoCapture(0)


# In[15]:


for i in range(0,10):
    status,photo = x.read()
    resize_photo = cv2.resize(photo , (224,224))
    cv2.imwrite("C://Users//GD GUPTA//Desktop//ml-ops//task3 using imagenet//testing//hey2//" + str(i) +".png" ,resize_photo)
    if cv2.waitKey(10) ==13:
        break
cv2.destroyAllWindows()
x.release()


# In[ ]:




