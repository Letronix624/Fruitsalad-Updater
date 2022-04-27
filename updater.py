import os, zipfile, tkinter, time, requests, threading, sys,json
from win32api import GetSystemMetrics
def update():
    if sys.executable.endswith("python.exe"):
        pydir = os.path.dirname(os.path.realpath(__file__))
    else:
        pydir = sys.executable[:-12]
    try:
        version = requests.get('http://seflon.ddns.net/secret/version.txt').text
    except:
        window.quit()
        os._exit(0)
    global display
    display.configure(text="Downloading")
    #download
    filename = "hello.howareyou"
    with requests.get(f"https://github.com/Letronix624/Fruit-Salad/releases/download/{json.loads(requests.get('https://api.github.com/repos/Letronix624/Fruit-Salad/releases').text)[0]['tag_name']}/FruitSalad.zip", stream=True) as r:
        print('Downloading Package')
        r.raise_for_status()
        with open(f"{pydir}//{filename}", 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        print("Package made")
    display.configure(text="Extracting")
    print(f"Extracting files to {pydir}")
    with zipfile.ZipFile(f"{pydir}\\{filename}", "r") as data:
        data.extractall(pydir)
    print(f'Downloaded Fruit Salad {version}')
    display.configure(text="Version "+version)
    os.remove(f"{pydir}\\{filename}")
    try:
        os.startfile(f"{pydir}\\FruitSalad.exe")
    except: display.configure(text="No?? Ok..")
    time.sleep(1)
    os._exit(0)
window = tkinter.Tk()
window.geometry("400x100+"+str(GetSystemMetrics(0)/2-200)[:-2]+"+"+str(GetSystemMetrics(1)/2-50)[:-2])
window.overrideredirect(True)
window.resizable(False, False)
window.attributes('-topmost', True)
font = ("Miriam Libre", 35)
window.configure(background="#C4C4C4")
tkinter.Canvas(window, bg="#C4C4C4", highlightthickness=10, highlightbackground="black").place(x=2,y=2,width=396,height=96)
display = tkinter.Label(window, text="Starting", bg="#C4C4C4", font=font, fg="black")
display.place(x=12,y=12, width=400-24, height=100-24)
threading.Thread(target=update).start()
window.mainloop()