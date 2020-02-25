# flag dictionary
def fDict():
    flagDict = {}
    flagDict['aliaswd']=[] 
    flagDict['cat']=['-n'] 
    flagDict['cd']=['~']      
    flagDict['chmod']=[]  
    flagDict['cp']=[]     
    flagDict['grep']=['-c','-v','-i','-n']   
    flagDict['head']=['-n']  
    flagDict['history']=[]
    flagDict['less']=[]   
    flagDict['ls']=['-a','-l','-h']     
    flagDict['mkdir']=[]  
    flagDict['mv']=[]     
    flagDict['pwd']=[]    
    flagDict['rm']=['-r']     
    flagDict['split']=['-b','-l']  
    flagDict['sort']=[]   
    flagDict['tail']=['-n']   
    flagDict['touch']=['-m','-a']  
    flagDict['wc']=['-l','-m','-w']     
    flagDict['!x']=[]    
    flagDict['who']=[]    
    return flagDict

def flags():
    flaglist = ['~','*','-a','-b','-l','-h','-r','-m','-w']
    return flaglist

def direct():    
    directlist = ['|','>','>>','<', '&']
    return directlist