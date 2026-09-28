exec(open('gen.py').read().split('# ---------- A.')[0])
w,h=2880,920
x,y=grid(w,h)
# warm sand -> ivory, light sweeping from upper right
base=lerp(SAND,IVORY,np.clip(0.15+0.55*x+0.45*(1-y),0,1)**1.15)
sweep=pool(x,y,0.78,0.18,1.05,1.15,1.5)
base=base+(np.array(IVORY,float)-base)*sweep[...,None]*0.75
# soft champagne shadow lower-left grounds it
shade=pool(x,y,0.06,1.02,0.85,0.95,1.7)
base=base+(np.array(CHAMP,float)-base)*shade[...,None]*0.55
# delicate concentric rings, low amplitude, centred left of middle
r=np.sqrt(((x-0.34)*2.1)**2+((y-0.52)*1.05)**2)
rings=np.cos(r*40.0)*np.clip(1-r*1.15,0,1)**1.6
base=base+rings[...,None]*3.4
# one hairline highlight ring
edge=np.exp(-((r-0.42)**2)/(2*0.006**2))
base=base+(np.array(ROSE,float)-base)*edge[...,None]*0.16
vig=1-pool(x,y,0.5,0.5,1.3,1.25,1.1)
base=base*(1-vig[...,None]*0.06)
save(grain(base,2.8,53),'gen_band.jpg')
