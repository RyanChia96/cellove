import numpy as np
from PIL import Image, ImageFilter

IVORY=(0xFB,0xF8,0xF4); BEIGE=(0xF4,0xED,0xE4); CHAMP=(0xEA,0xDC,0xC8)
SAND=(0xDD,0xC9,0xAF); ROSE=(0xBE,0x8E,0x76); GOLD=(0xB3,0x94,0x56)
INK=(0x1E,0x1B,0x18); INK8=(0x3B,0x35,0x2F)

def lerp(a,b,t):
    a=np.array(a,float); b=np.array(b,float)
    return a[None,None,:]+(b-a)[None,None,:]*t[...,None]

def grid(w,h):
    y,x=np.mgrid[0:h,0:w]
    return x/(w-1), y/(h-1)

def pool(x,y,cx,cy,rx,ry,soft=2.2):
    d=np.sqrt(((x-cx)/rx)**2+((y-cy)/ry)**2)
    return np.clip(1-d,0,1)**soft

def grain(img,amt=5.0,seed=7):
    rng=np.random.default_rng(seed)
    n=rng.normal(0,amt,img.shape[:2])
    n=np.array(Image.fromarray(((n-n.min())/(np.ptp(n)+1e-9)*255).astype('uint8')).filter(ImageFilter.GaussianBlur(0.6)),float)
    n=(n-n.mean())/ (n.std()+1e-9) * amt
    return np.clip(img+n[...,None],0,255)

def save(a,p,q=92):
    Image.fromarray(a.astype('uint8')).save(p,quality=q,subsampling=0)
    print(p, a.shape)

# ---------- A. Hero backdrop (560x640 slot @2x) ----------
w,h=1120,1280
x,y=grid(w,h)
base=lerp(IVORY,CHAMP,np.clip(y*0.85+x*0.15,0,1)*0.9)
light=pool(x,y,0.52,0.44,0.78,0.72,2.0)
base=base+ (np.array(IVORY,float)-base)*light[...,None]*0.55
warm=pool(x,y,0.18,0.92,0.9,0.7,1.6)
base=base+(np.array(SAND,float)-base)*warm[...,None]*0.22
vig=1-pool(x,y,0.5,0.5,1.25,1.15,1.2)
base=base*(1-vig[...,None]*0.10)
save(grain(base,3.2,11),'gen_hero.jpg')

# ---------- B. Ambient band (1440x460 @2x) ----------
w,h=2880,920
x,y=grid(w,h)
base=lerp(INK,INK8,np.clip(y*1.1,0,1))
p1=pool(x,y,0.30,0.55,0.55,1.05,2.4)
base=base+(np.array(ROSE,float)-base)*p1[...,None]*0.30
p2=pool(x,y,0.72,0.30,0.42,0.85,2.6)
base=base+(np.array(GOLD,float)-base)*p2[...,None]*0.20
rings=np.cos(np.sqrt(((x-0.30)*2.6)**2+((y-0.55)*1.3)**2)*34.0)
base=base+(rings*p1)[...,None]*5.0
save(grain(base,3.6,23),'gen_band.jpg')

# ---------- C. Portrait placeholder texture (300x400 @2x) ----------
w,h=600,800
x,y=grid(w,h)
base=lerp(CHAMP,BEIGE,np.clip(y*0.9+0.05,0,1))
lp=pool(x,y,0.42,0.30,0.85,0.8,1.8)
base=base+(np.array(IVORY,float)-base)*lp[...,None]*0.5
save(grain(base,2.6,31),'gen_portrait.jpg')

# ---------- D. Map surface (560x520 @2x) ----------
w,h=1120,1040
x,y=grid(w,h)
base=lerp(INK,INK8,np.clip(y*0.8+x*0.2,0,1))
lp=pool(x,y,0.5,0.5,0.7,0.7,2.0)
base=base+(np.array(GOLD,float)-base)*lp[...,None]*0.10
save(grain(base,2.4,41),'gen_map.jpg')
