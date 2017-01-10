# captchaDecoder
Python atttempt to decode IITG webmail captcha. Currently not working as expected


#Tasks pending now

 * Write actual value of each image (manually) so that error can be calculated automatically
 * Component labelling is not done. That may be causing error.


### My approach:
I am almost following this [paper](http://www.iitg.ernet.in/amitsethi/publications/12.05CaptchaIndicon.pdf). I do not know exactly how to make templates so i cropped letters from preprocessed captcha images. 4 instances of each letter. Then I removed all zeroes from all side of the template images. Based on the final size of the template image i am cutting piece of captcha and comparing it with all template image. In this case for each template image the portion that is cut out from captcha is different that is not the case with the paper's algorithm. I am unable to pin point why performance is so low. Did not even quantify the error.May be variable area of consideration is causing problem.
res1.txt contains result when i consider pearson coefficient.
res.txt contains result when Mean square error is considered.
 
