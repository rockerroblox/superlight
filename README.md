``` ___ _   _ _ __   ___ _ __| (_) __ _| |__ | |_
/ __| | | | '_ \ / _ | '__| | |/ _` | '_ \| __|
\__ | |_| | |_) |  __| |  | | | (_| | | | | |_
|___/\__,_| .__/ \___|_|  |_|_|\__, |_| |_|\__|
          |_|                  |___/
```
![Badge](https://badgen.net/static/Superlight/1.0/cyan)![Badge](https://badgen.net/static/license/GPL-3.0/blue)![Badge](https://badgen.net/badge/icon/windows?icon=windows&label)
> [!NOTE]
> New bypass methods and Impero Bypasser coming soon, SUPERLIGHT 2

We also have MSIX bundled roblox

> [!IMPORTANT]
> New method! CVE-LSE-2025-04 - Dynamic Murderer

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


# OSN - CVE-LSE-2025-02

OSN - Obvious Self-Extracting DNS Blocker


OSN kills both DNS and the websocket requests and essentially completely remove any contact to lightspeed so now there is radio silence.

Lightspeed source code is extremely badly made. It exposes secret keys, logins, links, etc. Even GitHub scans and finds the secrets. So here are the DNS links you can block with the program, coming soon.

```"lsrelay-config-production.s3.amazonaws.com".toLowerCase(),
                    "lsrelay-extensions-production.s3.amazonaws.com".toLowerCase(),
                    "devices.filter.relay.school".toLowerCase(),
                    "production-gc.lsfilter.com".toLowerCase(),
                    "lightspeedsystems.app",
                    "stagingls.io",
                    "developmentls.io",
                    "lsrelayaccess.com",
                    "lsurl.me",
                    "lsmdm-production.s3.amazonaws.com",
                    "devices.lsclassroom.com",
                    "lsorchestration-production.amazonaws.com",
                    "lsaccess.me",
                    "www.googleapis.com",
                    "ajax.googleapis.com",
                    "googleapis.com",
                    "fonts.googleapis.com",
                    "login.i-ready.com",
                    "gm4nyg31l2.execute-api.us-west-2.amazonaws.com",
                    "5rw61tcrl5.execute-api.us-west-2.amazonaws.com",
                    "wsmfcvajyf.execute-api.us-west-1.amazonaws.com",
                    "development.lsclassroom.com",
                    "staging-preview.lsclassroom.com",
                    "preview.lsclassroom.com",
                    "hosted186.renlearn.com",
                    "z40.renlearn.com",
                    "z40.renlearnrp.com",
                    "z46.renlearn.com",
                    "z46.renlearnrp.com",
                    "hosted298.renlearn.com",
                    "realtime.ably.io",
                    "z05.renlearn.com",
                    "z05.renlearnrp.com",
                    "hosted88.renlearn.com",
                    "gce-beacons.gcp.gvt2.com",
                    "gce-beacons.gcp.gvt3.com",
                    "rest.ably.io",
                    "lightspeed-realtime.ably.io",
                    "a-fallback-lightspeed.ably.io",
                    "b-fallback-lightspeed.ably.io",
                    "c-fallback-lightspeed.ably.io",
                    "staging-bp-01.lsfilter.com"
```

***Remember to go through and check each link!!!! Some are essential Google endpoints!!***
