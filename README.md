# smart-cctv
A research study presented to Laguna State Polytechnic University entitled "Comparison of YOLO and SSD for Weapon Detection on CCTV - Input to Crime Prevention", built with Python and Django.

## Requirements and Dependencies
1. Python 3.7
   - Download [Python 3.7](https://www.python.org/downloads/release/python-370/) and install it to your local machine.

2. Django 4.0.7
3. OpenCV 4.5.4
   - Repository [link](https://github.com/spmallick/learnopencv/tree/master/InstallScripts) for installing OpenCV to Windows.

4. Darknet (YOLO Backbone)
   - Repository [link](https://github.com/AlexeyAB/darknet) for installing Darknet to Windows.


## Getting Started - Installation
1. After satisfying the requirements and dependencies, Python 3.7, OpenCV 4.5.4, and Darknet (YOLO Backbone). 
2. Download and extract the project’s repository at this [URL](https://github.com/Ming-desu/smart-cctv).
3. Open the command prompt and navigate to the project’s directory. We need to create a virtual environment so we do not affect other projects in Python. Type the following to the command prompt:

    ```
    python -m venv .venv
    ```
    
4. Activate the virtual environment by navigating to the .venv/Scripts folder generated from the previous command or simply type this command from the terminal.

    ```
    cd .\.venv\Scripts\ && .\activate && cd .. && cd ..
    ```
    
5. We can install the dependencies of the project, simply type the following command.

    ```
    python -m pip install –upgrade pip && pip install -r requirements.txt
    ```
    
    ![Dependencies Installation](https://github.com/Ming-desu/smart-cctv/blob/main/screenshots/installation.png?raw=true "Requirement and Dependencies Installation")
    
    Your terminal should contain something like this, to ensure that installation was successful.

6. To run the server, all we need to do is to type the following command to the terminal. This will run the local server and can be accessed via browser with port 80.

    ```
    cd .\smart_cctv && python manage.py runserver 80
    ```
    
    ![Running Server](https://github.com/Ming-desu/smart-cctv/blob/main/screenshots/running-server.png?raw=true "Running Server")
    
    Your logs should be almost the same as the one presented above, if yes then we can navigate to the application by accessing [http://127.0.0.1/](http://127.0.0.1/) in the web browser.
    
## Application Usage
1. Navigate to [http://127.0.0.1/auth](http://127.0.0.1/auth), here you will see a login page, containing a field for the username and password along with a single button to sign in. Input the default credentials.
    
    ```
    Username: admin
    Password: admin
    ```
    
    ![Login UI](https://github.com/Ming-desu/smart-cctv/blob/main/screenshots/login-ui.jpg?raw=true "Login UI")
    
2. After logging in, you should see something like the image below, which contains a sidebar menu at the left side, and the main content section to the right side.

    ![Main UI](https://github.com/Ming-desu/smart-cctv/blob/main/screenshots/main-ui.jpg?raw=true "Main UI")
    
3. When managing or adding a new CCTV camera record, simply navigate to [http://127.0.0.1/cameras](http://127.0.0.1/cameras) or click the Camera item from the sidebar menu. It will redirect you to another page which contains the records of CCTV cameras, a search box, and a button for creating a new record.

    ![Camera UI](https://github.com/Ming-desu/smart-cctv/blob/main/screenshots/camera-ui.jpg?raw=true "Camera UI")
    
    You can edit individual records to update the information or as well as to change credentials of the cameras.
    
    ![Camera Edit UI](https://github.com/Ming-desu/smart-cctv/blob/main/screenshots/camera-edit-ui.jpg?raw=true "Camera Edit UI")
    
    When creating a new camera record, please do take note that this system only works for cameras that support Real-time Streaming Protocol or RTSP, this can be accessed by the camera’s IP address, and if it has credentials such as username and password, then it should be as well provided. The common pattern of the connection string is something like this.
    
    ```
    rtsp://username:password@ip_address:port/stream_path
    ```
    
    The part where stream_path lies, comes from the manufacturer of the camera itself, if the camera supports RTSP protocol, then most likely you can ask the manufacturer or even read the manual for the stream_path of the camera.
    
    ![Camera Create UI](https://github.com/Ming-desu/smart-cctv/blob/main/screenshots/camera-create-ui.jpg?raw=true "Camera Create UI")
    
4. In managing users who can access the system, simply navigate to [http://127.0.0.1/users](http://127.0.0.1/users) or click the users from the menu at the left side of the screen. This will redirect you to another page where you can find a text box for searching records, current available records, and a button for creating new one.

    ![User UI](https://github.com/Ming-desu/smart-cctv/blob/main/screenshots/user-ui.jpg?raw=true "User UI")
    
    You can only edit individual records if the account has the type of Admin, if not then the only record you can update is your own information.
    
    ![User Edit UI](https://github.com/Ming-desu/smart-cctv/blob/main/screenshots/user-edit-ui.jpg?raw=true "User Edit UI")
    
    In creating a new user, keep in mind that there are two roles available, Admin and Operator, the Admin can access everything. While Operator on the other hand has limited transactions, such as viewing Streams, Managing Cameras, and Profile only.
    
## Bugs and Feature Requests
Encountered a bug? [Report bug](https://github.com/Ming-desu/smart-cctv/issues/new?template=bug.md)
Have feature request? [Request feature](https://github.com/Ming-desu/smart-cctv/issues/new?template=feature.md&labels=feature)


## Copyright and License
The source code and documentation copyright 2020-2021 the authors. Code released under the [MIT License](https://github.com/Ming-desu/smart-cctv/blob/master/LICENSE)
Have a nice day and enjoy! :metal:
