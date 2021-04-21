'''
how to convert a song's length to minutes:seconds to seconds: 
0-60 if the song lasts anywhere between 0 second and a minute
(60*minutes)+seconds otherwise
'''
def convert(minutes, seconds):
    return (60*minutes)+seconds
    

artist_library=[
    "Porter Robinson",
    "VIRTUAL SELF",
    "Madeon",
    "Porter Robinson & Madeon"
]

song_library=[
        ##porter robinson
        #pre-spitfire
        ["Say My Name", artist_library[0], convert(6,32)],
        #spitfire
        ["Spitfire", artist_library[0], convert(6,45)],
        ["Unison", artist_library[0], convert(5,50)],
        ["100% in the Bitch", artist_library[0], convert(4,11)],
        ["Vandalism (ft. Amba Shepherd)", artist_library[0], convert(7,20)],
        ["The State", artist_library[0], convert(5,57)],
        ["The Seconds (ft. Jano)", artist_library[0], convert(5,43)],
        #language + easy
        ["Language", artist_library[0], convert(6,8)],
        ["Easy (with Mat Zo)", artist_library[0], convert(6,36)],
        #worlds
        ["Divinity (ft. Amy Millan)", artist_library[0], convert(6,8)],      
        ["Sad Machine", artist_library[0], convert(5,50)],                  
        ["Years of War (ft. Breanne Düren and Sean Caskey)", artist_library[0], convert(3,56)],                 
        ["Flicker", artist_library[0], convert(4,39)],                      
        ["Fresh Static Snow", artist_library[0], convert(5,58)],            
        ["Polygon Dust (ft. Lemaitre)", artist_library[0], convert(3,29)],            
        ["Hear The Bells (ft. Imaginary Cities)", artist_library[0], convert(4,46)],            
        ["Natural Light", artist_library[0], convert(2,58)],            
        ["Lionhearted (ft. Urban Cone)", artist_library[0], convert(4,24)],  
        ["Sea of Voices", artist_library[0], convert(4, 59)],          
        ["Fellow Feeling", artist_library[0], convert(5, 49)],    
        ["Goodbye to a World", artist_library[0], convert(5, 28)],   
        #virtual self
        ["Particle Arts", artist_library[1], convert(2,58)],            
        ["Ghost Voices", artist_library[1], convert(4,24)],  
        ["a.i.ngel (Become God)", artist_library[1], convert(4, 59)],           
        ["Key", artist_library[1], convert(5, 28)],  
        ["EON BREAK", artist_library[1], convert(2,58)],         
        ["ANGEL VOICES", artist_library[1], convert(6, 32)],      
        #nurture
        ["Lifelike", artist_library[0], convert(1, 35)],
        ["Get Your Wish", artist_library[0], convert(3, 38)],  
        ["Look At The Sky", artist_library[0], convert(5, 10)],  
        ["Wind Tempos", artist_library[0], convert(6, 4)],
        ["Musician", artist_library[0], convert(3, 58)],
        ["do-re-mi-fa-so-la-ti-do", artist_library[0], convert(3, 35)],
        ["Mother", artist_library[0], convert(3, 36)],
        ["dullscythe", artist_library[0], convert(4, 0)],
        ["Sweet Time", artist_library[0], convert(4, 12)],
        ["Mirror", artist_library[0], convert(5, 7)],
        ["Something Comforting", artist_library[0], convert(4, 42)],  
        ["Blossom", artist_library[0], convert(3, 46)],
        ["Unfold (with Totally Enormous Extinct Dinosaurs)", artist_library[0], convert(4, 46)],
        ["Trying to Feel Alive", artist_library[0], convert(4, 44)],
        ["fullmoon lullaby (with Wednesday Campanella)", artist_library[0], convert(4, 3)],
        ##porter robinson & madeon (2016)
        ["Shelter", artist_library[3], convert(3, 39)],  

        ##madeon
        #adventure
        ["Isometric (Intro)", artist_library[2], convert(1,20)],      
        ["You're On (ft. Kyan)", artist_library[2], convert(3,12)],                  
        ["OK", artist_library[2], convert(3,1)],                 
        ["La Lune (ft. Dan Smith)", artist_library[2], convert(3,39)],                      
        ["Pay No Mind (ft. Passion Pit)", artist_library[2], convert(4,9)],            
        ["Beings", artist_library[2], convert(3,35)],            
        ["Imperium", artist_library[2], convert(3,18)],            
        ["Zephyr", artist_library[2], convert(3,40)],            
        ["Nonsense (ft. Mark Foster)", artist_library[2], convert(3,45)],  
        ["Innocence (ft. Aquilo)", artist_library[2], convert(3, 44)],    
        ["Pixel Empire", artist_library[2], convert(4,4)],      
        ["Home", artist_library[2], convert(3,45)],                  
        ["Icarus", artist_library[2], convert(3,34)],                 
        ["Finale (ft. Nicholas Petricca)", artist_library[2], convert(3,24)],                      
        ["The City", artist_library[2], convert(3,54)],            
        ["Cut the Kid", artist_library[2], convert(3,17)],            
        ["Technicolor", artist_library[2], convert(6,25)],            
        ["Only Way Out (ft. Vancouver Sleep Clinic)", artist_library[2], convert(3,46)],              
        #good faith
        ["Dream Dream Dream", artist_library[2], convert(3,54)],      
        ["All My Friends", artist_library[2], convert(3,24)],                  
        ["Be Fine", artist_library[2], convert(3,28)],                 
        ["Nirvana", artist_library[2], convert(2,32)],                      
        ["Mania", artist_library[2], convert(2,32)],            
        ["Miracle", artist_library[2], convert(4,10)],            
        ["No Fear No More", artist_library[2], convert(3,15)],            
        ["Hold Me Just Because", artist_library[2], convert(3,6)],            
        ["Heavy With Hoping", artist_library[2], convert(4,1)],  
        ["Borealis", artist_library[2], convert(4, 45)],    
    ]

#song library to play in order for a few days when nurture is released
song_library_nurture=[
        ["Lifelike", artist_library[0], convert(1, 35)],
        ["Get Your Wish", artist_library[0], convert(3, 38)],  
        ["Look At The Sky", artist_library[0], convert(5, 10)],  
        ["Wind Tempos", artist_library[0], convert(6, 4)],
        ["Musician", artist_library[0], convert(3, 58)],
        ["do-re-mi-fa-so-la-ti-do", artist_library[0], convert(3, 35)],
        ["Mother", artist_library[0], convert(3, 36)],
        ["dullscythe", artist_library[0], convert(4, 0)],
        ["Sweet Time", artist_library[0], convert(4, 12)],
        ["Mirror", artist_library[0], convert(5, 7)],
        ["Something Comforting", artist_library[0], convert(4, 42)],  
        ["Blossom", artist_library[0], convert(3, 46)],
        ["Unfold (with Totally Enormous Extinct Dinosaurs)", artist_library[0], convert(4, 46)],
        ["Trying to Feel Alive", artist_library[0], convert(4, 44)],
        ["fullmoon lullaby (with Wednesday Campanella)", artist_library[0], convert(4, 3)]
    ]