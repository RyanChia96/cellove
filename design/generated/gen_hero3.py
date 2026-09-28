"""Hero field, third pass. Light falling across a warm surface.
No concentric rings: a glow ringed by circles reads as a cell, which the
brief bans. This is directional light and shadow only."""
import numpy as np, os
from PIL import Image, ImageFilter
exec(open('gen_cellove.py').read().split('print("writing to"')[0])

w,h=1400,1750
x,y=grid(w,h)

# diagonal tonal spine, light upper-left falling to warm shadow lower-right
t=np.clip(0.52*x+0.62*y,0,1)
base=lerp(PAPER,(0xCE,0xBA,0xAE),t**1.25)

# broad principal light, off-centre and soft-edged
base=mix(base,PAPER,pool(x,y,0.30,0.20,0.95,0.80,1.45),0.88)
base=mix(base,(0xFF,0xFE,0xFC),pool(x,y,0.26,0.14,0.44,0.36,1.9),0.60)

# rose gathers in the lower shadow, never as a disc
rose_mask=np.clip((0.58*x+0.72*y)-0.52,0,1)**1.45
base=mix(base,ROSE,rose_mask*0.62,0.42)
base=mix(base,ROSE_D,np.clip((0.5*x+0.8*y)-0.92,0,1)**1.3,0.34)

# gold grazes the right edge only
base=mix(base,GOLD,np.clip((x-0.72)/0.28,0,1)**2.1*np.clip(1-np.abs(y-0.46)*1.5,0,1),0.17)

# a single soft light streak, like a reflection off a curved surface
streak=np.exp(-((0.74*x-0.52*y-0.06)**2)/(2*0.042**2))
base=mix(base,PAPER,streak*np.clip(1-y*0.55,0,1),0.34)

# very low-frequency mottling for organic surface, far below ring frequency
n=np.random.default_rng(5).normal(0,1,(28,22))
n=np.array(Image.fromarray(((n-n.min())/np.ptp(n)*255).astype('uint8'))
           .resize((w,h),Image.BICUBIC),float)/255.0
base=base+((n-0.5)*9.0)[...,None]

base=base*(1-(1-pool(x,y,0.46,0.44,1.30,1.24,1.0))[...,None]*0.11)
a=grain(base,2.2,131)
a=np.array(Image.fromarray(a.astype('uint8')).filter(ImageFilter.GaussianBlur(0.5)),float)
save(a,'hero-field.jpg',92)
