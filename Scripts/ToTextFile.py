import  numpy as np

#creating an empty numpy array
array = np.ones((512, 512))

#opening file to write
with open('test.txt', 'w') as file:
    for j in range(0,512): # y loop
        for i in range(0,512,16): #x loop
            for k in range(i,i+16):# within the 16 rois
                x_0 = k
                y_0 = j
                x_1 = x_0+1
                y_1 = y_0+1
                n = [x_0,y_0,x_1,y_1]
                file.write(str(j*10+k)+" ")
        file.write("\n")









