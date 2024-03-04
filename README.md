# NowayBankrupt
A money tracking mini-app website with Flask for using in home, local network, with any device.

  This project based on a simple design. A big yellow button scheme on top, and other schemes on bottom.
I made design as simple as possible. Website is Turkish language originally but it could be translated easily.
It does have at most two sentences except version logs.

## Start Up
Firstly a tip: This app is working best on horizontal display. So, I recommend a experiment with a 
verticular browser.

When venv is started and the flask is up, go to the website. There's the app.

```bash
. venv/bin/activite
flask --app application run --host {local ip address here}
```
## Usage
It is simple. There is a yellow button bar on top for doing main stuff.
And in the bottom, page specific stuff.

In index page, you should see two buttons in button bar, that a minus and plus.
One is for adding a "money increase log" and one is for "money deacrease log".
Can you guess witch one is witch? Click one of them. Now you're in the "log"
page. Left one is title, and right one is amount of money. Type something to
there. And click the button at a bit down of text boxes. Now you'll back on
the index page. Based on your log type, there will be a color. And that
color will be more colorful if amount of money is high, or will be more
close to white if amount of money is low. If you didn't liked your log, 
tap the button at the right side of your log. That would destroy your log.
But in the case of liking the log, you can tap directly at your log and see
its details.

And finally, at bottom of every page, you'll see the version number. If you tap
it, you'll gonna be directed to version logs.
