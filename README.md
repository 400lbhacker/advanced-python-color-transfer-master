# advanced-python-color-transfer-master
 
Fixxes:
----------------------------------
Fixxed Fatal Errors. See: https://github.com/pengbo-learn/python-color-transfer/issues/1

Enhancements:
----------------------------------
previously all the imgs-paths.. (content and style and also output) were arbitarily declared in same directory. 
which was very confusing. I have updated this where they are now in seperate directories easy to organize.

in the imgs folder their are 2 subfolders named content and style. Your initial image go's into imgs/content folder, 
and your desired color-refrence image go's into imgs/style The photos must be matching in x,y dimensions. 
the content image must be named: 1.jpg, and style image: 2.jpg

I modified the code to remove the numpy concated output, which created a giant 5x collage, and found very hard 
to work with especially with larger images. Now it is designed that all 3x algorythem results will be saved 
seperately their own unique output png's. Which allows easier cycling and much more rapid overall procedure.
In the imgs/output folder they will appear as: (img_arr_lt.png, img_arr_mt.png, img_arr_reg.png) 


I have also compiled a standalone executable (.exe) for Windows users. Tested and working. it must be put in base
directory (next to demo.py) When clicked it will automatically computate imgs/content/1.jpg and 
imgs/style/2.jpg and produce 3 outputs in /imgs/output. Exactly how demo.py does. 

github would not let me upload the demo.exe cause it was to large (40 mb) but it can be downloaded here:
https://mega.nz/file/YmJmATyJ#-yjpcLS-2X9yI7qyOummSv3l8MsnDXffLdLL0Lk6XX8

![example output](https://github.com/400lbhacker/advanced-python-color-transfer-master/blob/main/example-outputs.png)



