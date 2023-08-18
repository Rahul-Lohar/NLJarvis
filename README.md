# NL Jarvis(Just a Rather Very Intelligent System)
A.I Voice Assistant
#### This was my attempt to make a voice assistant similar to JARVIS (in iron man movie)
#### Let's be honest, it's not as intelligent as in the movie, but it can do a lot of cool things and automate your daily tasks you do on your personal computers/laptops.
## Built with

<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code>

## Features

It can do a lot of cool things, some of them being:

- Tell current time and date
- Launch applications/softwares 
- Open any website
- Tells about any person (via Wikipedia)
- Can search anything on Google 
- Can take screenshot and save it with custom filename


## Installation
  -First Clone the repo
  - Make reuired path changes according to your convenience of folder path for reuired features.
  - Run Trained.py file
  - After Running Trained.py file Run Jarvis.py File.
  - 
## Code Structure


    ├── NLJarvis             # Main folder for features 
    │   ├── Database          # Contains required files.
    │   ├── features        # All functionalities of JARVIS 
    ├── requirements.txt    # all dependencies of the program

- The code structure if pretty simple. The code is completely modularized and is highly customizable
- To add a new feature:
  -  Make a new python file of feature or can edit Task.py file, write the feature's function you want to include
  - Make edit in intents,json file with possible words or command to execute the feature.
  - edit Jarvis.py to call function of required feature.


## Contribute
Please read [CONTRIBUTING.md](https://github.com/Gladiator07/JARVIS/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## License
This project is licensed under [MIT License](https://github.com/Rahul-Lohar/NLJarvis/blob/22eed329c71df792d4981edc3a30a3277629455e/LICENSE) 2023 Rahul Lohar

## Future Improvements
- GUI can be made for easy interaction with jarvis.
- More functionalities can be added
