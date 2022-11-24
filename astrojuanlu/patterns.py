# Simple hi-hat and bass drum
d1 >> play("x-")

# Typical rock beat: bass drum + snare drum, closed hi-hat
# Use brackets <> to play several patterns at the same time
d1 >> play("<x o ><-->")

# More interesting rock beat: bass drum + snare drum, closed hi-hat with open hi-hat at the end
# Use parentheses () to alternate between several patterns
d1 >> play("<x o ><-------(-=)>")

# Suspenseful hi-hat with claps and YEAH at the end
# Use square brackets [] to fit several patterns in the same beat in rapid succession
d1 >> play("-------[*([**]!)]", dur=1, amp=1, sample=2)

# Hi-hat, bass drum, claps, and YEAH
# We put the YEAH in a different pattern to control the sample independently
d1 >> play("<x-x-><  *( [**])>", dur=1/2)
d2 >> play("!", dur=8, sample=range(1, 5))

# Reggaeton
d1 >> play("xoxo", dur=[3/4,1/4,1/2,1/2])
# or, alternatively (it's equivalent!)
# Use dots . instead of whitespace for easier counting
d1 >> play("x..ox.o.", dur=1/4)

# Breakbeat I made up (I love this)
d1 >> play("x . . xxo . . oox ox ox o . ****", dur=1/4)
