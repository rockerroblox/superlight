<p align="center"
   <br>
   <img src="https://github.com/rockerroblox/superlight/blob/main/logo.png?raw=true">
   <br>
</p>

<h1 align="center">Superlight</h1>
<p align="center"><b>A school filter bypass framework</b></p>
<br>
<p align="center">
   <a href="#exploit-list" align="center">Exploit List</a>
   <a href="#instructions" align="center">Instructions</a>
   
</p>


<p align="center">
  <img src="https://badgen.net/badge/icon/windows?icon=windows&label" alt="Windows">
  <img src="https://badgen.net/static/license/GPL-3.0/blue" alt="GPL-3.0 License">
  <img src="https://badgen.net/static/Superlight/1.0/cyan" alt="Superlight 1.0">
</p>

---

``` ___ _   _ _ __   ___ _ __| (_) __ _| |__ | |_
/ __| | | | '_ \ / _ | '__| | |/ _` | '_ \| __|
\__ | |_| | |_) |  __| |  | | | (_| | | | | |_
|___/\__,_| .__/ \___|_|  |_|_|\__, |_| |_|\__|
          |_|                  |___/
```


# Description

**Superlight** is an exploit framework for school filtering programs, such as Lightspeed Alert Agent, Filter Agent, and Impero Classroom. Current **features:**

    • Extension removal
    • Websocket killer
    • Program killswitch (Work in progress)

The exploits Superlight contains block the WebSocket connections and website connections [via DNS] using a locally-ran script, which can be ran through multiple methods (see Instructions)

The system in place for exploit logging and categorising is known as LSE (Lightspeed Exploit) but is commonly referred to as CVE-LSE-XXXX-XX

LSE-2025-01 - Superlight 1 - OSN\
LSE-2025-02 - Superlight 2 - Decompilation Exploits (TBD)

Unfortunately, at this current moment it is unlikely for me to attain a Windows virtual machine to decompile the Filter Agent.

***

# Instructions

|____ **SafeRE**
|---- RunAsInvoker
|____ MSIX
|____ Live OS

## SafeRE (reccommended)

**SafeRE** is a method to install apps and change files in Windows Recovery Mode (rip BitLocker users 🥀🥀).

Boot into WinRE by holding shift and clicking the restart button. Click *Troubleshoot* - *Command Prompt*

Now there are a couple things you can do, you can edit files with the notepad or *load hives through regedit.*

You can then use **net user youruser password /add** and then **net localgroup administrators /add youruser**

Then login and run your script, but this is dangerous and you may get caught. If you do this, maybe consider the MSIX option.

## RunAsInvoker

Simple, use the included batch file to run without elevation.

## MSIX

This is one of the easiest options for the user, but hard as hell for me. First of all, you need to use the MSIX Packaging Tool to package the EXE file. Then you need a self-signed certificate that verifies, with a password and a timestamp,\
And 95% of the time it dosen't work. All you need to do is download the MSIX, add my certificate to your Trusted Root Certification Authorities and click Install.

There are 2 MSIX apps:
   • SUPERLIGHT client
   • Your bundled app

The SUPERLIGHT client is a coming-soon app that allows you to essentially sideload apps through it, play unblocked games, download MS Store apps and games, run exploits, update the client and much more.

Your bundled app is just, your bundled app.

If you want ways to achieve administrator to add the certificate, I'll add those guides later, but consider checking out the Titanium Network Discord for their Kajigs.

## Live OS

Get a USB drive, and install Rufus or Ventoy. Install a live OS Linux distro and use: **chntpw** to add admin users, or use the **Utilman** method.

# Exploit List

## PSW - CVE-LSE-2025-01

**PSW - Python Socket Worker** is an exploit for Lightspeed Filter Agent and **Lightspeed Alert Agent**, although primarily used for Alert Agent. It works by killing Lightspeed websocket connections and occupies ports.
It is the predecessor to OSN and is simply not worth using anymore.

## NPB - CVE-LSE-2025-02 (Severity: Low)
NPB - Non-Administrator Panic Button - is quite simply a panic button which shuts off your internet, turns your PC into aeroplane mode, clears your history, and your cache, blocks Lightspeed filter ports and then you can re-enable things with a button press in the GUI.


## OSN - CVE-LSE-2025-02

OSN - Obvious Self-Performing DNS Blocker

**OSN** kills DNS and HTTPS requests to Lightspeed, and optionally, Impero, and also kills WebSocket requests and occupies ports.

Lightspeed code exposes a lot of sensitive info, such as secret keys, tokens, access keys, links, ports, filter lists, etc.


