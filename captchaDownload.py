import urllib2
import time

proxy = urllib2.ProxyHandler({'https': 'https://suraj.jha:jZpn5pcy@202.141.80.22:3128'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

URL = "https://webmail.iitg.ernet.in/plugins/captcha/backends/watercap/image_generator.php?sq=1483962648"
for i in xrange(400):
    with open(str(i)+'.png','wb') as f:
        f.write(urllib2.urlopen(URL).read())
        f.close()
    time.sleep(0.01)
