from time import sleep
import colorama


class Trafficlight:
    __colour_light = ['red', 'yellow', 'green']

    def running(self):
        # print(type(self.__colour_light))
        # print(type(self.__colour_light[0]))
        # print('\033[31m{}'.format('Trafficlight is working'), self.__colour_light[0])
        red_time = 7
        yellow_time = 2
        green_time = 1
        print(colorama.Fore.RED + 'Trafficlight is working')
        sleep(red_time)
        print(colorama.Fore.YELLOW + 'Trafficlight is working')
        sleep(yellow_time)
        print(colorama.Fore.GREEN + 'Trafficlight is working')
        sleep(green_time)
        print(colorama.Style.RESET_ALL)
        print('Trafficlight turned off')


my_trafficlight = Trafficlight()
my_trafficlight.running()
