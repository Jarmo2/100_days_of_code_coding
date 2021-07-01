import numpy as np
import sounddevice as sd
import time

class SoundPlayer:
    def __init__(self):
        #Duration
        self.long_dur = 2
        self.short_dur = 0.5
        # Samples per second
        self.sps = 44100
        # Frequency / pitch
        self.frequency = 440.0
        # Attenuation so the sound is reasonable
        self.atten = 0.3


    def short_sound(self):
        each_sample_number = np.arange(self.short_dur * self.sps)
        waveform = np.sin(2 * np.pi * each_sample_number * self.frequency / self.sps)
        waveform_quiet_short = waveform * self.atten
        sd.play(waveform_quiet_short, self.sps)
        time.sleep(self.short_dur)
        sd.stop()

    def long_sound(self):
        each_sample_number = np.arange(self.long_dur * self.sps)
        waveform = np.sin(2 * np.pi * each_sample_number * self.frequency / self.sps)
        waveform_quiet_short = waveform * self.atten
        sd.play(waveform_quiet_short, self.sps)
        time.sleep(self.long_dur)
        sd.stop()