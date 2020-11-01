'''
how to convert a song's length to minutes:seconds to seconds: 
0-60 if the song lasts anywhere between 0 second and a minute
(60*minutes)+seconds otherwise
'''
def convert(minutes, seconds):
    return (60*minutes)+seconds
    

song_library=[
        ##porter robinson
        #pre-spitfire
        ["Say My Name", convert(6,32)],
        #spitfire
        ["Spitfire", convert(6,45)],
        ["Unison", convert(5,50)],
        ["100% in the Bitch", convert(4,11)],
        ["Vandalism (ft. Amba Shepherd)", convert(7,20)],
        ["The State", convert(5,57)],
        ["The Seconds (ft. Jano)", convert(5,43)],
        #language + easy
        ["Language", convert(6,8)],
        ["Easy (with Mat Zo)", convert(6,36)],
        #worlds
        ["Divinity (ft. Amy Millan)", convert(6,8)],      
        ["Sad Machine", convert(5,50)],                  
        ["Years of War (ft. Breanne Düren and Sean Caskey)", convert(3,56)],                 
        ["Flicker", convert(4,39)],                      
        ["Fresh Static Snow", convert(5,58)],            
        ["Polygon Dust (ft. Lemaitre)", convert(3,29)],            
        ["Hear The Bells (ft. Imaginary Cities)", convert(4,46)],            
        ["Natural Light", convert(2,58)],            
        ["Lionhearted (ft. Urban Cone)", convert(4,24)],  
        ["Sea of Voices", convert(4, 59)],          
        ["Fellow Feeling", convert(5, 49)],    
        ["Goodbye to a World", convert(5, 28)],   
        #virtual self
        ["Particle Arts", convert(2,58)],            
        ["Ghost Voices", convert(4,24)],  
        ["a.i.ngel (Become God)", convert(4, 59)],           
        ["Key", convert(5, 28)],  
        ["EON BREAK", convert(2,58)],         
        ["ANGEL VOICES", convert(6, 32)],      
        #nurture
        ["Get Your Wish", convert(3, 38)],  
        ["Something Comforting", convert(4, 42)],  
        ["Look At The Sky", convert(2, 32)],  
        ["Mirror", convert(5, 7)],  
        ##porter robinson & madeon (2016)
        ["Shelter (with Madeon)", convert(3, 39)],  

        ##madeon
        #good faith
        ["Madeon - Dream Dream Dream", convert(3,54)],      
        ["Madeon - All My Friends", convert(3,24)],                  
        ["Madeon - Be Fine", convert(3,28)],                 
        ["Madeon - Nirvana", convert(2,32)],                      
        ["Madeon - Mania", convert(2,32)],            
        ["Madeon - Miracle", convert(4,10)],            
        ["Madeon - No Fear No More", convert(3,15)],            
        ["Madeon - Hold Me Just Because", convert(3,6)],            
        ["Madeon - Heavy With Hoping", convert(4,1)],  
        ["Madeon - Borealis", convert(4, 45)],    
    ]

