import os

shape_predictor_path    = os.path.join('data','shape_predictor_68_face_landmarks.dat')
alarm_paths             = [os.path.join('data','audio_files','wakeup.wav'),
                           os.path.join('data','audio_files','break.wav'),
                           os.path.join('data','audio_files','road.wav')]

EYE_DROWSINESS_THRESHOLD    = 0.25
EYE_DROWSINESS_INTERVAL     = 5.0
MOUTH_DROWSINESS_THRESHOLD  = 0.35
MOUTH_DROWSINESS_INTERVAL   = 1.0
DISTRACTION_INTERVAL        = 3.0
