import simpleaudio as sa
import wave
import sys

wave_file = wave.open(sys.argv[1],"rb")
wave_obj = sa.WaveObject.from_wave_read(wave_file)
play_obj=wave_obj.play()
play_obj.wait_done()
