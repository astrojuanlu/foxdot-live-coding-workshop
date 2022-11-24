# `astrojuanlu` sound bank

## Inspiration

- How old gaming consoles created sound https://youtu.be/8RrQrATnXXY
- Basic waveforms explained https://youtu.be/VRD9Uj2YTBk
- Hi-hat variations and explanations https://youtu.be/KzCXZ3TnUxo
- One of my favourite videogame soundtracks ever https://youtu.be/rdYh7XTxnZE
- An electronic music classic that captivates me https://youtu.be/iRA82xLsb_w
- Marc Rebillet's "How to funk in 2 minutes" https://youtu.be/3vBwRfQbXkg
- "Keygen? What's that?" says the Gen Z https://youtu.be/BvWnwi-Kgm4
- Luis Fonsi & Dadee Yankee feat. Square Waves https://youtu.be/siRMGLA6FsU

## Sound effects

- SNES Super Mario from https://www.mariomayhem.com/downloads/sounds/
- Super Mario Kart from https://www.superluigibros.com/super-mario-allstars-sounds-wav
- Others from https://soundeffects.fandom.com/

## Tools

- Collaborative live coding! https://github.com/Qirky/Troop
- Cool visuals https://github.com/projectM-visualizer/projectm

## Further reading

- In-depth FoxDot workshop https://gitlab.com/iShapeNoise/foxdot_codingmusic_part1/
- Advanced patterns by the FoxDot author https://github.com/Qirky/FoxDot-Worksheet/
- Live coding book by [Alex McLean](https://en.wikipedia.org/wiki/Alex_McLean) https://livecodingbook.toplap.org/book/

## FoxDot Cheatsheet

| Number | Anglo | Latin |
|---|---|---|
| 0 | C | Do |
| 1 | D | Re |
| 2 | E | Mi |
| 3 | F | Fa |
| 4 | G | Sol |
| 5 | A | La |
| 6 | B | Si |

All `Samples`:

```
'!': Yeah!
'#': Crash
'$': Beatbox
'%': Noise bursts
'&': Chime
'*': Clap
'+': Clicks
'-': Hi hat closed
'/': Reverse sounds
'1': Vocals (One)
'2': Vocals (Two)
'3': Vocals (Three)
'4': Vocals (Four)
':': Hi-hats
'=': Hi hat open
'@': Gameboy noise
'A': Gameboy kick drum
'B': Short saw
'C': Choral
'D': Dirty snare
'E': Ringing percussion
'F': Trumpet stabs
'G': Ambient stabs
'H': Clap
'I': Rock snare
'J': Ambient stabs
'K': Percussive hits
'L': Noisy percussive hits
'M': Acoustic toms
'N': Gameboy SFX
'O': Heavy snare
'P': Tabla long
'Q': Electronic stabs
'R': Metallic
'S': Tamborine
'T': Cowbell
'U': Misc. Fx
'V': Hard kick
'W': Distorted
'X': Heavy kick
'Y': High buzz
'Z': Loud stabs
'\\': Lazer
'^': 'Donk'
'a': Gameboy hihat
'b': Noisy beep
'c': Voice/string
'd': Woodblock
'e': Electronic Cowbell
'f': Pops
'g': Ominous
'h': Finger snaps
'i': Jungle snare
'j': Whines
'k': Wood shaker
'l': Robot noise
'm': 808 toms
'n': Noise
'o': Snare drum
'p': Tabla
'q': Ambient stabs
'r': Metal
's': Shaker
't': Rimshot
'u': Soft snare
'v': Soft kick
'w': Dub hits
'x': Bass drum
'y': Percussive hits
'z': Scratch
'|': Hangdrum
'~': Ride cymbal
```

All "instruments" (`SynthDefs`):

```
['loop', 'stretch', 'play1', 'play2', 'audioin', 'noise', 'dab', 'varsaw', 'lazer', 'growl',
'bass', 'dirt', 'crunch', 'rave', 'scatter', 'charm', 'bell', 'gong', 'soprano', 'dub',
'viola', 'scratch', 'klank', 'feel', 'glass', 'soft', 'quin', 'pluck', 'spark', 'blip',
'ripple', 'creep', 'orient', 'zap', 'marimba', 'fuzz', 'bug', 'pulse', 'saw', 'snick',
'twang', 'karp', 'arpy', 'nylon', 'donk', 'squish', 'swell', 'razz', 'sitar', 'star',
'jbass', 'sawbass', 'prophet', 'pads', 'pasha', 'ambi', 'space', 'keys', 'dbass', 'sinepad']
```

All effects (`FX`):

```
<'bandPassFilter': keyword='bpf', other args=['bpr', 'bpnoise', 'sus']>
<'chop': keyword='chop', other args=['sus']>
<'coarse': keyword='coarse', other args=['sus']>
<'combDelay': keyword='echo', other args=['beat_dur', 'echotime']>
<'filterSwell': keyword='swell', other args=['sus', 'hpr']>
<'formantFilter': keyword='formant'>
<'glissando': keyword='glide', other args=['glidedelay', 'sus']>
<'highPassFilter': keyword='hpf', other args=['hpr']>
<'lowPassFilter': keyword='lpf', other args=['lpr']>
<'overdriveDistortion': keyword='drive'>
<'pitchBend': keyword='bend', other args=['sus', 'benddelay']>
<'pitchShift': keyword='pshift'>
<'reverb': keyword='room', other args=['mix']>
<'slideFrom': keyword='slidefrom', other args=['sus', 'slidedelay']>
<'slideTo': keyword='slide', other args=['sus', 'slidedelay']>
<'spinPan': keyword='spin', other args=['sus']>
<'striate': keyword='striate', other args=['sus', 'buf', 'rate']>
<'tremolo': keyword='tremolo', other args=['beat_dur']>
<'trimLength': keyword='cut', other args=['sus']>
<'vibrato': keyword='vib', other args=['vibdepth']>
<'wavesShapeDistortion': keyword='shape'>
```
