# FRM
### Friend Relationship Manager

Some people might have problems getting in touch with friends and family, specialy those who live away. In order to keeep track
 of social desires of talking with and meeting people we like, this is a backend service that handles friends list with alert 
frequencies and exposes alert data with an api.

Written in python.

### File Structure

.\
├── README.md\
├── src\
│   ├── frm\
│   │   ├── Business\
│   │   │   ├── __init\__.py\
│   │   │   ├── RequestHandler.py\
│   │   │   ├── Scheduler.py\
│   │   │   └── UserBusiness.py\
│   │   ├── Domain\
│   │   │   ├── Alert.py\
│   │   │   ├── __init\__.py\
│   │   │   └── User.py\
│   │   ├── frm.py\
│   │   ├── Repository\
│   │   │   ├── AlertRepository.py\
│   │   │   ├── BaseRepository.py\
│   │   │   ├── __init\__.py\
│   │   │   └── UserRepository.py\
│   │   └── Util\
│   │       ├── Constants.py\
│   │       └── __init\__.py\
│   └── requirements.txt\
└── tests\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
├── __init\__.py\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
└── samples_test.py