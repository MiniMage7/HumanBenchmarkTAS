# Write your code here :-)
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


# Does the entire reaction test once it's started
def reaction():
    print("\nWaiting for green")

    for i in range(5):
        while True:
            if pyautogui.pixelMatchesColor(1620, 420, (75, 219, 106)):
                pyautogui.click(320, 420)
                pyautogui.sleep(.5)
                pyautogui.click(320, 420)
                break


# Does sequence memory up to the user specified amount
def sequenceMemory():
    pass
    print("What score do you want to stop at?")
    targetScore = input("> ")
    litPixel = (255, 255, 255)

    for i in range(1, int(targetScore) + 1):
        buttonList = []
        moveCount = 0
        while moveCount < i:
            # Checks if a next move has happened, save it, and wait til the next move might start
            moveCount += 1
            if pyautogui.pixelMatchesColor(780, 390, litPixel):
                buttonList.append(1)
                while pyautogui.pixelMatchesColor(780, 390, litPixel):
                    pass
            elif pyautogui.pixelMatchesColor(950, 390, litPixel):
                buttonList.append(2)
                while pyautogui.pixelMatchesColor(950, 390, litPixel):
                    pass
            elif pyautogui.pixelMatchesColor(1100, 390, litPixel):
                buttonList.append(3)
                while pyautogui.pixelMatchesColor(1100, 390, litPixel):
                    pass
            elif pyautogui.pixelMatchesColor(780, 550, litPixel):
                buttonList.append(4)
                while pyautogui.pixelMatchesColor(780, 550, litPixel):
                    pass
            elif pyautogui.pixelMatchesColor(950, 550, litPixel):
                buttonList.append(5)
                while pyautogui.pixelMatchesColor(950, 550, litPixel):
                    pass
            elif pyautogui.pixelMatchesColor(1100, 550, litPixel):
                buttonList.append(6)
                while pyautogui.pixelMatchesColor(1100, 550, litPixel):
                    pass
            elif pyautogui.pixelMatchesColor(780, 720, litPixel):
                buttonList.append(7)
                while pyautogui.pixelMatchesColor(780, 720, litPixel):
                    pass
            elif pyautogui.pixelMatchesColor(950, 720, litPixel):
                buttonList.append(8)
                while pyautogui.pixelMatchesColor(950, 720, litPixel):
                    pass
            elif pyautogui.pixelMatchesColor(1100, 720, litPixel):
                buttonList.append(9)
                while pyautogui.pixelMatchesColor(1100, 720, litPixel):
                    pass
            else:
                moveCount -= 1

        # Once all the squares have been shown, click them again
        for j in range(i):
            match buttonList[j]:
                case 1:
                    pyautogui.click(780, 390)
                case 2:
                    pyautogui.click(950, 390)
                case 3:
                    pyautogui.click(1100, 390)
                case 4:
                    pyautogui.click(780, 550)
                case 5:
                    pyautogui.click(950, 550)
                case 6:
                    pyautogui.click(1100, 550)
                case 7:
                    pyautogui.click(780, 720)
                case 8:
                    pyautogui.click(950, 720)
                case 9:
                    pyautogui.click(1100, 720)

        # Prevents a duplicate detection
        pyautogui.sleep(.1)


# Starts aimTrainer 5 seconds after being called
def aimTrainer():
    pyautogui.sleep(5)
    # Make sure Aim Trainer is probably open
    if not pyautogui.pixelMatchesColor(965, 480, (149, 195, 232)):
        print("Aim Trainer not detected")
        pyautogui.sleep(2)
        return

    pyautogui.click(950, 500)

    count = 0
    while True:
        ss = pyautogui.screenshot(region=(210, 250, 1500, 500))
        # Check if over
        if ss.getpixel((720, 460)) == (255, 209, 84):
            break

        xValue = 0
        yValue = 0
        while True:
            # Check if the pixel is the target
            if ss.getpixel((xValue, yValue)) == (149, 195, 232):
                pyautogui.click(xValue + 210, yValue + 250)
                count += 1
                break

            # Move to another spot on the screen
            xValue += 9
            if xValue > 1490:
                xValue = 0
                yValue += 9


# This one uses Selenium, so it opens automatically
# TODO: Make second number type correctly
def numberMemory():
    # Open a selenium browser to the test
    browser = webdriver.Firefox()
    url = "https://humanbenchmark.com/tests/number-memory"
    browser.get(url)
    pyautogui.sleep(10)

    # Start Test
    element = browser.find_element(By.XPATH, "/html/body/div/div/div[4]/div[1]/div/div/div/div[3]/button")
    element.click()

    # Loop of Number Memory
    while True:
        # Grab number
        pyautogui.sleep(1)
        page_source = browser.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        number = soup.find(class_='big-number')

        # Type number
        pyautogui.sleep(5)
        pyautogui.typewrite(number)
        pyautogui.sleep(.1)
        pyautogui.press('enter')

        # Click next
        pyautogui.sleep(.5)
        elements = browser.find_elements(By.TAG_NAME, "Button")
        elements[1].click()


if __name__ == '__main__':
    pyautogui.PAUSE = .001

    while True:
        print("Human Benchmark Tests\n")
        print("Select your test:")
        print("\t1: Reaction")
        print("\t2: Sequence Memory")
        print("\t3: Aim Trainer")
        print("\t4: Number Memory")
        userInput = input("> ")

        match userInput:
            case "1":
                reaction()
            case "2":
                sequenceMemory()
            case "3":
                aimTrainer()
            case "4":
                numberMemory()
