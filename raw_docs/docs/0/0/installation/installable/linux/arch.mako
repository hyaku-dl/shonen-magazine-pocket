# Installable - Linux - Arch Linux distro and derivatives

- Open your preferred terminal and run the following command:

    ```shell
    sudo pacman -Syyu --noconfirm curl
    curl -s ${VARS["scripts_url"]}/${"/".join(cwd.parts[2:4])}/li | sudo bash
    ```

- You can now use ${VARS["repo_name"]} by running the following command:

    ```shell
    ${VARS["project_name"]}
    ```
