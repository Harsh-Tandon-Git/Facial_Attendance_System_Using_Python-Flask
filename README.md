App.py file contains the initialization of FLASK application along with the CSV file that contains the attendance and updates on realtime.
Add_faces.py file contains the functionality to register users for the first time to train the model. It will click 5 samples of your face in one go and by using haarCascade model, it will extract features from your face and using euclidean distance it will compare the faces for recognition.
recognise_faces.py contains the functionality to recognise your faces for marking the attendance. By pressing "O" from your keyboard after initiating webcam, you will hear a sound "Attendance Taken" and your attendance will mark along with your name and time on realtime basis because of DateTime library of python.
After recognising your face, it will wait for 3 secs and ready again for recognising new face until you press "q" from the keyboard to stop it.
The attendance will automatically update in the datebase and you can download that updated CSV file from the GUI.

The below commands will help you in executing the program:
python app.py
python Add_faces.py
python recognise_faces.py

Note: Make sure you install all the python libraries that are imported in the project before executing, otherwise you will encounter alot of warnings and errors.
