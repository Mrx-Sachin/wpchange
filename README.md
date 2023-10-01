# Automatic Wallpaper Changer

This Python script allows you to automatically set your desktop wallpaper based on the time of day. It dynamically selects wallpapers from designated folders to match your current time, creating a visually immersive experience.
### Previews

|Aurora|Beach|Bitday|Chihuahuan|
|--|--|--|--|
|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/aurora.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/beach.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/bitday.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/chihuahuan.gif)|

|Cliffs|Colony|Desert|Earth|
|--|--|--|--|
|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/cliffs.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/colony.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/desert.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/earth.gif)|

|Exodus|Factory|Forest|Gradient|
|--|--|--|--|
|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/exodus.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/factory.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/forest.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/gradient.gif)|

|Home|Island|Lake|Lakeside|
|--|--|--|--|
|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/home.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/island.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/lake.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/lakeside.gif)|

|Market|Mojave|Moon|Mountains|
|--|--|--|--|
|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/market.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/mojave.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/moon.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/mountains.gif)|

|Room|Sahara|Street|Tokyo|
|--|--|--|--|
|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/room.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/sahara.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/street.gif)|![gif](https://raw.githubusercontent.com/adi1090x/files/master/dynamic-wallpaper/tokyo.gif)|


## Features

- Seamless transition between morning, afternoon, evening, and night wallpapers.
- Customizable wallpaper folders for each time of day.
- Easily change the wallpaper folder by pressing 'y' and providing the new directory path.
- Persists the last selected wallpaper folder in a 'path.txt' file.
- Simple and user-friendly interface using the console.

## Prerequisites

Before you can use this script, you'll need:

- Windows OS (the script uses Windows API for wallpaper change).
- Python 3.x installed on your system.
- Basic knowledge of using the command prompt.

## Installation

1. Clone this repository to your local machine:

```
git clone https://github.com/Mrx-Sachin/wpchange.git
```
2. Navigate to the project directory:

```
cd wpchange
```

3. Run the script:
```
python wpchange.py
```



## Usage

1. When the script starts, it will display a console window.
2. By default, it will load wallpapers from the previously selected folder (stored in 'path.txt').

- To change the wallpaper folder, press 'y', and a file dialog will appear.
- Navigate to the folder containing wallpapers for the current time of day and select it.
- The script will update the wallpaper and store the new folder path.

3. The wallpaper will automatically change based on the time of day:

- Morning (0-9 AM)
- Afternoon (10 AM - 4 PM)
- Evening (5-9 PM)
- Night (10 PM - 11:59 PM)

4. To manually update the wallpaper, press 'n'.

### Automating the Script

You can set up this script to run automatically at specific intervals using a cron job (on Linux/macOS) or Task Scheduler (on Windows). Here's how to do it:

#### On Windows using Task Scheduler

1. Open the Task Scheduler application.

2. Click "Create Basic Task" and follow the wizard to create a new task.

3. In the "Action" step, select "Start a program" and browse to the location of your Python script.

4. Choose the desired trigger (e.g., daily, hourly) and set the schedule according to your preferences.

5. Complete the wizard, and the script will run automatically based on the schedule you defined.

Now, your wallpaper will change automatically without any manual intervention, enhancing your desktop experience.

