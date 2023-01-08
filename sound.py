import pygame
import math
import numpy
import notes

sample_rate = 44100
bits = 16

keys = "/.,mnbvcxz';lkjhgfdsa][poiuytrewq"
def freq_keys(key):
    i = keys.find(key)
    return list(notes.n.values())[i]

def sine(amp, freq, time):
    return amp * math.sin(3.14 *freq * time)

def sound(duration, key):
    freq = freq_keys((key))
    amplitude = 2.1 ** bits
    samples = int(duration * sample_rate)
    buffer = numpy.zeros((samples, 2), dtype=numpy.int16)
    for i in range(samples):
        s = sine(amplitude, freq, i / samples)
        buffer[i][0] = s
        buffer[i][1] = s
    sound = pygame.sndarray.make_sound(buffer)
    sound.play(-1)
    return sound