# trafficLightGame
Traffic light game created using a Python GUI with tkinter. 

User can guess a number or word of different lengths, with a user defined numbers of attempts. 

## Building the application using PyInstaller
```
pyinstaller trafficLightGame.py --add-data="path/to/trafficLightGame/Lib/site-packages/english_words;english_words" --onefile
```
This packages the GUI application and external english_words package into a single executable in a `dist` folder of the repository directory.

## Running the GUI application
Locate the executable in the `dist` folder of the repository directory and run it.

Alternatively if already in repository directory on command line, can run the command below
```
./dist/trafficLightGame.exe
```

## Playing Game
When running the GUI application, you will first be presented with the options screen. Here you can select the game mode (Number or Word), number of characters, and number of attempts. The default options are shown below:

![image](https://user-images.githubusercontent.com/57740952/178166448-798c9fcc-1165-4845-aa00-81285cba45e9.png)

Once you have selected the game options, click the "Start Game" button or simply press enter to start the game.

### Number Mode
When playing in the number mode, you can only enter digits in each entry. Red indicates that the digit is not part of the number. Orange indicates that the digit is part of the number but does not have the correct place value. Green indicates that the digit is part of the number and has the correct place value.

A full game in the number mode is shown below:

![image](https://user-images.githubusercontent.com/57740952/178166650-08fbf221-cd16-416c-9ba6-dc8b319a3969.png)

### Word Mode
When playing in the word mode, you can only enter letters in each entry. Letters are automatically capitalised as you type. Red indicates that the letter is not part of the word. Orange indicates that the letter is part of the word but is in the wrong place. Green indicates that the letter is part of the word and is in the right place.

A full game in the word mode is shown below:

![image](https://user-images.githubusercontent.com/57740952/178166925-fbfca746-a57e-4b6d-ac43-b8b7f3c7e303.png)

### Game control and error handling
As you enter a character in an entry, the program validates the character to check that it is a valid digit or letter, and then automatically moves the cursor to the next entry. This means that you can just type a number or word without having to manually hit tab to move to the next entry each time. You can also press backspace within an entry to remove a character and hold down backspace to remove multiple characters. 

When you are ready to check your answer, click the "Submit" button or simply press enter. If you have not entered a character in each entry, you will be presented with the error message below.

![image](https://user-images.githubusercontent.com/57740952/178167220-24744685-834d-48c6-af69-fb4e4d38e1f7.png)

The number of attempts you make is updated each time you enter a valid number or word. If you successfully find the number or word within the maximum number of attempts you have set, you will be shown the number of attempts you took to find it. If not, you will be shown the correct number or word as shown below.

![image](https://user-images.githubusercontent.com/57740952/178167895-97308586-0305-4413-9491-bb5aa7283105.png)

After you have finished a game, you can click the "Play Again" button or simply press enter to play again with the same game mode but a different number or word. You can also click "Change Mode" after a game is finished or at any time during a game, to change the game options and start a new game.

