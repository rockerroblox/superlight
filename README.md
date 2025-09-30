``` ___ _   _ _ __   ___ _ __| (_) __ _| |__ | |_
/ __| | | | '_ \ / _ | '__| | |/ _` | '_ \| __|
\__ | |_| | |_) |  __| |  | | | (_| | | | | |_
|___/\__,_| .__/ \___|_|  |_|_|\__, |_| |_|\__|
          |_|                  |___/
```

> [!NOTE]
> AWS vulnerabilities through Lightspeed themselves coming soon: CVE-LSE-2025-03 - DBCheck

Superlight is a framework to remove Lightspeed Filter Agent through various methods. Methods include:

    • Extension removal
    • Websocket killer
    • Program killswitch (Work in progress)

The script mainly kills the websocket connections Lightspeed attempts to make to the locally-running WS alert relay system, which then sends via their systems to your schools flagging agent

We use a system called LSE similar to CVE

LSE-2025-01 - Superlight 1 - Websocket Killer\
LSE-2025-02 - Superlight 2 - Decompilation Exploits (TBD)

To fully find out the entire process of Lightspeed I will need to decompile and analyse the initial files. At this current moment I do not possess a Windows virtual machine and you currently cannot download the ISO.

# Unplug - CVE-LSE-2025-01

**Unplug** is an exploit for Lightspeed Filter Agent and **Lightspeed Alert Agent**, although primarily used for Alert Agent. I *do* understand Alert Agent is used for student protection and wellbeing but I like this kinda thing.

The way Alert Agent works is that it uses websockets and extensions/apps, but let's call that your Lightspeed installation. Your Lightspeed will log your searches and match them against the wordlist and have some weird function known in the source code as 'CheckIntent' which dosen't seem to do much except match your query or text against the list. Then it uses websockets to send it to your schools lightspeed.

This is slightly annoying because you can search for something completely innocuous and it gets flagged and then you get called in or sum idk

# Extended Metaphor - CVE-LSE-2025-02

Coming soon...
(weird name I know its a work in progress)
