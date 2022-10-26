import time

Bar = [
    " [ =    ]",
    " [  =   ]",
    " [   =  ]",
    " [    = ]",
    " [     =]",
    " [    = ]",
    " [   =  ]",
    " [  =   ]",
    " [ =    ]",
    " [=     ]",
        ]
Point = [
    "..",
    "...",
    "...."
    "..."
    ".."
    "."
]
i = 0

while i < 500:
    print(Bar[i % len(Bar)], end="\r")
    time.sleep(.2)
    i += 1