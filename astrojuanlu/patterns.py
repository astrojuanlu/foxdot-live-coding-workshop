## Drum beats

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

## Melodies

# You might know this one
Clock.bpm = 80
dur = ([1] * 3 + [1.5, 0.5, 1]) * 2 + [1] * 3 + [9]
h1 >> pads([4, 4, 5, 3.5, 4, 5, 6, 6, 7, 6, 5  , 4, 5, 4, 3.5, 4], dur=dur, vib=0, amp=2, room=10)
h2 >> bass([4, 2, 0, 1, 2, 3.5, 4, 2, 0, 1, 1.5, 2, 0, 1, 1, 4], oct=5, dur=dur, amp=1, room=10)

# Blue
Clock.bpm = 120
p1 >> pluck([7, 2, 5, 7, 8, 4, 6, 7, 7, 5, 7, 9, 10, 5, 9, 8], dur=1 / 2)

# Dark blue
p1 >> pluck(P[7, 2, 5, 7, 8, 4, 6, 7, 7, 5, 7, 9, 10, 5, 9, 8].stutter(4), root=-1, dur=1 / 8, amp=1, room=50, vib=10)

# U can't touch this (well actually Super Freak)
p1 >> bass(
    [8, 7, 6, 5, 5, 2, 4, 4, 6, 5, 5],
    dur=[1, 1/2, 1/2, 1/2, rest(1), 1/2, 1/2, rest(1), 1/2, 1/2, rest(3/2)],
    oct=4,
    pan=[0] * 5 + [1] * 3 + [-1] * 3,
)
