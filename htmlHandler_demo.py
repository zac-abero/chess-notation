import webbrowser
import sched, time


gif = 'gifs/SwimmingHorse.gif'

f = open('gifpage.html', 'w')

html_template = """

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport"
     content="width=device-width,
      initial-scale=1.0">
    <title>Inline CSS GIF Background</title>
</head>

<body>
    <div
        style="background-image: url("""+ gif +"""); 
                background-size: 100%;
               background-repeat: no-repeat; 
               background-position: center center;
               height: 100vh;">
    </div>
</body>

</html>

"""

f.write(html_template)

f.close()
webbrowser.open('gifpage.html') # open html file

def change_gif(scheduler):
    scheduler.enter(5, 1, change_gif, (scheduler,))
    print("changing gif..")
    
    gif =   'gifs/Soldier_Bird.gif'
    
    f = open('gifpage.html', 'w')
    
    html_new = """
        <!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport"
            content="width=device-width,
            initial-scale=1.0">
            <title>Inline CSS GIF Background</title>
        </head>

        <body>
            <div
                style="background-image: url("""+ gif +"""); 
                        background-size: 100%;
                    background-repeat: no-repeat; 
                    background-position: center center;
                    height: 100vh;">
            </div>
        </body>

        </html>

        """
    f.write(html_new)
    f.close()
    webbrowser.open('gifpage.html', new = 0) # open html file

    
my_scheduler = sched.scheduler(time.time, time.sleep)
my_scheduler.enter(5, 1, change_gif, (my_scheduler,))
my_scheduler.run()
