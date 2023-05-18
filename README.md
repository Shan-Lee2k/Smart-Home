# Smart-Home
Connect IoT Gateway to Server:
### NOTE: To using this project you need to load your file "face_recognition.h5" to folder.

## HOW TO USE MY PROJECT

### Module1: PERFORM FACE RECOGNITION TO OPEN DOOR:

**Step 1: Open file "DEMO.py"**

- Comment line threading.Thread(target=speech_recognition).start() and run :

**Step 2: Run**
```
python DEMO.py
```

**Step 3: Before Recognizing Face**

![image](https://github.com/Shan-Lee2k/Smart-Home/assets/120365693/b572372c-1d62-4f8d-82f8-e20e4517c084)

**After Recognizing Face**

![image](https://github.com/Shan-Lee2k/Smart-Home/assets/120365693/df92f236-19dd-48f5-870c-f403c5b74538)



### Module2: PERFORM SPEECH RECOGNITION:

**Step 1: Uncomment line threading.Thread(target=speech_recognition).start()**

**Step 2: Comment line threading.Thread(target=face_recognition).start()**

**Step 3: Run file "DEMO.py"" to perform Speech Recognition**
```
python DEMO.py
```
**Step 4: Issue the command "OK Turn on/off the light"**

- TURN ON:


![image](https://github.com/Shan-Lee2k/Smart-Home/assets/120365693/93537d86-89b5-43be-88e3-288c22686bc7)


- TURN OFF:


![image](https://github.com/Shan-Lee2k/Smart-Home/assets/120365693/ed9fa370-088a-43a4-8d32-f05f5011e286)




