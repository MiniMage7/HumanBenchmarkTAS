import pyautogui
from selenium.common import exceptions
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
    print("What score do you want to stop at?")
    targetScore = input("> ")
    litPixel = (255, 255, 255)
    squareCoordinates = [[780, 390], [950, 390], [1100, 390],
                         [780, 550], [950, 550], [1100, 550],
                         [780, 720], [950, 720], [1100, 720]]

    for i in range(1, int(targetScore) + 1):
        buttonList = []
        moveCount = 0
        while moveCount < i:
            for j in range(9):
                if pyautogui.pixelMatchesColor(squareCoordinates[j][0], squareCoordinates[j][1], litPixel):
                    buttonList.append(j)
                    moveCount += 1
                    while pyautogui.pixelMatchesColor(squareCoordinates[j][0], squareCoordinates[j][1], litPixel):
                        pass

        # Once all the squares have been shown, click them again
        for j in range(i):
            pyautogui.click(squareCoordinates[buttonList[j]][0], squareCoordinates[buttonList[j]][1])

        # Prevents duplicate detection
        pyautogui.sleep(.1)


# Starts aimTrainer 5 seconds after being called
def aimTrainer():
    pyautogui.sleep(5)
    # Make sure Aim Trainer is probably open
    if not pyautogui.pixelMatchesColor(965, 480, (149, 195, 232)):
        print("Aim Trainer not detected")
        pyautogui.sleep(2)
        return

    # Start game
    pyautogui.click(950, 500)

    count = 0
    while True:
        ss = pyautogui.screenshot(region=(210, 250, 1500, 500))
        # Check if game is over
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

        # Wait for and find the input box
        boxFound = False
        inputBox = None
        while not boxFound:
            try:
                inputBox = browser.find_element(By.TAG_NAME, "input")
                boxFound = True
            except exceptions.NoSuchElementException:
                pass

        # Type and submit number
        inputBox.send_keys(number)
        inputBox.send_keys(webdriver.Keys.RETURN)

        # Hit next for the next number
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
