"""Absorption field, second pass. Light travelling left to right through a warm
medium, which is the idea the section is about. No concentric rings: a ring
around a glow reads as a cell, and the brief rules that imagery out."""
import numpy as np
from PIL import Image, ImageFilter
exec(open('gen_cellove.py').read().split('print("writing to"')[0])

w,h=1600,1100
x,y=grid(w,h)

# medium darkens to the left, clears to the right: the direction is the message
base=lerp((0xD8,0xC7,0xBC),PAPER,np.clip(0.06+0.78*x+0.22*(1-y),0,1)**1.35)

# light entering from the right, broad and soft
base=mix(base,PAPER,pool(x,y,0.88,0.30,1.05,1.15,1.5),0.80)
base=mix(base,(0xFF,0xFE,0xFD),pool(x,y,0.94,0.24,0.42,0.50,2.0),0.45)

# three soft horizontal bands of travel, low contrast, no closed shapes
for cy,amp,width in ((0.34,0.030,0.10),(0.52,0.042,0.13),(0.71,0.026,0.09)):
    band=np.exp(-((y-cy-0.035*np.sin(x*2.6))**2)/(2*width**2))
    base=mix(base,PAPER,band*np.clip(x*1.25,0,1),amp*6.0)

# rose settles in the dense left where light has not yet arrived
base=mix(base,ROSE,np.clip(1-x*2.0,0,1)**1.4*np.clip(y*1.15,0,1),0.30)
base=mix(base,ROSE_D,np.clip(1-x*3.2,0,1)**1.6*np.clip((y-0.5)*1.9,0,1),0.22)

# gold grazes the upper left corner only
base=mix(base,GOLD,np.clip(1-x*3.6,0,1)**2.0*np.clip(1-y*2.4,0,1),0.16)

n=np.random.default_rng(17).normal(0,1,(26,18))
n=np.array(Image.fromarray(((n-n.min())/np.ptp(n)*255).astype('uint8'))
           .resize((w,h),Image.BICUBIC),float)/255.0
base=base+((n-0.5)*7.0)[...,None]

base=base*(1-(1-pool(x,y,0.5,0.5,1.32,1.26,1.05))[...,None]*0.08)
a=grain(base,2.2,71)
a=np.array(Image.fromarray(a.astype('uint8')).filter(ImageFilter.GaussianBlur(0.45)),float)
save(a,'absorption-field.jpg',92)
