import os

path = 'C:/Users/tahsinsoyak/Desktop/New folder/'
i = 0
for filename in os.listdir(path):
    os.rename(os.path.join(path,filename), os.path.join(path,str(i)+'.jpg'))
    i = i +1