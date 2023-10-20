import pyautogui
from selenium.common import exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


# Does the reaction test
def reaction():
    browser.get("https://humanbenchmark.com/tests/reactiontime")
    pyautogui.sleep(2)

    # Start game
    background = browser.find_element(By.CLASS_NAME, "view-splash")
    background.click()

    for i in range(5):
        while True:
            try:
                # Find and click the background if its green
                background = browser.find_element(By.CLASS_NAME, "view-go")
                background.click()
                pyautogui.sleep(.1)
                break
            except exceptions.NoSuchElementException:
                pass
        # If it's not the last round, start the next round
        if i < 4:
            background = browser.find_element(By.CLASS_NAME, "view-result")
            background.click()


# Does sequence memory up to the user specified amount
def sequenceMemory():
    print("What score do you want to stop at?")
    targetScore = input("> ")

    browser.get("https://humanbenchmark.com/tests/sequence")
    pyautogui.sleep(2)

    # Click start button
    element = browser.find_element(By.XPATH, "/html/body/div/div/div[4]/div[1]/div/div/div/div[2]/button")
    element.click()

    # Loops for user specified amount of rounds
    for i in range(1, int(targetScore) + 1):
        squareList = []
        moveCount = 0
        while moveCount < i:
            while True:
                try:
                    activeEntities = browser.find_elements(By.CLASS_NAME, "active")

                    # Check to make sure it's a different active square
                    if len(squareList) > 0:
                        while activeEntities[1] == squareList[-1]:
                            activeEntities = browser.find_elements(By.CLASS_NAME, "active")

                    # Add the square to a list to be clicked later
                    squareList.append(activeEntities[1])
                    moveCount += 1
                    break
                except IndexError:
                    pass

        # Click all the stored squares
        pyautogui.sleep(.75)
        for square in squareList:
            square.click()


# Does the aim trainer test
# The window has to be in focus for aim trainer
def aimTrainer():
    browser.get("https://humanbenchmark.com/tests/aim")
    browser.minimize_window()
    browser.maximize_window()
    pyautogui.sleep(2)

    # Start game
    pyautogui.click(950, 500)

    count = 0
    while True:
        ss = pyautogui.screenshot(region=(350, 250, 1200, 500))
        # Check if game is over
        if ss.getpixel((580, 460)) == (255, 209, 84):
            break

        xValue = 0
        yValue = 0
        while True:
            # Check if the pixel is the target
            if ss.getpixel((xValue, yValue)) == (149, 195, 232):
                pyautogui.click(xValue + 350, yValue + 250)
                count += 1
                break

            # Move to another spot on the screen
            xValue += 9
            if xValue >= 1200:
                xValue = 0
                yValue += 9

    browser.minimize_window()


# Plays number memory up to user specified amount
def numberMemory():
    print("What score do you want to stop at?")
    targetScore = input("> ")

    browser.get("https://humanbenchmark.com/tests/number-memory")
    pyautogui.sleep(2)

    # Start Test
    element = browser.find_element(By.XPATH, "/html/body/div/div/div[4]/div[1]/div/div/div/div[3]/button")
    element.click()

    # Loop of Number Memory
    for _ in range(int(targetScore)):
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


# Plays verbal memory up to user specified amount
def verbalMemory():
    print("What score do you want to stop at?")
    targetScore = input("> ")

    browser.get("https://humanbenchmark.com/tests/verbal-memory")
    pyautogui.sleep(2)

    # Start Test
    element = browser.find_element(By.XPATH, "/html/body/div/div/div[4]/div[1]/div/div/div/div[4]/button")
    element.click()

    seenWords = []
    for _ in range(int(targetScore)):
        # Get the word shown
        page_source = browser.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        word = soup.find(class_='word')

        elements = browser.find_elements(By.TAG_NAME, "Button")
        # Check if word has been seen
        if word in seenWords:
            elements[1].click()
        else:
            elements[2].click()
            # Add word to seen list if it's a new word
            seenWords.append(word)


# Plays verbal memory up to 41 (the max score)
def chimpTest():
    browser.get("https://humanbenchmark.com/tests/chimp")
    pyautogui.sleep(2)

    # Start Test
    element = browser.find_element(By.XPATH, "/html/body/div/div/div[4]/div[1]/div/div[1]/div[2]/button")
    element.click()

    for i in range(4, 41):
        pyautogui.sleep(.1)
        # Get a list of all numbered buttons
        buttons = browser.find_elements(By.CLASS_NAME, "css-19b5rdt")
        buttonsPushed = 0
        listIndex = 0
        # This loop goes until all buttons have been pushed
        while buttonsPushed < i:
            # This keeps going through the list of potential buttons,
            # hitting them if they're next, and then removing them from the list
            if int(buttons[listIndex].get_attribute("data-cellnumber")) == buttonsPushed + 1:
                # When the next button is found, click it and remove it from the list
                buttons[listIndex].click()
                del buttons[listIndex]
                buttonsPushed += 1
                listIndex = 0
                continue
            else:
                # Check the next number in the list
                listIndex += 1

        # Go to next round
        pyautogui.sleep(.1)
        if i != 40:
            buttonObjects = browser.find_elements(By.TAG_NAME, "button")
            buttonObjects[1].click()


# Plays visual memory up to user specified score
def visualMemory():
    print("What score do you want to stop at?")
    targetScore = input("> ")

    browser.get("https://humanbenchmark.com/tests/memory")
    pyautogui.sleep(2)

    # Start Test
    element = browser.find_element(By.XPATH, "/html/body/div/div/div[4]/div[1]/div/div/div/div[2]/button")
    element.click()

    for _ in range(int(targetScore)):
        # Wait until there is an active square
        pyautogui.sleep(.3)
        activeElements = []
        while len(activeElements) < 2:
            activeElements = browser.find_elements(By.CLASS_NAME, "active")

        # Grab a list of all the active elements
        activeSquares = browser.find_elements(By.CLASS_NAME, "active")
        # The first element isn't a square
        del activeSquares[0]

        # Wait until the active squares fade
        while len(activeElements) > 2:
            activeElements = browser.find_elements(By.CLASS_NAME, "active")

        pyautogui.sleep(.3)
        # Click all the squares
        for square in activeSquares:
            square.click()


# Does the typing test
def typing():
    browser.get("https://humanbenchmark.com/tests/typing")
    pyautogui.sleep(2)

    # Grab all the letters to type
    page_source = browser.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    characters = soup.find_all(class_='incomplete')

    # Combine them into a string
    stringToType = ''
    for char in characters:
        stringToType += char.get_text()

    # Type the string
    typingBox = browser.find_element(By.CLASS_NAME, "letters")
    typingBox.send_keys(stringToType)


if __name__ == '__main__':
    pyautogui.PAUSE = .001
    print("Opening browser")

    # Open a selenium browser
    browser = webdriver.Firefox()
    browser.minimize_window()
    browser.get("https://humanbenchmark.com/")

    while True:
        print("Human Benchmark Tests\n")
        print("Select your test:")
        print("\t1: Reaction")
        print("\t2: Sequence Memory")
        print("\t3: Aim Trainer")
        print("\t4: Number Memory")
        print("\t5: Verbal Memory")
        print("\t6: Chimp Test")
        print("\t7: Visual Memory")
        print("\t8: Typing")
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
            case "5":
                verbalMemory()
            case "6":
                chimpTest()
            case "7":
                visualMemory()
            case "8":
                typing()
