# Vokaturi
pypi package for the Vokaturi emotion classifier for Linux and Mac
for more detailed information see (https://developers.vokaturi.com/getting-started/overview)

# Use

```python
from vokaturi import Vokaturi

emotion = Vokaturi.detect(myAudioFile)
```
the above requires 
- [FFmpeg]

[ffmpeg]: https://ffmpeg.org/download.html

optionally you will not need ffmpeg if your audio file is already .wav format.
in that case 

```python
from vokaturi import Vokaturi

emotion = Vokaturi.detect(myAudioFile, False)
```