![main](https://i.imgur.com/K1QLswz.png)
## REQUIREMENTS:
WINDOWS ONLY
```
pip install pywin32
```
## NOTES:
- Will not work on top of a fullscreen application, if you are using this to draw on top of a game, use borderless windowed instead.
- Anything with a black background will be chroma keyed, giving the transparent effect.
- For more informaton about how the transparent window works, check the following Win32 API articles
   - https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setlayeredwindowattributes
   - https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setwindowlonga
   - https://docs.microsoft.com/en-us/windows/win32/winmsg/extended-window-styles
