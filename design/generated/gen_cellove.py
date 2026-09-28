"""Cellove atmospheric fields.

The brief bans medical stock photography and glowing-DNA/blue-cell graphics.
These are warm abstract light fields used as backgrounds only, tuned to the
locked token palette. They are never the subject of a section.
"""
import numpy as np
from PIL import Image, ImageFilter
import os

PAPER=(0xFD,0xFB,0xF9); STONE=(0xEF,0xE8,0xE2); STONE_D=(0xE2,0xD8,0xD1)
INK=(0x23,0x20,0x1F); INK_2=(0x35,0x30,0x2D)
ROSE=(0xB8,0x7C,0x6E); ROSE_D=(0x8F,0x53,0x46); GOLD=(0xB3,0x94,0x4E)

OUT = os.path.join(os.path.dirname(__file__), '..', '..', 'public', 'media')
OUT = os.path.abspath(OUT)
os.makedirs(OUT, exist_ok=True)

def lerp(a,b,t):
    a=np.array(a,float); b=np.array(b,float)
    return a[None,None,:]+(b-a)[None,None,:]*t[...,None]

def grid(w,h):
    y,x=np.mgrid[0:h,0:w]
    return x/(w-1), y/(h-1)

def pool(x,y,cx,cy,rx,ry,soft=2.2):
    d=np.sqrt(((x-cx)/rx)**2+((y-cy)/ry)**2)
    return np.clip(1-d,0,1)**soft

def mix(base,color,mask,amt):
    return base+(np.array(color,float)-base)*mask[...,None]*amt

def grain(img,amt=3.0,seed=7):
    rng=np.random.default_rng(seed)
    n=rng.normal(0,amt,img.shape[:2])
    n=np.array(Image.fromarray(((n-n.min())/(np.ptp(n)+1e-9)*255).astype('uint8'))
               .filter(ImageFilter.GaussianBlur(0.6)),float)
    n=(n-n.mean())/(n.std()+1e-9)*amt
    return np.clip(img+n[...,None],0,255)

def save(a,name,q=90):
    p=os.path.join(OUT,name)
    Image.fromarray(a.astype('uint8')).save(p,quality=q,subsampling=0,optimize=True)
    print(f"  {name:28} {a.shape[1]}x{a.shape[0]}  {os.path.getsize(p)//1024}kb")

print("writing to", OUT)

# A. Hero field, 4:5 portrait. Light gathers upper-centre, warmth settles low-left.
w,h=1200,1500
x,y=grid(w,h)
base=lerp(PAPER,STONE_D,np.clip(y*0.78+x*0.22,0,1)**1.1*0.95)
base=mix(base,PAPER,pool(x,y,0.48,0.30,0.82,0.70,1.9),0.70)
base=mix(base,ROSE,pool(x,y,0.16,0.88,0.72,0.62,2.1),0.14)
base=mix(base,GOLD,pool(x,y,0.84,0.66,0.46,0.50,2.6),0.07)
r=np.sqrt(((x-0.48)*1.9)**2+((y-0.34)*1.5)**2)
base=base+(np.cos(r*26.0)*np.clip(1-r*1.2,0,1)**1.8)[...,None]*2.2
base=base*(1-(1-pool(x,y,0.5,0.5,1.28,1.2,1.15))[...,None]*0.07)
save(grain(base,2.6,11),'hero-field.jpg')

# B. Deep band, wide. The single deliberate dark moment on the page.
w,h=2880,1000
x,y=grid(w,h)
base=lerp(INK,INK_2,np.clip(y*1.05,0,1))
base=mix(base,ROSE_D,pool(x,y,0.26,0.60,0.60,1.10,2.3),0.34)
base=mix(base,GOLD,pool(x,y,0.78,0.28,0.44,0.90,2.7),0.14)
r=np.sqrt(((x-0.26)*2.4)**2+((y-0.60)*1.25)**2)
base=base+(np.cos(r*30.0)*np.clip(1-r*1.1,0,1)**1.7)[...,None]*3.4
save(grain(base,3.0,23),'band-deep.jpg')

# C. Absorption field, landscape. Light travelling left to right = delivery.
w,h=1600,1100
x,y=grid(w,h)
base=lerp(STONE,PAPER,np.clip(0.10+0.70*x+0.30*(1-y),0,1)**1.2)
base=mix(base,PAPER,pool(x,y,0.80,0.24,1.00,1.10,1.6),0.72)
base=mix(base,ROSE,pool(x,y,0.10,0.92,0.66,0.70,2.0),0.13)
r=np.sqrt(((x-0.30)*2.0)**2+((y-0.54)*1.15)**2)
base=base+(np.cos(r*34.0)*np.clip(1-r*1.15,0,1)**1.7)[...,None]*2.6
edge=np.exp(-((r-0.40)**2)/(2*0.007**2))
base=mix(base,ROSE,edge,0.13)
save(grain(base,2.4,53),'absorption-field.jpg')

# D. Portrait placeholder plates. TODO: replace with real doctor photography.
for i,(seed,cx) in enumerate([(31,0.42),(37,0.52),(43,0.36)],start=1):
    w,h=800,1000
    x,y=grid(w,h)
    base=lerp(STONE_D,STONE,np.clip(y*0.88+0.06,0,1))
    base=mix(base,PAPER,pool(x,y,cx,0.30,0.86,0.80,1.8),0.52)
    base=mix(base,ROSE,pool(x,y,0.5,1.02,0.9,0.5,2.0),0.07)
    save(grain(base,2.2,seed),f'portrait-placeholder-{i}.jpg')
