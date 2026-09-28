"""Hero field, second pass. Reads as macro photography of light through fluid:
warm, abstract, premium. Deliberately not cells, not DNA, not a laboratory."""
import numpy as np, os
from PIL import Image, ImageFilter
exec(open('gen_cellove.py').read().split('print("writing to"')[0])

w,h=1400,1750
x,y=grid(w,h)

# deeper tonal base so the image has real range instead of a flat wash
base=lerp(STONE_D,STONE,np.clip(y*0.9+x*0.1,0,1)**1.05)
base=mix(base,(0xD3,0xC2,0xB6),np.clip((y-0.45)*1.7,0,1)**1.3,0.55)

# principal light, upper centre-left, strong
L=pool(x,y,0.44,0.26,0.62,0.54,1.7)
base=mix(base,PAPER,L,0.92)
base=mix(base,(0xFF,0xFE,0xFD),pool(x,y,0.44,0.24,0.30,0.26,2.2),0.55)

# rose bloom low left, the brand warmth
base=mix(base,ROSE,pool(x,y,0.14,0.86,0.60,0.54,1.9),0.34)
base=mix(base,ROSE_D,pool(x,y,0.06,0.98,0.34,0.30,2.2),0.20)

# gold fall on the right edge, restrained
base=mix(base,GOLD,pool(x,y,0.92,0.60,0.34,0.62,2.3),0.16)

# concentric interference around the light source, like fluid caustics
r=np.sqrt(((x-0.44)*1.75)**2+((y-0.28)*1.42)**2)
env=np.clip(1-r*0.92,0,1)**1.5
base=base+(np.cos(r*21.0)*env)[...,None]*7.5
base=base+(np.cos(r*47.0)*env**2.2)[...,None]*3.0

# two hairline caustic rings catch the rose
for rad,amt in ((0.33,0.22),(0.56,0.13)):
    e=np.exp(-((r-rad)**2)/(2*0.010**2))
    base=mix(base,ROSE,e,amt)

# soft diagonal sweep adds depth without a visible gradient band
sweep=np.clip(1-np.abs((x*0.8+(1-y)*0.6)-0.72)*2.0,0,1)**1.8
base=mix(base,PAPER,sweep,0.14)

base=base*(1-(1-pool(x,y,0.5,0.5,1.22,1.16,1.05))[...,None]*0.13)
a=grain(base,2.4,97)
a=np.array(Image.fromarray(a.astype('uint8')).filter(ImageFilter.GaussianBlur(0.4)),float)
save(a,'hero-field.jpg',92)
