import sys
import ctypes

def startConfig():
    # This fix the monitor scaling different from 100%
    # Source: https://stackoverflow.com/questions/62775254/why-does-my-pygame-window-not-fit-in-my-4k3840x2160-monitor-scale-of-pygame-w
    if sys.platform == 'win32':
        # On Windows, the monitor scaling can be set to something besides normal 100%.
        # PyScreeze and Pillow needs to account for this to make accurate screenshots.
        # TODO - How does macOS and Linux handle monitor scaling?

        import ctypes

        try:
            ctypes.windll.user32.SetProcessDPIAware()

        except AttributeError:
            pass # Windows XP doesn't support monitor scaling, so just do nothing.




        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        width, heigth = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

        return width, heigth