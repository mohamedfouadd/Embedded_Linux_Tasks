import pyautogui
import time

# Open Visual Studio Code
pyautogui.press('win')
time.sleep(1)  
pyautogui.write('visual studio code')
time.sleep(1) 
pyautogui.press('enter')
time.sleep(5)

# Install Clangd extension
pyautogui.hotkey('ctrl', 'p')
time.sleep(1)  
pyautogui.write('ext install llvm-vs-code-extensions.vscode-clangd')
time.sleep(2)
pyautogui.press('enter')
time.sleep(5)

# Install C++ TestMate extension
pyautogui.hotkey('ctrl', 'p')
time.sleep(1) 
pyautogui.write('ext install matepek.vscode-catch2-test-adapter')
time.sleep(2)
pyautogui.press('enter')
time.sleep(5)  

# Install C++ Helper extension
pyautogui.hotkey('ctrl', 'p')
time.sleep(1)  
pyautogui.write('ext install abrasmussen.cpp-helper')
time.sleep(2)
pyautogui.press('enter')
time.sleep(5) 

# Install CMake extension
pyautogui.hotkey('ctrl', 'p')
time.sleep(1) 
pyautogui.write('ext install twxs.cmake')
time.sleep(2)
pyautogui.press('enter')
time.sleep(5)  

# Install CMake Tools extension
pyautogui.hotkey('ctrl', 'p')
time.sleep(1)  
pyautogui.write('ext install ms-vscode.cmake-tools')
time.sleep(2)
pyautogui.press('enter')
time.sleep(5)  
