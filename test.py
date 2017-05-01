import time
from ezprogbar import ProgressBar

pb = ProgressBar(140)

for i in range(140):
    time.sleep(0.1)
    pb.advance()

