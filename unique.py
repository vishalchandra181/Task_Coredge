import uuid

def uid(var_id=None,org_length=2,var2_id=None,res_length=2,var3_id=None,pro_length=1,totallength=10):
    
    """
      Ensure that org_length, res_length, and pro_length are not negative.
      The maximum length of unique_id is 32 if no parameters are given."
    """
    
    try:
        
        totalid=''
            
        #1
        if len(str(var_id))>=org_length and var_id is not None:
            org=str(var_id).replace(' ','')
            org=org[:org_length]
            totalid+=org
            
        # 5---7   
        elif len(str(var_id))<org_length and var_id is not None:
            org=str(var_id).replace(' ','')
            totalid+=org[:len(org)]

         #2
        if len(str(var2_id))>=res_length and var2_id is not None:
            res=str(var2_id).replace(' ','')
            res=res[:res_length]
            totalid+=res
            
        elif len(str(var2_id))<res_length and var2_id is not None:
            res=str(var2_id).replace(' ','')
            totalid+=res[:len(res)] 

        #3
        if len(str(var3_id))>=pro_length and var3_id is not None:
            pro=str(var3_id).replace(' ','')
            pro=pro[:pro_length]
            totalid+=pro
            
        elif len(str(var3_id))<pro_length and var3_id is not None:
            pro=str(var3_id).replace(' ','')
            totalid+=pro[:len(pro)] 

        #managelength
        if len(totalid)<totallength:
           uid=str(uuid.uuid4()).replace("-", "")
           totalid+=uid[:totallength-len(totalid)]
  
        else:
             totalid=totalid[:totallength]     
        
        return totalid         
    
    except Exception as ex:
        
        return str(ex)

print(uid(var_id='vi shal',org_length=3,var2_id='dfg',res_length=1,var3_id='gards',pro_length=2,totallength=10))