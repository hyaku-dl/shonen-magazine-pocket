# Programmatic - Windows 7 and up

- Press <kbd>Windows</kbd> + <kbd>R</kbd> (Press <kbd>Windows</kbd> and <kbd>R</kbd> keys simultaneously)
    <img alt="1" src="/assets/images/prerequisites/python/windows/1.png" />
    <img alt="1" src="/assets/images/prerequisites/python/windows/1.png" />
- Search for settings by typing "<code>Settings</code>" in the text field as shown below:
    <img alt="2" src="/assets/images/prerequisites/python/windows/2.png" />

    Press <kbd>Enter</kbd>.
- A window should pop up as shown below:
    <img alt="3" src="/assets/images/prerequisites/python/windows/3.png" />

    Press "<code>Apps</code>" in the selection below.
- You should be redirected to "<code>Apps &amp; Features</code>" as shown below:
    <img alt="4" src="/assets/images/prerequisites/python/windows/4.png" />

    Below the subtitle "<code>Apps &amp; Features</code>", press the hyperlink"<code>App execution aliases</code>".
- You should be redirected to "<code>App execution aliases</code>" as shown below:
    <img alt="5" src="/assets/images/prerequisites/python/windows/5.png" />

    Toggle the "<code>App installer</code>" for both "<code>python.exe</code>" and "<code>python3.exe</code>". Exit the settings app.
- Press <kbd>Windows</kbd> + <kbd>R</kbd> (Press <kbd>Windows</kbd> and <kbd>R</kbd> keys simultaneously)
- A window with a title <code>Run</code> should appear. Focus to the said window in the <code>Open:</code>
    text field by hovering the mouse towards the said text field and left-clicking the mouse and type
    <code>powershell</code> like illustrated below:
    <img alt="run_box_cmd" src="/assets/images/run_box_ps.png" />
- Press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Enter</kbd> (Press <kbd>Ctrl</kbd>, <kbd>Shift</kbd>, and <kbd>Enter</kbd> keys simultaneously).
- A window with a title <code>Windows Powershell</code> should appear. Focus to the said window by hovering the mouse towards the said window and left-clicking the mouse and type the following command:

    ```ps
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    choco install python
    choco install 7zip.install
    python3 -m pip install MangDL
    ```

- You can now use shonen-magazine-pocket programmatically!