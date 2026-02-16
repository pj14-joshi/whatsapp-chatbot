import pyautogui
import pyperclip
import time
from api import get_gemini_reply

# ✅ Your confirmed coordinates
CHAT_START = (870, 269)     # top-left of chat area
CHAT_END = (1596, 1000)      # bottom-right of chat area
INPUT_BOX = (1052, 1010)    # message input box

def get_chat_text():
    """Copy the latest visible messages from WhatsApp Web."""
    # Select chat area and copy text
    pyautogui.moveTo(*CHAT_START)
    pyautogui.dragTo(*CHAT_END, duration=1, button='left')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(869 , 269)
    time.sleep(0.5)

    chat_text = pyperclip.paste().strip()
    return chat_text

def send_reply(message):
    """Type and send the reply message."""
    pyautogui.click(*INPUT_BOX)
    time.sleep(0.5)
    pyautogui.typewrite(message)
    pyautogui.press('enter')
    print("✅ Sent reply:", message)

def main():
    print("🤖 WhatsApp Auto-Reply Bot Started!")
    print("👉 Make sure WhatsApp Web is open and the chat window is visible.\n")

    last_chat = ""

    while True:
        try:
            chat = get_chat_text()

            if chat and chat != last_chat:
                print("\n📩 New message detected!")
                print("📝 Chat copied:\n", chat)

                # Generate reply using Gemini API
                reply = get_gemini_reply(chat)
                print("💬 Gemini reply:", reply)

                send_reply(reply)
                last_chat = chat

            time.sleep(6)  # Check every 6 seconds

        except Exception as e:
            print("⚠️ Error:", e)
            time.sleep(5)

if __name__ == "__main__":
    main()
