#three needed cuts
a = 17+11/16 #inches
b = round(a*2+30*3/25.4,4)#inches
c = 54#inches
T = 6060/25.4

# (108+3/4)*2
# 125.5

ass = 14
bss = 2
css = 6
best = [0,[]]
for x1 in range(css+1):# number of c in cut 1
    if x1*c>T:
        break
    for y1 in range(bss+1):# number of b in cut 1
        if x1*c+y1*b>T:
            break
        for x2 in range(css+1):# number of a in cut 1
            if x2*c>T or x1+x2>css:
                break
            for y2 in range(bss+1):# number of b in cut 1
                z1 = (T-(x1*c+y1*b))//a
                z2 = (T-(x2*c+y2*b))//a
                if x2*c+y2*b>T or y1+y2>bss or z1+z2>ass:
                    break
                l = T-a*(ass-z1-z2)-b*(bss-y1-y2)-c*(css-x1-x2)
                if l>best[0]:
                    best = [l,[(x1,y1,z1),(x2,y2,z2),(css-x1-x2,bss-y1-y2,ass-z1-z2)]]
                    ls= (T-(x1*c+y1*b+z1*a),T-(x2*c+y2*b+z2*a),l)
for i,tup in enumerate(best[1]):
    print('Cut '+ str(i+1)+':\n', tup[0],'of',str(c)+'"\n', tup[1],'of',str(b)+'"\n', int(tup[2]),'of',str(a)+'"\n')
print('Leftovers:\n',str(ls[0])+'"\n',str(ls[1])+'"\n',str(ls[2])+'"')