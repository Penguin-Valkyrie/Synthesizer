from pysinewave import SineWave
import time

class SoundWave:
    def __init__(self, pitch, volumeC, harmonic=0):
        if harmonic == 0:
            self.pitch = pitch
        if harmonic == 1:
            self.pitch = pitch + 12
        if harmonic == 2:
            self.pitch = pitch + 19
        if harmonic == 3:
            self.pitch = pitch + 24
        if harmonic == 4:
            self.pitch = pitch + 28
        if harmonic == 5:
            self.pitch = pitch + 31
        self.fadeVolume = -100
        self.volumeDifferential = 70
        self.volume = (volumeC - self.volumeDifferential)
        if harmonic != 0:
            self.volume = self.volume / (harmonic * 4)
        self.wave = SineWave(self.pitch, 12, self.fadeVolume, 200)

    def begin(self):
        self.wave.play()
        self.wave.set_volume(self.volume)
    
    def end(self):
        self.wave.set_volume(self.fadeVolume)
        time.sleep(.1)
        self.wave.stop()

    def changePitch(self, pitch):
        self.pitch = pitch
        self.wave.set_pitch(self.pitch)
    
    def changeVolume(self, volumeC):
        self.volume = volumeC - self.volumeDifferential
        self.wave.set_volume(self.volume)

go = True
pitch = 0
volumeController = 50
sinewaves = []
sinewaves.append(SoundWave(pitch, volumeController))

while go:
    command = input("Command: begin, end, higher, lower, louder, add harmonic, readout, quit? ")

    if command == "begin":
        sinewaves[0].begin()

    elif command == "end":
        for w in sinewaves:
            w.end()

    elif command == "higher":
        pitch += 1
        for w in sinewaves:
            w.changePitch(pitch)

    elif command == "lower":
        pitch -= 1
        for w in sinewaves:
            w.changePitch(pitch)

    elif command == "louder":
        volumeController += 10
        sinewaves[0].changeVolume(volumeController)

    elif command == "quieter":
        volumeController -= 10
        sinewaves[0].changeVolume(volumeController)

    elif command == "add harmonic":
        harmonicNumber = input("Harmonic Number (1 - 5): ")
        sinewaves.append(SoundWave(pitch, volumeController, int(harmonicNumber)))
        sinewaves[-1].begin()

    elif command == "quit":
        go = False

    elif command == "readout":
        for w in range(0, len(sinewaves) - 1):
            print("Harmonic " + str(w) + "'s volume is " + str(sinewaves[w].volume))

    else:
        print("Unknown Input, please try again")
