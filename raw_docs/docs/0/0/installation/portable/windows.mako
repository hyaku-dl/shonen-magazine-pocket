# Portable - Windows 7 and up

Part of the following is a summary of <a
    href="https://community.chocolatey.org/courses/installation/installing?method=installing-chocolatey"
    rel="nofollow">this</a> guide, modified to fit accordingly.

- Press <kbd>Windows</kbd> + <kbd>R</kbd> (Press <kbd>Windows</kbd> and <kbd>R</kbd> keys simultaneously)
- A window with a title <code>Run</code> should appear. Focus to the said window in the <code>Open:</code> text field by hovering the mouse towards the said text field and left-clicking the mouse and type <code>powershell</code> like illustrated below:
    <img alt="run_box_cmd" src="/assets/images/run_box_ps.png" />
- Press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Enter</kbd> (Press <kbd>Ctrl</kbd>, <kbd>Shift</kbd>, and <kbd>Enter</kbd> keys simultaneously).
- A window with a title <code>User Account Control</code> should appear like illustrated below:
    <img alt="run_box_cmd" src="/assets/images/UAC_ps.png" />

    Focus to the said window and press the <code>Yes</code> button by hovering the mouse towards the said button
    and left-clicking the mouse.
- Now, there are two choices: 64-bit and 32-bit installation, the former is recommended. Run the command corresponding your choice.

    - 64-bit:

        ```ps
        Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://${VARS["scripts_url"]}/${"/".join(cwd.parts[2:4])}/wp64'))
        ```

    - 32-bit:

        ```ps
        Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://${VARS["scripts_url"]}/${"/".join(cwd.parts[2:4])}/wp32'))
        ```

- You can now use ${VARS["repo_name"]} by running the following command:

    ```shell
    .\${VARS["project_name"]}\main.bat
    ```
