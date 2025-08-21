import time
from collections import deque

class Message:
    def __init__(self, text, timestamp):
        self.text = text
        self.timestamp = timestamp

class ChatHistory:
    def __init__(self):
        self.message_queue = deque()
        self.undo_stack = []
        self.redo_stack = []

    def send_message(self, text):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        msg = Message(text, timestamp)
        self.message_queue.append(msg)
        self.undo_stack.append(msg)
        self.redo_stack.clear()
        print(f"Message sent: {text} [{timestamp}]")

    def show_history(self):
        print("Message History:")
        for idx, msg in enumerate(self.message_queue, 1):
            print(f"{idx}. {msg.text} [{msg.timestamp}]")
        if not self.message_queue:
            print("-- No messages --")

    def undo(self):
        if not self.undo_stack:
            print("No message to undo.")
            return
        msg = self.undo_stack.pop()
        self.redo_stack.append(msg)
        self.message_queue.pop()
        print(f"Undo: Removed '{msg.text}'")

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo.")
            return
        msg = self.redo_stack.pop()
        self.message_queue.append(msg)
        self.undo_stack.append(msg)
        print(f"Redo: Restored '{msg.text}'")

def main():
    chat = ChatHistory()
    while True:
        print("\n--- Chat Menu ---")
        print("1. Send message")
        print("2. Show history")
        print("3. Undo")
        print("4. Redo")
        print("5. Quit")
        choice = input("Choice: ")
        if choice == "1":
            text = input("Message: ")
            chat.send_message(text)
        elif choice == "2":
            chat.show_history()
        elif choice == "3":
            chat.undo()
        elif choice == "4":
            chat.redo()
        elif choice == "5":
            print("Bye")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

#Output:-
--- Chat Menu ---
1. Send message
2. Show history
3. Undo
4. Redo
5. Quit
Choice: 1
Message: Hello!
Message sent: Hello! [2025-08-21 08:17:54]

--- Chat Menu ---
1. Send message
2. Show history
3. Undo
4. Redo
5. Quit
Choice: 1
Message: How are you?
Message sent: How are you? [2025-08-21 08:17:58]

--- Chat Menu ---
1. Send message
2. Show history
3. Undo
4. Redo
5. Quit
Choice: 2
Message History:
1. Hello! [2025-08-21 08:17:54]
2. How are you? [2025-08-21 08:17:58]

--- Chat Menu ---
1. Send message
2. Show history
3. Undo
4. Redo
5. Quit
Choice: 3
Undo: Removed 'How are you?'

--- Chat Menu ---
1. Send message
2. Show history
3. Undo
4. Redo
5. Quit
Choice: 2
Message History:
1. Hello! [2025-08-21 08:17:54]

--- Chat Menu ---
1. Send message
2. Show history
3. Undo
4. Redo
5. Quit
Choice: 4
Redo: Restored 'How are you?'

--- Chat Menu ---
1. Send message
2. Show history
3. Undo
4. Redo
5. Quit
Choice: 2
Message History:
1. Hello! [2025-08-21 08:17:54]
2. How are you? [2025-08-21 08:17:58]

--- Chat Menu ---
1. Send message
2. Show history
3. Undo
4. Redo
5. Quit
Choice: 5
Bye


