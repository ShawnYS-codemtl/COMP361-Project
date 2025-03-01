import pygame
import sys
import pygame._sdl2
from control_element.drop_down import DropDown
from control_element.button import Button

#support resize

class Simulation:
    def __init__(self, display, program_state_manager):
        self.display = display
        self.program_state_manager = program_state_manager
        self.sdl2_window = pygame._sdl2.video.Window.from_display_module()

        #MENU
        COLOR_MAIN_INACTIVE = (30,33,38)
        COLOR_MAIN_ACTIVE = (65, 71, 82)
        MENU_TEXT_COLOR = "white"
        MENU_BORDER_RADIUS = 3
        MENU_H = 25
        MENU_Y = 3
        FONT = pygame.font.Font("Inter/Inter-VariableFont_opsz,wght.ttf", 13)   

        #DROP_DOWNS
        DROP_DOWN_COLOR_OPTION_ACTIVE = (65, 71, 82)
        DROP_DOWN_COLOR_OPTION_INACTIVE = (30,33,38)

        PROJECT_OPTIONS = ["New Project", "Load Project", "Save Project", "Delete Project"]

        #Temporary. TODO needs to upgrade button class
        TEMP_OPTION = [":D","ehehe", "》:O", "來財， 來"]

        self.project_drop_down = DropDown("Project", PROJECT_OPTIONS, COLOR_MAIN_INACTIVE, COLOR_MAIN_ACTIVE, DROP_DOWN_COLOR_OPTION_INACTIVE, DROP_DOWN_COLOR_OPTION_ACTIVE,FONT, MENU_TEXT_COLOR, MENU_BORDER_RADIUS, 40, MENU_Y, 55, MENU_H, 150)

        self.select_rover_drop_down = DropDown("Select Rover", TEMP_OPTION, COLOR_MAIN_ACTIVE, (13, 59, 66), DROP_DOWN_COLOR_OPTION_ACTIVE, (	21, 97, 109),FONT, MENU_TEXT_COLOR, 5, display.get_width()/2 - 75, MENU_Y, 250, MENU_H, 250)

        #ICONS TOP
        ICON_W = 30
        CLOSE_ICON = pygame.image.load('images/icon_close.png')
        RESTORE_ICON = pygame.image.load('images/icon_restore.png')
        MINIMIZE_ICON = pygame.image.load('images/icon_minimize.png')

        self.add_rover_button = Button("Add Rover", COLOR_MAIN_INACTIVE, COLOR_MAIN_ACTIVE, FONT, MENU_TEXT_COLOR, MENU_BORDER_RADIUS, 100, MENU_Y, 75, MENU_H)

        self.help_button = Button("Help", COLOR_MAIN_INACTIVE, COLOR_MAIN_ACTIVE, FONT, MENU_TEXT_COLOR, MENU_BORDER_RADIUS, 180, MENU_Y, 45, MENU_H)

        self.close_window_button = Button("Close", COLOR_MAIN_INACTIVE, COLOR_MAIN_ACTIVE, FONT, MENU_TEXT_COLOR, MENU_BORDER_RADIUS, display.get_width() - 40, MENU_Y, ICON_W, MENU_H, CLOSE_ICON, 0.8)

        self.restore_window_button = Button("Restore", COLOR_MAIN_INACTIVE, COLOR_MAIN_ACTIVE, FONT, MENU_TEXT_COLOR, MENU_BORDER_RADIUS, display.get_width() - 75, MENU_Y, ICON_W, MENU_H, RESTORE_ICON, 0.7)

        self.minimize_window_button = Button("Minimize", COLOR_MAIN_INACTIVE, COLOR_MAIN_ACTIVE, FONT, MENU_TEXT_COLOR, MENU_BORDER_RADIUS, display.get_width() - 110, MENU_Y, ICON_W, MENU_H, MINIMIZE_ICON, 0.8)

        #ICONS SIDE
        S_ICON_X = 3
        S_ICON_H = 25

        ERROR_ICON = pygame.image.load('images/icon_error.png')
        SETTING_ICON = pygame.image.load('images/icon_setting.png')
        VISIBILITY_ICON = pygame.image.load('images/icon_visibility.png')

        self.error_button = Button("Error", COLOR_MAIN_INACTIVE, COLOR_MAIN_ACTIVE, FONT, MENU_TEXT_COLOR, MENU_BORDER_RADIUS, S_ICON_X, display.get_height() - 110, ICON_W, S_ICON_H, ERROR_ICON, 0.8)

        self.view_data_button = Button("View", COLOR_MAIN_INACTIVE, COLOR_MAIN_ACTIVE, FONT, MENU_TEXT_COLOR, MENU_BORDER_RADIUS, S_ICON_X, display.get_height() - 75, ICON_W, S_ICON_H, VISIBILITY_ICON, 0.8)

        self.setting_button = Button("Setting", COLOR_MAIN_INACTIVE, COLOR_MAIN_ACTIVE, FONT, MENU_TEXT_COLOR, MENU_BORDER_RADIUS, S_ICON_X, display.get_height() - 40, ICON_W, S_ICON_H, SETTING_ICON, 0.8)



    

    def draw_window(self):

        SIMULATION_WINDOW_X = 40
        SIMULATION_WINDOW_Y = 30
        SIMULATION_WINDOW_W = self.display.get_width() - 40
        SIMULATION_WINDOW_H = self.display.get_height() - 30
        SIMULATION_SCREEN_COLOR = (48,48,49)
        simulation_window = pygame.Rect(SIMULATION_WINDOW_X,SIMULATION_WINDOW_Y,
        SIMULATION_WINDOW_W,SIMULATION_WINDOW_H)
        pygame.draw.rect(self.display, SIMULATION_SCREEN_COLOR, simulation_window)

        self.project_drop_down.draw(self.display)
        self.select_rover_drop_down.draw(self.display)
        self.add_rover_button.draw(self.display)
        self.help_button.draw(self.display)
        self.close_window_button.draw(self.display)
        self.restore_window_button.draw(self.display)
        self.minimize_window_button.draw(self.display)

        self.error_button.draw(self.display)
        self.view_data_button.draw(self.display)
        self.setting_button.draw(self.display)

        

    def run(self, events):
        self.display.fill((30,33,38))

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    pygame.quit()
                    sys.exit()

        #Title Bar Logic
        project_dragdown_option = self.project_drop_down.update(events)
        rover_select_dragdown_option = self.select_rover_drop_down.update(events)
        self.add_rover_button.update(events)
        self.help_button.update(events)
        self.close_window_button.update(events)
        self.restore_window_button.update(events)
        self.minimize_window_button.update(events)
        
        #Handle Window Control
        if self.close_window_button.is_clicked:
            pygame.quit()
            sys.exit()
        if self.minimize_window_button.is_clicked:
            self.sdl2_window.minimize()

        #Side Bar Logic
        self.setting_button.update(events)
        self.error_button.update(events)
        self.view_data_button.update(events)

        self.draw_window()

    def get_size(self):
        return self.width, self.height
        
