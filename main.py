import soundcard as sc
import numpy as np
from scipy.io.wavfile import read, write

quantization = [8, 16, 32]


def main():

    while True:
        print("Wybierz:\n"
              "w -> nagrywanie\n"
              "r -> odcztywanie\n"
              "q -> wyjscie")
        option = input("Opcja:")
        match option:
            case 'w':
                value = int(input("Podaj poziom kwantyzacji(8,16,32): "))
                while value not in quantization:
                    value = int(input("Podaj poziom kwantyzacji: "))

                sampling = int(input("Podaj częstotliowść próbki: "))

                seconds = int(input("Podaj długość nagrywania: "))
                audio = sc.default_microphone()

                print("Nagrywanie rozpoczęte")
                recorded_audio = audio.record(seconds*sampling, sampling)
                data = recorded_audio

                if quantization == 8:
                    data = np.int8(data / np.max(abs(data)) * np.iinfo("int8").max)
                elif quantization == 16:
                    data = np.int16(data / np.max(abs(data)) * np.iinfo("int16").max)
                else:
                    data = np.int32(data / np.max(abs(data)) * np.iinfo("int32").max)
                write("output.wav", sampling, data)
                print("Recording has been saved successfully.")

            case 'r':
                data = read("output.wav")
                sampling = data[0]
                print("Sampling: ", sampling)
                data = np.float64(data[1] / np.max(abs(data[1])))
                channels = []
                for i in range(len(data[0])):
                    channels.append(i)
                print("Channels: ", channels)
                audio = sc.default_speaker()
                audio.play(data, sampling, channels)
            case 'q':
                break
            case _:
                print("Podales nieznana opcje")

main()

