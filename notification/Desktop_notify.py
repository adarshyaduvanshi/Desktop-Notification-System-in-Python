from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title="take rest",
            message=" if you hard work it will benifit for getting job",
            timeout=5,
        )
        time.sleep(10)