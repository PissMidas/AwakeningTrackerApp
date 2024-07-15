from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import tkinter as tk
from tkinter import messagebox, ttk
import os
import re
import sys
import pygetwindow
import time
from PIL import Image, ImageTk

#pyinstaller --onefile --icon=images/dubu.ico --add-data "images;images" --noconsole --name "AwakeningTracker" tk.py
#command line to compile

#pyinstaller --onedir --icon=images/dubu.ico --add-data "images;images" --noconsole --name "AwakeningTracker" tk.py
#alternative command line to compile. (antivirus less likely to have a false positive)




def resourcePath(relativePath):
    #Get absolute path to resource, works for dev and for PyInstaller
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        basePath = sys._MEIPASS
    except Exception:
        basePath = os.path.abspath(".")

    return os.path.join(basePath, relativePath)


image_cache = {}
class LogEventHandler(FileSystemEventHandler):
    def __init__(self, log_file_path, main_window):
        super().__init__()
        self.log_file_path = log_file_path
        self.main_window = main_window
        self.file_size = 0
    #    self.assigned_team_time = None
    #    self.assigned_team = None

    def on_modified(self, event):
        if not event.is_directory and event.src_path == self.log_file_path:
            # Get the size of the modified file
            current_size = os.path.getsize(self.log_file_path)

            # Read only the newly added content since the last modification
            with open(self.log_file_path, "r") as file:
                file.seek(self.file_size)
                new_content = file.read()

            # Update the file size
            self.file_size = current_size

            # Process the new log messages
            log_lines = new_content.splitlines()
            for line in log_lines:

                if 'StreamTeamLevel' in line or 'Training Class' in line or 'Application Will Terminate' in line or 'PostGameCelebration' in line or 'EMatchPhase::VersusScreen' in line or 'EMatchPhase::Intermission' in line or 'EMatchPhase::ArenaOverview' in line or "Server Disconnect Reasons":
                    #print(line) #USED FOR DEBUGGING
                    # Call the Tkinter event function here
                    self.main_window.event_function(line)

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AwakeningTracker v0.0.16") #v0.0.16 7/11/2024



        self.master_copy_deck = ['TD_AvoidDamageHitHarder', 'TD_BarrierBuff', 'TD_BaseStaggerAndRegen', 'TD_BlessingCooldownRate', 'TD_BlessingMaxStagger', 'TD_BlessingPower', 'TD_BlessingShare', 'TD_BlessingSpeed', 'TD_BuffAndDebuffDuration', 'TD_ComboATarget', 'TD_CreationSize', 'TD_CreationSizeLifeTime', 'TD_DistancePower', 'TD_EdgePower', 'TD_EmpoweredHitsBuff', 'TD_EnergyCatalyst', 'TD_EnergyConversion', 'TD_EnergyDischarge', 'TD_EnhancedOrbsCooldown', 'TD_EnhancedOrbsSpeed', 'TD_FasterDashes', 'TD_FasterDashes2', 'TD_FasterDashes3', 'TD_FasterProjectiles', 'TD_FasterProjectiles2', 'TD_FasterProjectiles3', 'TD_HitAnythingRestoreStagger', 'TD_HitEnemyBurnThem', 'TD_HitRockCooldown', 'TD_HitsIncreaseSpeedAndPower', 'TD_HitSpeed', 'TD_HitsReduceCooldowns', 'TD_IncreasedSpeedWithStagger', 'TD_KOKing', 'TD_MovementAbilityCharges', 'TD_MultiHitsReduceCooldowns', 'TD_OrbShare', 'TD_PrimaryAbilityCooldownReduction', 'TD_PrimaryEcho', 'TD_ResistFirstHit', 'TD_Revive', 'TD_ShrinkSelfGrowAllies', 'TD_SizeIncrease', 'TD_SizeIncrease2', 'TD_SizePowerConversion', 'TD_SpecialCooldownAfterRounds', 'TD_StackingSize', 'TD_StaggerCooldownRateConversion', 'TD_StaggerPowerConversion', 'TD_StaggerSpeedConversion', 'TD_StrikeCooldownReduction', 'TD_StrikeRockTowardsAllies', 'TD_TakeDownReduceCooldowns']


        # List of items to remove
        items_to_remove = ['TD_EdgePower', 'TD_BarrierBuff', 'TD_CreationSizeLifeTime',
          'TD_SizeIncrease', 'TD_EnergyConversion',
         'TD_HitSpeed', 'TD_EnergyDischarge', 'TD_OrbShare',
         'TD_BlessingCooldownRate', 'TD_BlessingMaxStagger', 'TD_BlessingPower', 'TD_BlessingShare', 'TD_BlessingSpeed',
         'TD_IncreasedSpeedWithStagger', 'TD_FasterDashes', 'TD_HitAnythingRestoreStagger',
         'TD_EmpoweredHitsBuff', 'TD_Revive', 'TD_ShrinkSelfGrowAllies'
         ]

    # Remove items from self.master_copy_deck
        self.master_copy_deck = [item for item in self.master_copy_deck if item not in items_to_remove]


        self.hidden_deck = self.master_copy_deck.copy()
        self.shown_deck = []
        self.shown_deck_check_after_gui_updates= []
        self.build_image_cache()
        self.resizable(False, False)
        icon_path = resourcePath("images/dubu.ico")  # Replace with the actual path to your icon file
        self.iconbitmap(default = icon_path)
        self.wm_iconbitmap(icon_path)
    def build_image_cache(self):
        global image_cache
        for card_name in self.hidden_deck:
            image_path = resourcePath(f"images/{card_name}.png")
            image = Image.open(image_path)
            image = image.resize((56, 56))
            photo = ImageTk.PhotoImage(image)
            image_cache[image_path] = photo

        for card_name in self.shown_deck:
            image_path = resourcePath(f"images/{card_name}.png")
            image = Image.open(image_path)
            image = image.resize((56, 56))
            photo = ImageTk.PhotoImage(image)
            image_cache[image_path] = photo


    def event_function(self, message):
        # Your custom event handling logic here

        if 'Training Class' in message:

            # then we need to process it!
            #print(message) #USED FOR DEBUGGING
            pattern = r"Training Class '([^']+)'"
            match = re.search(pattern, message)

            if match:
                extracted_word = match.group(1)
                #print(extracted_word) #USED FOR DEBUGGING
                if extracted_word in self.hidden_deck:
                    tempcard = self.hidden_deck.remove(extracted_word)
                    if extracted_word in self.shown_deck:
                        return
                    self.shown_deck.append(extracted_word)



        elif 'Application Will Terminate' in message:
            print('GAME HAS EXITED, TERMINATING TRACKER APP')
            self.destroy()
            sys.exit()

        elif 'PostGameCelebration' in message or "Server Disconnect Reasons" in message:
            self.reset_decks()

        elif 'EMatchPhase::VersusScreen' in message or 'EMatchPhase::IntermissionIntro, EMatchPhase::Intermission' in message or 'EMatchPhase::ArenaOverview' in message:
            self.draw_cards()

    def reset_decks(self):
        self.hidden_deck = self.master_copy_deck.copy()
        self.shown_deck = []

    def draw_cards(self, first_draw_flag=False):
        global image_cache  # Access the global image_cache variable
        # self.after(200, self.update)

        if first_draw_flag == True:
            # then we don't want to return! and draw the awakenings!
            pass
        elif set(self.shown_deck_check_after_gui_updates) == set(self.shown_deck):
            return
        # Clear the existing cards from the window
        for widget in self.winfo_children():
            widget.destroy()




        hidden_label = tk.Label(self, text="Hidden Awakenings", font=("Helvetica", 16, "bold"))
        hidden_label.grid(row=0, column=0, columnspan=6)

        # Display hidden cards grid
        hidden_deck_cols = 0
        hidden_deck_row = 1  # Updated row value
        for card_name in self.hidden_deck:
            image_path = resourcePath(f"images/{card_name}.png")
            photo = image_cache.get(image_path)

            # Create a label for the image
            label = tk.Label(self, image=photo)
            label.grid(row=hidden_deck_row, column=hidden_deck_cols % 6, padx=0, pady=0)

            hidden_deck_cols += 1
            if hidden_deck_cols >= 6:
                hidden_deck_cols = 0
                hidden_deck_row += 1

        shown_label = tk.Label(self, text="Shown Awakenings", font=("Helvetica", 16, "bold"))
        shown_label.grid(row=hidden_deck_row + 1, column=0, columnspan=6)

        total_rows = hidden_deck_row + (len(self.shown_deck) // 6) + 1  # Updated row value
        shown_deck_row = hidden_deck_row + 2  # Updated row value

        shown_deck_cols = 0
        for card_name in self.shown_deck:
            image_path = resourcePath(f"images/{card_name}.png")
            photo = image_cache.get(image_path)

            label = tk.Label(self, image=photo)
            label.grid(row=shown_deck_row, column=shown_deck_cols % 6, padx=0, pady=0)

            shown_deck_cols += 1
            if shown_deck_cols >= 6:
                shown_deck_cols = 0
                shown_deck_row += 1

        shown_label.grid_configure(row=hidden_deck_row + 1, column=0, columnspan=6)
        self.shown_deck_check_after_gui_updates = self.shown_deck.copy()

def is_omega_strikers_window_open():
    game_title = "OmegaStrikers"
    windows = pygetwindow.getAllWindows()
    for window in windows:
        if game_title in window.title:
            return True
    return False
# Rest of the code
# Create the main Tkinter window


# Show a message box dialog if OmegaStrikers window is not found
if not is_omega_strikers_window_open():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    # Show a message box dialog
    messagebox.showinfo("Message", "Omega strikers not found. Exiting app.")
    sys.exit()

# Create an instance of your Tkinter window class
window = MainWindow()
window.draw_cards(True)

# Create the log file path
log_file_path = os.path.join(os.getenv('LOCALAPPDATA'), 'OmegaStrikers', 'Saved', 'Logs', 'OmegaStrikers.log')

# Create an instance of LogEventHandler and pass the Tkinter window reference
time.sleep(1)
log_handler = LogEventHandler(log_file_path, window)
time.sleep(2)
# Create the watchdog observer and start monitoring
observer = Observer()
time.sleep(1)
observer.schedule(log_handler, os.path.dirname(log_file_path), recursive=False)
time.sleep(1)
observer.start()
time.sleep(1)
# Start the Tkinter event loop
window.mainloop()
