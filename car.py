
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import time\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create our body classifier\n",
    "car_classifier = cv2.CascadeClassifier('haarcascade_car.xml')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Initiate video capture for video file\n",
    "cap = cv2.VideoCapture('C:/Users/gaurav sahani/Desktop/Machine LearningOpenCV/cars2.avi')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<VideoCapture 000001CB9ABC0F90>"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cap"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Loop once video is successfully loaded\n",
    "while cap.isOpened():\n",
    "    \n",
    "    time.sleep(.05)\n",
    "    # Read first frame\n",
    "    ret, frame = cap.read()\n",
    "    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)\n",
    "   \n",
    "    # Pass frame to our car classifier\n",
    "    cars = car_classifier.detectMultiScale(gray, 1.4, 2)\n",
    "    \n",
    "    # Extract bounding boxes for any bodies identified\n",
    "    for (x,y,w,h) in cars:\n",
    "        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)\n",
    "        cv2.imshow('Cars', frame)\n",
    "\n",
    "    if cv2.waitKey(1) ==13: #13 is the Enter Key\n",
    "        break\n",
    "        \n",
    "cap.release()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count":0,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
