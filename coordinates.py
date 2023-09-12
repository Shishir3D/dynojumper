import pyautogui

def main():
    print("Click anywhere on the screen to get coordinates.")
    print("Press Ctrl+C to exit.")

    try:
        while True:
            x, y = pyautogui.position()
            print(f"X: {x}, Y: {y}")
    except KeyboardInterrupt:
        print("\nProgram terminated.")

main()