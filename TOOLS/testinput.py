# Test the values provided in the xml input file
import os

def testinput(inp):
    
    niceinput=True
    
    if inp['verbose']!='1' and inp['verbose']!='0':
        print 'Verbose must be 1 or 0.'
        niceinput=False
    
    if inp['plot']!='1' and inp['plot']!='0':
        print 'plot must be 1 or 0.'
        niceinput=False
        
        
    try:
        ml=int(inp['quality']['min_length_in_sec'])
    except ValueError:
        print 'min_length_in_sec must be a number.'
        niceinput=False
        return niceinput
        
   
        
    if inp['first_step']!='split' and inp['first_step']!='decimate':
        print 'Invalid choice for first_step: Must be split or decimate.'
        niceinput=False
        
    
    if inp['processing']['split']['doit']!='0' and inp['processing']['split']['doit']!='1':
        print 'Choice for split must be 0 or 1.'
        niceinput=False
    
    try:
        int(inp['processing']['split']['length_in_sec'])
    except ValueError:
        print 'length_in_sec must be a number.'
        niceinput=False
        
        
    if inp['processing']['detrend']!='0' and inp['processing']['detrend']!='1':
        print 'Choice for detrend must be 0 or 1.'
        niceinput=False    
        
        
    if inp['processing']['demean']!='0' and inp['processing']['demean']!='1':
        print 'Choice for demean must be 0 or 1.'
        niceinput=False
       
      
     
    if inp['processing']['trim']!='0' and inp['processing']['trim']!='1':
        print 'Choice for trim must be 0 or 1.'
        niceinput=False  
    
    if inp['processing']['taper']['doit']!='0' and inp['processing']['taper']['doit']!='1':
        print 'Choice for taper must be 0 or 1.'
        niceinput=False
    
    
    try:
        tw=float(inp['processing']['taper']['taper_width'])
        if tw>0.05:
            print 'More than 5% of trace will be tapered.'
    except ValueError:
        print 'taper width must be a number.'
        niceinput=False
    
    
    
    if inp['processing']['bandpass_1']['doit']!='0' and inp['processing']['bandpass_1']['doit']!='1':
        print 'Choice for bandpass_1 must be 0 or 1.'
        niceinput=False  
        
        
    try:
        freq=float(inp['processing']['bandpass_1']['f_min'])
        if freq<(10/ml):
            print 'Warning, minimum window contains less than 10 cycles of lowest frequency.'
            
    except ValueError:
        print 'Frequencies must be numbers.'
       
    
    if inp['processing']['decimation']['doit']!='0' and inp['processing']['decimation']['doit']!='1':
        print 'Choice for decimation must be 0 or 1.'
        niceinput=False
        
        
    try:
        fs_new=inp['processing']['decimation']['new_sampling_rate'].split(' ')
        for fs in fs_new:
            fs=float(fs)
    except ValueError:
        print 'Sampling frequency must be number.'    
        
     
         
    try:
        freq=float(inp['processing']['bandpass_1']['f_max'])
        if freq>0.5*fs:
            print 'High corner of bandpass 1 is not compatible with new sampling rate.'
            
    except ValueError:
        print 'Frequencies must be numbers.'   
    
    
        
    if inp['processing']['bandpass_2']['doit']!='0' and inp['processing']['bandpass_2']['doit']!='1':
        print 'Choice for bandpass_2 must be 0 or 1.'
        niceinput=False
     
    try:
        freq=float(inp['processing']['bandpass_2']['f_min'])
        if freq<(10/ml):
            print 'Warning, minimum window contains less than 10 cycles of lowest frequency.'
            return niceinput
            
    except ValueError:
        print 'Frequencies must be numbers.'
    
    try:
        freq=float(inp['processing']['bandpass_2']['f_max'])
        if freq>0.5*fs:
            print 'High corner of bandpass 2 is not compatible with new sampling rate.'
            return niceinput
            
    except ValueError:
        print 'Frequencies must be numbers.'   
        
    
   
       
    